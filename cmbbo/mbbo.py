#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2017-4-12
@author: Amy
'''
import time
import random
import math
import json
import sys
import copy
#from pyspark import SparkContext

def checkeffective(popu1):
    '''
    目标：检查当前population所有chrom的有效性，即vm-hm的拓扑中，hm资源请求量不能超过1.0
    '''
    # 将 popu1['p_cost'],popu1['m_cost']清零，并对迁移进化后的popu1['population']，重新统计各HM的资源使用情况（为了确保）
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            popu1['p_cost'][i][j] = 0
            popu1['m_cost'][i][j] = 0
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            tmp_position = popu1['population'][i][j]
            popu1['p_cost'][i][tmp_position] += popu1['rp'][j]
            popu1['m_cost'][i][tmp_position] += popu1['rm'][j]
        for x in range(popu1['num_var']):
            if popu1['p_cost'][i][x] > 1.0:
                return False
    return True


def range2rect(size, num_var):
    '''
    构造size x num_var 的矩阵
    '''
    res = range(size)
    for i in range(size):
        res[i] = range(num_var)
    # 简单写法
    #res = [[[] for j in range(num_var)] for i in range(size)]
    return res

def make_population(size, num_var, rp, rm, f, p_mutate, time_base, lambdaa):
    '''
    构造一个population，包含size个候选解chrom,每个chrom是由num_var个记录各vm所放置的pm下标组成的
    '''
    population = {
        'size': size,                                                       # int,population中chrom的个数
        'num_var': num_var,                                                 # int,chrom元素个数，即vm个数（同时假设HM个数也是num_var）
        'rp': rp,                                                           # list(num_var),所有vm的cpu demand
        'rm': rm,                                                           # list(num_var),所有vm的mem demand
        'f': f,                                                             # float，差分因子，系统运行前必须指定
        'p_mutate': p_mutate,                                               # float,突变概率
        'time_base': time_base,                                             # float,时间基数
        'lambdaa': tuple(lambdaa),                                          # tuple(size),所有chrom候选解的迁入率，rank值越小，越优秀，迁入率越小
        'population': range2rect(size, num_var),                            # size x num_var的矩阵，每代population的size个解集合
        'population0': range2rect(size, num_var),                           # 保存初始population的所有chroms
        'p_cost': range2rect(size, num_var),                                # size x num_var的矩阵，记录每个HM被请求的CPU总量
        'm_cost': range2rect(size, num_var),                                # size x num_var的矩阵，记录每个HM被请求的MEM总量
        'power_cost': [x*0 for x in range(size)],                           # list(size),记录当前代population中，每个chrom的能耗代价
        'v_balance_cost': [x*0 for x in range(size)],                         # list(size),记录当前population中,每个chrom的负载均衡指数
        'migration_time_cost': [x*0+time_base*num_var for x in range(size)],     # list(size),记录迁移时间，这里指定为固定值
        'rank': [x*0 for x in range(size)],                                 # list(size),记录每个chrom排名，rank值越大，排名越靠后
        'elite_power': 999999.0*num_var,                                    # float,记录每代种群中最优秀解的能耗代价值
        'elite_v_balance': 999999.0*num_var,                                  # float,记录每代种群中最优秀解的负载均衡指数
        'elite_migration_time': time_base*num_var,                          # float,........的迁移时间
        'elite_chrom': range(num_var)                                       # list(num_var)，保存每代种群中精英chrom
    }
    return population

def initialize_population(popu1):
    '''initialize chroms in population'''
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            popu1['population'][i][j] = 0
            popu1['p_cost'][i][j] = 0
            popu1['m_cost'][i][j] = 0
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            while True:
                tmp_position = random.randint(0, popu1['num_var']-1)                 # 为第i个chrom中第j个vm随机临时HM编号
                tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]       # 并统计第j个VM放于该临时HM位置后，HM的cpu使用量
                tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]       # 第j个vm放入该临时HM后，HM的mem使用量
                if tmp_p_cost < 1.0 and tmp_m_cost < 1.0:
                    popu1['population'][i][j] = tmp_position
                    popu1['p_cost'][i][tmp_position] = tmp_p_cost                    # 满足约束条件即可放入，即一个合理的候选解
                    popu1['m_cost'][i][tmp_position] = tmp_m_cost
                    break
    for i in range(popu1['size']):
        popu1['population0'][i] = tuple(popu1['population'][i])                      # 对初始化后的种群进行保存
    return popu1

def mbbode_migration(popu1):
    '''migrate SIVs among in population'''
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            rand_sum = random.random()
            lambda_scale = (popu1['lambdaa'][i] - popu1['lambdaa'][0]) / (popu1['lambdaa'][popu1['size']-1] - popu1['lambdaa'][0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
            if rand_sum < lambda_scale:                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
                index1 = random.randint(0, popu1['size']-1)
                index2 = random.randint(0, popu1['size']-1)
                while index1 == index2:
                    index2 = random.randint(0, popu1['size']-1)
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                tmp_position = int(popu1['population'][i][j] + popu1['f']*(popu1['population'][i][j] - popu1['population'][index1][j]) + popu1['f']*(popu1['population'][index1][j] - popu1['population'][index2][j] + 0.5)) % popu1['num_var']
                if tmp_position < 0:
                    tmp_position = -tmp_position
                while True:
                    tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]
                    tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]
                    if tmp_p_cost < 1.0 and tmp_m_cost < 1.0:                  # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
                        original_position = popu1['population'][i][j]
                        popu1['population'][i][j] = tmp_position
                        popu1['p_cost'][i][tmp_position] = tmp_p_cost
                        popu1['m_cost'][i][tmp_position] = tmp_m_cost
                        popu1['p_cost'][i][original_position] -= popu1['rp'][j]
                        popu1['m_cost'][i][original_position] -= popu1['rm'][j]
                        break
                    else:
                        tmp_position = (tmp_position + 1) % popu1['num_var']
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            if popu1['p_cost'][i][j] < 0.000001:
                popu1['p_cost'][i][j] = 0
            if popu1['m_cost'][i][j] < 0.000001:
                popu1['m_cost'][i][j] = 0
    if checkeffective(popu1):
        return popu1
    else:
        print "not effective in compute mbbode_migration"
        sys.exit()

def mbbode_mutation(popu1):
    '''mutate SIVs in a population'''
    for i in range(popu1['size']):
        for j in range(popu1['num_var']):
            rand_num = random.random()
            if rand_num < popu1['p_mutate']:                    # chromi的第j元素(vmj) 被突变率选中,随机生成新的SIV值，进行替换
                tmp_position = random.randint(0, popu1['num_var'] - 1)
                while True:
                    tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]
                    tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]
                    if tmp_p_cost < 1.0 and tmp_m_cost < 1.0:
                        original_position = popu1['population'][i][j]
                        popu1['population'][i][j] = tmp_position
                        popu1['p_cost'][i][tmp_position] = tmp_p_cost
                        popu1['m_cost'][i][tmp_position] = tmp_m_cost
                        popu1['p_cost'][i][original_position] -= popu1['rp'][j]
                        popu1['m_cost'][i][original_position] -= popu1['rm'][j]
                        break
                    else:
                        tmp_position = (tmp_position + 1) % popu1['num_var']
    if checkeffective(popu1):
        return popu1
    else:
        print "not effective in compute mbbode_mutation"
        sys.exit()


def mbbode_cost(popu1):
    '''compute the costs of three objectives in MBBO/DE algorithm'''
    # compute the power cost of popu1
    for i in range(popu1['size']):
        popu1['power_cost'][i] = 0.0
        for j in range(popu1['num_var']):
            x = popu1['p_cost'][i][j]
            if x > 0.0:
                popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)             # 计算size个chrom的能耗值  能耗与cpu使用率紧密关系

    # compute the v_balance cost of popu1
    for i in range(popu1['size']):
        popu1['v_balance_cost'][i] = 0.0
        load_index = range(popu1['num_var'])
        average_load_index = 0.0
        for j in range(popu1['num_var']):
            load_index[j] = 1.0 / (1.0005 - popu1['p_cost'][i][j]) / (1.0005 - popu1['m_cost'][i][j])  # 各chrom中每个vm的负载指数
            average_load_index += load_index[j]                                                        # 各chrom所有vms的总负载指数
        #average_load_index /= 50                                                                      # 此处50有问题，应该是实际承受负载的hm个数
        average_load_index /= popu1['num_var']                                                         # 各chrom的平均负载指数
        for j in range(popu1['num_var']):
            popu1['v_balance_cost'][i] = popu1['v_balance_cost'][i] + (load_index[j] - average_load_index)*(load_index[j] - average_load_index)
        #popu1['v_balance_cost'][i] = math.sqrt(popu1['v_balance_cost'][i] / 50)                           # 此处50有问题，应该是num_var值
        popu1['v_balance_cost'][i] = math.sqrt(popu1['v_balance_cost'][i] / popu1['num_var'])              # 各chrom的负载均衡代价值


    # # compute the migration_time_cost of popu1 without getting rid of invalid migration
    # for i in range(popu1['size']):
    #     popu1['migration_time_cost'][i] = 0
    #     for j in range(popu1['num_var']):
    #         if(popu1['population'][i][j] != popu1['population0'][i][j]):
    #             popu1['migration_time_cost'][i] += popu1['time_base']

    # compute the migration_time_cost of popu1 with getting rid of invalid migration
    for i in range(popu1['size']):
        popu1['migration_time_cost'][i] = 0
        for j in range(popu1['num_var']):
            if popu1['population'][i][j] != popu1['population0'][i][j]:
                popu1['migration_time_cost'][i] += popu1['time_base']                                 # 改变源，目标hm的vm需要迁移
                # 剔除无效迁移
                for x in range(j+1, popu1['num_var']):
                    if popu1['rp'][j] == popu1['rp'][x] and popu1['rm'][j] == popu1['rm'][x]:  # 若有2个虚拟机尺寸cpu,mem一样
                        # print 'i have enter the x loop and find one equal',j
                        if popu1['population0'][i][j] == popu1['population'][i][x]:            # vm_x将迁入的目标hm是vm_j的源hm,则直接将vm_x的目标hm改为vm_j的目标hm，vm_j不用进行迁移
                            popu1['population'][i][x] = popu1['population'][i][j]
                            popu1['population'][i][j] = popu1['population0'][i][j]
                            popu1['migration_time_cost'][i] -= popu1['time_base']                     # 节省1次迁移用时
                        elif popu1['population0'][i][x] == popu1['population'][i][j]:          # vm_j将迁入的目标hm是vm_x的源hm,则直接将vm_j的目标hm改为vm_x的目标hm，vm_x不用进行迁移
                            popu1['population'][i][j] = popu1['population'][i][x]
                            popu1['population'][i][x] = popu1['population0'][i][x]
                            popu1['migration_time_cost'][i] -= popu1['time_base']                     # 节省1次迁移用时
                    # print "don't find invalid migration\n"



    if checkeffective(popu1):
        return popu1
    else:
        print "not effective in compute mbbode_cost"
        sys.exit()


def mbbode_rank(popu1, hsi_list):
    '''
    compute each chrom rank of population with non-dominated sorting
    hsi_list 传入需要比较的代价目标
    '''
    # update the value of rank of each chrom
    for i in range(popu1['size']):
        popu1['rank'][i] = 0
    for i in range(popu1['size']):
        for j in range(i+1, popu1['size']):                                                            # 按照非支配解排序non-dominated sorting
            if popu1['power_cost'][i] < popu1['power_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['power_cost'][i] > popu1['power_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['v_balance_cost'][i] < popu1['v_balance_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['v_balance_cost'][i] > popu1['v_balance_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['migration_time_cost'][i] < popu1['migration_time_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['migration_time_cost'][i] > popu1['migration_time_cost'][j]:
                popu1['rank'][i] += 1

    # 寻找当前经过迁移突变后种群的排名rank最小值
    rank = popu1['rank'].index(min(popu1['rank']))
    # if popu1['elite_power'] > popu1['power_cost'][rank] and popu1['elite_v_balance'] > popu1['v_balance_cost'][i]:    # 若上一代精英解没有当前代最优解优秀，则替换之
    #     popu1['elite_power'] = popu1['power_cost'][rank]
    #     popu1['elite_v_balance'] = popu1['v_balance_cost'][rank]
    #     popu1['elite_migration_time'] = popu1['migration_time_cost'][rank]
    #     popu1['elite_chrom'] = popu1['population'][rank][:]
    # else:
    #     popu1['population'][0] = popu1['elite_chrom'][:]
    flag = False
    for u in hsi_list:
        if popu1['elite_'+u] > popu1[u+'_cost'][rank]:
            flag = True
            continue
        else:
            flag = False
            break
    if flag:
        popu1['elite_power'] = popu1['power_cost'][rank]
        popu1['elite_v_balance'] = popu1['v_balance_cost'][rank]
        popu1['elite_migration_time'] = popu1['migration_time_cost'][rank]
        popu1['elite_chrom'] = popu1['population'][rank][:]
    else:
        popu1['population'][0] = popu1['elite_chrom'][:]
    return popu1

def mbbode_get_best_chr(popu1, popu2):
    '''get the best chrom from RDD'''
    if popu1.power_cost < popu2.power_cost and popu1.v_balance_cost < popu2.v_balance_cost:
        return popu1
    return popu2

def get_best_cost(popu1, popu2):
    '''get the best cost from best_chrom'''
    best_cost = [0.0, 0.0, 0.0]
    if popu1['elite_power'] > popu2['elite_power'] and popu1['elite_v_balance'] > popu2['elite_v_balance']:
        best_cost[0] = popu2['elite_power']
        best_cost[1] = popu2['elite_v_balance']
        best_cost[2] = popu2['elite_migration_time']
    else:
        best_cost[0] = popu1['elite_power']
        best_cost[1] = popu1['elite_v_balance']
        best_cost[2] = popu1['elite_migration_time']
    return best_cost



def initVMResrcs(rp_u, rm_u, p, num_var):
    '''
    目标：随机生成测试虚拟机集中每个vm对cpu和mem的资源请求
    参数：
    rp_u是对cpu请求的指导变量，rm_u是对mem资源请求的指导变量，虚拟机对cpu，mem的最终需求量会以正态分布的形式落在以指导变量为期望的邻域附近
    p代表虚拟机的cpu和mem两种资源之间的相关系数，负责控制每台虚拟机对两种资源需求的关联程度
    num_var是需要生成的虚拟机个数
    '''
    rp = range(num_var)                                                  # 记录每个虚拟机cpu,mem请求量
    rm = range(num_var)
    for i in range(num_var):
        rp[i] = random.uniform(0, 2*rp_u)
        rm[i] = random.uniform(0, rm_u)
    for i in range(num_var):
        r = random.random()
        if (r < p and rp[i] >= rp_u) or (r >= p and rp[i] < rp_u):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            rm[i] += rm_u
        if rm[i] >= 1.0:                                               # 控制mem请求量合理性
            rm[i] -= 1.0
    return rp, rm

def migrateRate(size):
    '''
    目标：compute the Cosine migration rates，候选解越优秀迁入率越低，迁出率越高
    参数：
    size，初始种群中候选解的个数，即每代population中有size个chrom，每个chrom中有num_var个SIV
    '''
    lambdaa = range(size)                                               # 每个解对应一对迁入lambdaa迁出率mu,共有size个解
    mu = range(size)
    for i in range(size):
        lambdaa[i] = math.cos(float(size - (i + 1)) / size)             # 按照种群所有候选解排名后的顺序，依次求解余弦迁入率，rank值越小迁入率越小
        mu[i] = math.sin(float(size - (i + 1)) / size)                  # 迁出率
    return lambdaa, mu

def main(generation, size, num_var, p, hsi_list):
    '''
    目标：控制入口函数
    参数：
    generation，    种群迭代次数
    size，          population中chrom个数
    num_var，       每个chrom中SIV个数
    p，             VM对CPU,MEM两种资源请求的相关系数
    '''
    # initail some parameters of the MBBO/DE algorithm
    # generation = 1000
    # size = 10
    # num_var = 200
    p_mutate = 0.02                        # 高斯突变率（这里直接给出值没有进行计算）0.01
    f = 0.6                                # 差分因子
    rp_u = 0.25                            # VM请求CPU的指导变量
    rm_u = 0.25                            # VM请求MEM的指导变量
    p = p
    time_base = 65                         # 作为单台虚拟机迁移的基准时间

    # random create num_var vms with cpu,mem requirements
    # 为了与cmbbo做对比，这里采用cmbbo随机生成的方式进行赋值  rp, rm = initVMResrcs(rp_u, rm_u, p, num_var)
    rp = [0.27100308301093373, 0.47253617448485086, 0.29166113026471713, 0.25295716886000946, 0.0711556658565517, 0.3179055611908086, 0.4550972172073262, 0.46447625473649246, 0.13413414788225597, 0.05872624503765722, 0.24038938623846295, 0.45398104762109337, 0.25248350068690906, 0.18370787820885676, 0.26746656178349215, 0.4877195365009911, 0.22691901137977571, 0.4905863621336404, 0.2796166701264831, 0.20789205323475207, 0.12073753718843178, 0.06063010918719752, 0.3016460901561072, 0.028925091395117508, 0.2897262606163179, 0.13677453023266684, 0.12150875881267065, 0.07845118752246749, 0.4116848518330767, 0.31024543611135097, 0.10911452306645203, 0.3666567773359689, 0.23485558499153414, 0.023339793659812424, 0.49217284915233933, 0.13707682612043331, 0.4489723032262774, 0.2736659386330228, 0.3553041176710768, 0.22339591583215812, 0.012938600709828496, 0.36587130016372266, 0.29202217069697384, 0.27154049906665934, 0.30213649044077334, 0.48544538237333834, 0.3085649367750341, 0.38458449239266224, 0.3214852252999142, 0.46273503304898767, 0.24911549469788125, 0.41043630771848144, 0.3352982748362221, 0.238580214590291, 0.04087723013176031, 0.3780049985424545, 0.33903242843630305, 0.19354073463399868, 0.2503226422155127, 0.13654246439379503, 0.06499730190281056, 0.3147464176534923, 0.4372401997328494, 0.0623906516670959, 0.09254204326669174, 0.30908420530534014, 0.43552331533976785, 0.10163284482354962, 0.4326548699811369, 0.4962611749621776, 0.4616409563352538, 0.02861867713004196, 0.4853220001030228, 0.38350373096602336, 0.35127762995163064, 0.14360361792684423, 0.481783562436264, 0.4667673677446844, 0.03870301352056871, 0.3963096003560373, 0.2593297880003198, 0.3164900024299173, 0.48989473356377466, 0.4599949014668202, 0.04035083291296043, 0.37658571564488497, 0.35560476580942685, 0.2842361411341277, 0.05267982442910496, 0.4721655529230384, 0.30742520043163385, 0.49256990320994876, 0.4154014893514008, 0.31427537374763287, 0.4418682619280884, 0.05209097352844966, 0.48831227833722823, 0.21498998733770192, 0.40786701966013333, 0.16963566116462891, 0.3974886243280375, 0.32200385198046794, 0.33807091374664217, 0.17570813226645227, 0.37326657847198597, 0.07698872050488148, 0.48318920181186686, 0.1940521010943151, 0.028444915449346686, 0.4030029193810309, 0.36382617125656463, 0.11229257257625974, 0.009581235460502213, 0.4890240933239285, 0.3302200615321202, 0.2549078787117144, 0.2859255631796829, 0.31981404027502863, 0.1412534614169365, 0.20465152872875192, 0.3673378214248758, 0.0851754354496318, 0.14966974256298038, 0.06133213289316697, 0.13711471533405994, 0.12307411977390087, 0.21888181468323786, 0.23446936742206487, 0.09694481795705234, 0.365334294495704, 0.11632946891865609, 0.40893072068633524, 0.3934049773702517, 0.08957855947180487, 0.013606809094504013, 0.3495327625031082, 0.3868852150971912, 0.40930526870629896, 0.425963527472579, 0.3924228840917364, 0.18935740658136785, 0.36141416625151623, 0.49387090444431947, 0.4656490954149132, 0.053546644082470174, 0.38481513721686283, 0.3383322033964793, 0.17271631033724433, 0.13430389881686383, 0.31143595965383486, 0.3164019170207928, 0.23817049939294577, 0.4379324720998254, 0.2917960624441971, 0.3668083349130668, 0.018145101415861065, 0.47638742668637435, 0.12250586596320295, 0.42731999947184895, 0.43465925572788333, 0.23560186610087464, 0.4049788890338728, 0.48907193408187627, 0.19579128263926204, 0.23927958568638474, 0.10303988123922558, 0.3642948701932237, 0.06485135597491476, 0.45920110285618976, 0.09223169031024181, 0.4133551824883866, 0.3904255037007202, 0.47950305208578015, 0.4267755343962325, 0.024369855766055215, 0.34094353201707195, 0.45845907217355825, 0.46987563331640686, 0.43671597090948355, 0.35927915404308247, 0.37122982233212387, 0.2314945256171928, 0.08857938113614172, 0.4258429597382398, 0.42030898285617, 0.05145670926943502, 0.09966585298469127, 0.18246509227061924, 0.24239896801049993, 0.3670064450468022, 0.3015227403746993, 0.14049871342287218, 0.06651136080719455, 0.392579595450299, 0.034664581458275334, 0.2982070186281772, 0.37249909703424317, 0.3417662865562231, 0.08531854666153055, 0.021530277442558032]
    rm = [0.3505193727629189, 0.4878365772326554, 0.40469514723489086, 0.4005460341387705, 0.23546460252328602, 0.41826500958111656, 0.37085709566300007, 0.4127320917192182, 0.004267918838915946, 0.06716054003701269, 0.21946242751815415, 0.49530267928124316, 0.4294585534926114, 0.13765753163721015, 0.4617152182043857, 0.37456118638737695, 0.24559200510161222, 0.3113371294945845, 0.2762068691663795, 0.03564892624212343, 0.010069478572617585, 0.22967726489361776, 0.4854775491170144, 0.19777848211228774, 0.26432068415551097, 0.09146595552989553, 0.04946288354507569, 0.18447148336451286, 0.4335776282673599, 0.40517898293495397, 0.14691110060132165, 0.26395206172857644, 0.2329817770463271, 0.015291209535468087, 0.43812193929192356, 0.18740638876584634, 0.382106623833105, 0.31470700539984026, 0.4815097263291738, 0.18954375433547932, 0.033626150593739856, 0.42459726633694495, 0.3576373007558272, 0.4236876576022912, 0.3684092821234306, 0.2637899336140895, 0.29168748782447435, 0.26218780990263746, 0.3417408803886633, 0.3433944528284467, 0.2404640330648532, 0.3446355259007192, 0.33272239464523234, 0.026007591133210495, 0.19813217078458634, 0.30857412740837165, 0.28445117892423055, 0.15887146359673943, 0.4202172761298759, 0.1608371848229952, 0.01835399455607742, 0.2977228977877091, 0.47357277748482546, 0.013402663357483469, 0.06268136435153354, 0.34074805058675944, 0.38169126342278303, 0.13314279056101952, 0.45032661589384987, 0.2608036589147227, 0.37639589456054146, 0.20887832749224713, 0.2681068877290635, 0.37055107509921525, 0.3738199800381681, 0.010245435248755652, 0.3492504795023429, 0.35473212027354656, 0.022551335436165915, 0.2735091455164408, 0.4391152491328004, 0.30268581542644635, 0.4740808393402245, 0.36449594942320745, 0.09063270643912194, 0.29308680213608684, 0.3953198673596981, 0.2651725759921571, 0.21245423897940374, 0.31215382611196196, 0.48320273969091265, 0.254296496991705, 0.30998940477847403, 0.359402163262497, 0.4505383777026774, 0.027604875133107748, 0.2614172100976874, 0.012817307234968545, 0.44656283013681225, 0.10592499398784644, 0.4761036497803002, 0.3444238491362477, 0.4258856845606046, 0.1644602324396401, 0.29000482139109, 0.12439941962132356, 0.4071237699684714, 0.11438731272933766, 0.08234366510860167, 0.3610800342848533, 0.2631827746751508, 0.15069598332960726, 0.23564492161589376, 0.37430077250130056, 0.42707656817072803, 0.34224062274041045, 0.4951023997526991, 0.35264851131823094, 0.09473310739742993, 0.24740617585375035, 0.26299770787341403, 0.01589245387197849, 0.18238753136458946, 0.11076991369176847, 0.04681113225583394, 0.1853921767905411, 0.18745464762768235, 0.23774034804880145, 0.014229722025369373, 0.47477703825894874, 0.22403304119428627, 0.45949248020474426, 0.4416761631459476, 0.02186282655638072, 0.2061850450808009, 0.2746729023860063, 0.29037512300774915, 0.2756958329244799, 0.29075037008892834, 0.39118132613130685, 0.035437406701261054, 0.4340578951425139, 0.38100955615880133, 0.2602205222391305, 0.16129486533468293, 0.2614726714317524, 0.49470910148724356, 0.031231773140053404, 0.024955420009052792, 0.37067818082108683, 0.4887803731062409, 0.1948412565748366, 0.4381370854552116, 0.4016770198927485, 0.4773873412218854, 0.2292447735821627, 0.4507826513874317, 0.15056244267512187, 0.3616386784099921, 0.4477903516730293, 0.19043355472290685, 0.49211140908475604, 0.4319209353712953, 0.023838998195905597, 0.19210120831189711, 0.16108734173016828, 0.4459530518193606, 0.08375882852046473, 0.2866900468950916, 0.08937937314997352, 0.2751189932389356, 0.467526649134708, 0.31360582703675677, 0.3071354695622348, 0.009871927414298931, 0.42976222971186995, 0.4818312899111704, 0.3927826874941396, 0.3669884835791826, 0.3777452435578258, 0.44585262461406194, 0.015308786876416486, 0.17330176351886256, 0.4783063258824488, 0.2582787687475157, 0.00010428280446964089, 0.09954240185137703, 0.015975799015606196, 0.21970520405597901, 0.32975280910989657, 0.4190255909444197, 0.085956714928144, 0.14321190508354734, 0.28825377792269335, 0.006987282745792411, 0.27384482362684637, 0.4243463074660594, 0.4106804729410944, 0.06832797147911499, 0.201022160679294]
    # compute each chrom immgrate rate and emgrate rate of all sorted chroms
    lambdaa, mu = migrateRate(size)


    # 初始populations
    init_population = make_population(size, num_var, rp, rm, f, p_mutate, time_base, lambdaa)
    init_population = initialize_population(init_population)
    init_population = mbbode_cost(init_population)
    init_population = mbbode_rank(init_population, hsi_list)

    ## 初始种群的代价即候选解
    tmp = random.randint(0, size-1)           # 从每个群岛的population中size个随机选出第tmp各解
    save_chrom = init_population['population'][tmp]             # 随机挑选的第tmp个初始候选解，代表MBBO执行前vm-hm拓扑关系
    save_cost = (init_population['power_cost'][tmp], init_population['v_balance_cost'][tmp], init_population['migration_time_cost'][tmp]) # 第tmp个初始候选解的3个HSI代价值

    elite_cost = {'power': 9999.9*num_var, 'v_balance': 9999.9*num_var, 'migration_time': time_base*num_var}   # 初设的全局精英解能耗代价、负载均衡指数、迁移时间
    save_elite_cost = {'power': 0, 'v_balance': 0, 'migration_time': 0}               # 用于保存每一代的全局最优解，并在新的一代时比较有否变化，只有改变后才会打印，否则不打印
    time1 = time.time()                       # 算法迭代进化开始时间戳

    for g in range(generation):               # 设置最大迭代次数

        init_population = mbbode_migration(init_population)
        init_population = mbbode_mutation(init_population)
        init_population = mbbode_cost(init_population)
        init_population = mbbode_rank(init_population, hsi_list)

        # 全局最优解替换
        # if elite_cost['power'] > init_population['elite_power'] and elite_cost['v_balance'] > init_population['elite_v_balance']:
        #     elite_cost['power'] = init_population['elite_power']
        #     elite_cost['v_balance'] = init_population['elite_v_balance']
        #     elite_cost['migration_time'] = init_population['elite_migration_time']
        flag = False
        for u in hsi_list:
            if elite_cost[u] > init_population['elite_'+u]:
                flag = True
                continue
            else:
                flag = False
                break
        if flag:
            elite_cost['power'] = init_population['elite_power']
            elite_cost['v_balance'] = init_population['elite_v_balance']
            elite_cost['migration_time'] = init_population['elite_migration_time']


        # 展示改变后的全局最优解
        if save_elite_cost['power'] != elite_cost['power'] or save_elite_cost['v_balance'] != elite_cost['v_balance'] or save_elite_cost['migration_time'] != elite_cost['migration_time']:    # 每一代全局最优解有变化时才会记录并打印
            print elite_cost
            save_elite_cost = copy.deepcopy(elite_cost)

    time2 = time.time()
    print 'Time cost: ', (time2 - time1), '\n'
    print 'the init chrom maybe is %s, use %s pms, the cost is %s' %(save_chrom, len(set(save_chrom)), save_cost)
    print 'after mbbo, chrom maybe is %s, use %s pms' %(init_population['elite_chrom'], len(set(init_population['elite_chrom'])))


if __name__ == '__main__':
    '''
    hsi_list：可选String： power、v_balance
    '''
    hsi_list = ['power','h_balance']
    if 'h_balance' in hsi_list:
        print "剔除无效的h_balance"
        hsi_list.remove('h_balance')
    main(500, 10, 200, 1.0, hsi_list)
