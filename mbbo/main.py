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
            if (popu1['p_cost'][i][x] > 1.0):
                return False
    return True


def range2rect(size, num_var):
    #构造size x num_var 的矩阵
    res = range(size)
    for i in range(size):
        res[i] = range(num_var)
    # 简单写法
    #res = [[[] for j in range(num_var)] for i in range(num_var)]
    return res

def make_population(size, num_var, rp, rm, f, p_mutate, time_base, lambdaa):
    #构造一个population，包含size个候选解chrom,每个chrom是由num_var个记录各vm所放置的pm下标组成的
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
        'balance_cost': [x*0 for x in range(size)],                         # list(size),记录当前population中,每个chrom的负载均衡指数
        'migration_time': [x*0+time_base*num_var for x in range(size)],     # list(size),记录迁移时间，这里指定为固定值
        'rank': [x*0 for x in range(size)],                                 # list(size),记录每个chrom排名，rank值越大，排名越靠后
        'elite_power': 999999.0*num_var,                                    # float,记录每代种群中最优秀解的能耗代价值
        'elite_balance': 999999.0*num_var,                                  # float,记录每代种群中最优秀解的负载均衡指数
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
            while(True):
                tmp_position = random.randint(0, popu1['num_var']-1)                 # 为第i个chrom中第j个vm随机临时HM编号
                tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]       # 并统计第j个VM放于该临时HM位置后，HM的cpu使用量
                tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]       # 第j个vm放入该临时HM后，HM的mem使用量
                if(tmp_p_cost < 1.0 and tmp_m_cost < 1.0):
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
            if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
                index1 = random.randint(0, popu1['size']-1)
                index2 = random.randint(0, popu1['size']-1)
                while(index1 == index2):
                    index2 = random.randint(0, popu1['size']-1)
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                tmp_position = int(popu1['population'][i][j] + popu1['f']*(popu1['population'][i][j] - popu1['population'][index1][j]) + popu1['f']*(popu1['population'][index1][j] - popu1['population'][index2][j] + 0.5)) % popu1['num_var']
                if(tmp_position < 0):
                    tmp_position = -tmp_position
                while(True):
                    tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]
                    tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]
                    if(tmp_p_cost < 1.0 and tmp_m_cost < 1.0):                  # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
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
            if(popu1['p_cost'][i][j] < 0.000001):
                popu1['p_cost'][i][j] = 0
            if(popu1['m_cost'][i][j] < 0.000001):
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
            if(rand_num < popu1['p_mutate']):                                 # chromi的第j元素(vmj) 被突变率选中,随机生成新的SIV值，进行替换
                tmp_position = random.randint(0, popu1['num_var'] - 1)
                while(True):
                    tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]
                    tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]
                    if(tmp_p_cost < 1.0 and tmp_m_cost < 1.0):
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
            if(x > 0.0):
                popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)             # 计算size个chrom的能耗值  能耗与cpu使用率紧密关系

    # compute the balance cost of popu1
    for i in range(popu1['size']):
        popu1['balance_cost'][i] = 0.0
        load_index = range(popu1['num_var'])
        average_load_index = 0.0
        for j in range(popu1['num_var']):
            load_index[j] = 1.0 / (1.0005 - popu1['p_cost'][i][j]) / (1.0005 - popu1['m_cost'][i][j])  # 各chrom中每个vm的负载指数
            average_load_index += load_index[j]                                                        # 各chrom所有vms的总负载指数
        #average_load_index /= 50                                                                      # 此处50有问题，应该是num_var
        average_load_index /= popu1['num_var']                                                         # 各chrom的平均负载指数
        for j in range(popu1['num_var']):
            popu1['balance_cost'][i] = popu1['balance_cost'][i] + (load_index[j] - average_load_index)*(load_index[j] - average_load_index)
        #popu1['balance_cost'][i] = math.sqrt(popu1['balance_cost'][i] / 50)                           # 此处50有问题，应该是num_var值
        popu1['balance_cost'][i] = math.sqrt(popu1['balance_cost'][i] / popu1['num_var'])              # 各chrom的负载均衡代价值

    # compute the migration_time of popu1
    for i in range(popu1['size']):
        popu1['migration_time'][i] = 0
        for j in range(popu1['num_var']):
            if(popu1['population'][i][j] != popu1['population0'][i][j]):
                popu1['migration_time'][i] += popu1['time_base']

    if checkeffective(popu1):
        return popu1
    else:
        print "not effective in compute mbbode_cost"
        sys.exit()


def mbbode_rank(popu1):
    '''compute each chrom rank of population with non-dominated sorting'''
    # update the value of rank of each chrom
    for i in range(popu1['size']):
        popu1['rank'][i] = 0
    for i in range(popu1['size']):
        for j in range(i+1, popu1['size']):                                                            # 按照非支配解排序non-dominated sorting
            if(popu1['power_cost'][i] < popu1['power_cost'][j]):
                popu1['rank'][j] += 1
            elif(popu1['power_cost'][i] > popu1['power_cost'][j]):
                popu1['rank'][i] += 1
            if(popu1['balance_cost'][i] < popu1['balance_cost'][j]):
                popu1['rank'][j] += 1
            elif(popu1['balance_cost'][i] > popu1['balance_cost'][j]):
                popu1['rank'][i] += 1
            if(popu1['migration_time'][i] < popu1['migration_time'][j]):
                popu1['rank'][j] += 1
            elif(popu1['migration_time'][i] > popu1['migration_time'][j]):
                popu1['rank'][i] += 1
    rank = 999999
    for i in range(popu1['size']):
        if(rank > popu1['rank'][i]):
            rank = popu1['rank'][i]                                                                    # 查找最优秀解，rank最小
    for i in range(popu1['size']):
        if(rank == popu1['rank'][i]):                                                                  # 获取该最优秀解size编号
            if(popu1['elite_power'] > popu1['power_cost'][i] and popu1['elite_balance'] > popu1['balance_cost'][i]):    # 若上一代精英解没有当前代最优解优秀，则替换之
                popu1['elite_power'] = popu1['power_cost'][i]
                popu1['elite_balance'] = popu1['balance_cost'][i]
                popu1['elite_migration_time'] = popu1['migration_time'][i]
                for j in range(popu1['num_var']):
                    popu1['elite_chrom'][j] = popu1['population'][i][j]
            else:
                for j in range(popu1['num_var']):                                                     # 若当前代最优解没有精英解优秀，则精英解保留不变并用其替换当代最优解（即下标为0的chrom）
                    popu1['population'][0][j] = popu1['elite_chrom'][j]
    return popu1

def mbbode_get_best_chr(popu1, popu2):
    '''get the best chrom from RDD'''
    if(popu1.power_cost < popu2.power_cost and popu1.balance_cost < popu2.balance_cost):
        return popu1
    else:
        return popu2

def get_best_cost(popu1, popu2):
    '''get the best cost from best_chrom'''
    best_cost = [0.0, 0.0, 0.0]
    if(popu1['elite_power'] > popu2['elite_power'] and popu1['elite_balance'] > popu2['elite_balance']):
        best_cost[0] = popu2['elite_power']
        best_cost[1] = popu2['elite_balance']
        best_cost[2] = popu2['elite_migration_time']
    else:
        best_cost[0] = popu1['elite_power']
        best_cost[1] = popu1['elite_balance']
        best_cost[2] = popu1['elite_migration_time']
    return best_cost

def createJSON(init_population1,save_chrom,save_cost,HSI_history,performance):
    '''
    目标：构造json文件，记录MBBO算法中的中间/最终结果保存
    参数：
    init_population1, 是整个MBBO算法都会去change的population字典类型
    save_chrom， 随机保存的一组初始候选解
    save_cost, 该随机挑选的初始解对应的3个HSI代价值
    '''
    #data字典中分别存储vm数量、pm数量、vm的cpu,mem尺寸、pm资源cpu,mem被占用量、state下标为pm，内容为该pm上的vm编号、
    #plan为每个vm的迁移src与des的hm编号，若不需要迁移则为空、
    #HSI_cost保存2个元组，分别保存初始的(power_cost,balance_cost,migration_time)和MBBO后精英解的(elite_power,elite_balance,elite_migration_time)
    data = { 'vms_num': init_population1['num_var'], \
        'pms_num': init_population1['num_var'], \
		'vms':[], \
        'state1':{'pms_used':[],'vms_place':[]}, \
        'state0':{'pms_used':[],'vms_place':[]}, \
        'plan':[], \
        'HSI_cost':[], \
        'HSI_history': HSI_history, \
        'performance': performance}

    # 统计每台pm上拥有的vm编号
    vms_place = [ [] for i in range(init_population1['num_var'])] # num_var个pms
    for vm in range(len(init_population1['elite_chrom'])):
        pm = init_population1['elite_chrom'][vm]
        vms_place[pm].append(vm)
    data['state1']['vms_place'] = vms_place

    vms_place = [ [] for i in range(init_population1['num_var'])] # num_var个pms
    for vm in range(len(save_chrom)):
        pm = save_chrom[vm]
        vms_place[pm].append(vm)
    data['state0']['vms_place'] = vms_place

    # 统计每个vm的cpu,mem请求量
    vms = [ [] for i in range(init_population1['num_var']) ]
    for i in range(init_population1['num_var']):
        p = init_population1['rp'][i]
        m = init_population1['rm'][i]
        vms[i] = [p, m]
    data['vms'] = vms

    # 统计每台pm的cpu,mem被请求量
    data['state1']['pms_used'] = [[0,0]]*init_population1['num_var']
    for pm in range(init_population1['num_var']):
        all_p,all_m = 0,0
        for vm in data['state1']['vms_place'][pm]:
            all_p += init_population1['rp'][vm]  # 计算当前pm上所有vm占用的cpu
            all_m += init_population1['rm'][vm]  # 计算当前pm上所有vm占用的mem
        data['state1']['pms_used'][pm] = [all_p,all_m]

    data['state0']['pms_used'] = [[0,0]]*init_population1['num_var']
    for pm in range(init_population1['num_var']):
        all_p,all_m = 0,0
        for vm in data['state0']['vms_place'][pm]:
            all_p += init_population1['rp'][vm]  # 计算当前pm上所有vm占用的cpu
            all_m += init_population1['rm'][vm]  # 计算当前pm上所有vm占用的mem
        data['state0']['pms_used'][pm] = [all_p,all_m]



    # 迁移对统计
    data['plan'] = [ [] for i in range(init_population1['num_var'])]
    for vm in range(init_population1['num_var']):
        #if (save_chrom[vm] != init_population1['elite_chrom'][vm]):   # 如果初始候选解中某vm存放的hm编号不等于MBBO之后精英解该vm存放的hm编号，则认为需要迁移，两个hm编号分别为src,des位置
        data['plan'][vm] = [save_chrom[vm],init_population1['elite_chrom'][vm]]

    # 能耗，负载指数，迁移时间的统计
    elite_cost = (init_population1['elite_power'],init_population1['elite_balance'],init_population1['elite_migration_time'])
    data['HSI_cost'].append(save_cost)
    data['HSI_cost'].append(elite_cost)

    # 导出为json文件
    json.dump(data, open('../viz/data-mbbo-{g}.json'.format(g=data['performance'][0]),'w'),indent=2)
    return True


def initVMResrcs(rp_u,rm_u,p,num_var):
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
        if((r < p and rp[i] >= rp_u) or (r >= p and rp[i] < rp_u)):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            rm[i] += rm_u
        if(rm[i] >= 1.0):                                               # 控制mem请求量合理性
            rm[i] -= 1.0
    return rp,rm

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
    return lambdaa,mu

def main(generation,size,num_var,p):
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
    p_mutate = 0.01                        # 高斯突变率（这里直接给出值没有进行计算）
    f = 0.6                                # 差分因子
    rp_u = 0.25                            # VM请求CPU的指导变量
    rm_u = 0.25                            # VM请求MEM的指导变量
    # p = 1.0
    time_base = 65                         # 作为单台虚拟机迁移的基准时间

    # random create num_var vms with cpu,mem requirements
    rp,rm = initVMResrcs(rp_u,rm_u,p,num_var)
    # compute each chrom immgrate rate and emgrate rate of all sorted chroms
    lambdaa,mu = migrateRate(size)


    # deployed in Spark, here father_size is the number of populations in MBBO/DE
    father_size = 1                                                     # 初始father_size个populations
    init_population = range(father_size)
    for i in range(father_size):                                        # 对father_size个初始populations分别进行初始化和并计算HSI及进行排名
        init_population[i] = make_population(size, num_var, rp, rm, f, p_mutate, time_base, lambdaa)
        init_population[i] = initialize_population(init_population[i])
        init_population[i] = mbbode_cost(init_population[i])
        init_population[i] = mbbode_rank(init_population[i])

    #sc = SparkContext(appName="Paralleled MBBO/DE algorithm")
    ## SparkContext():Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster,and can be used to create RDD and broadcast variables on that cluster

    elite_cost = [9999.9*num_var, 9999.9*num_var, time_base*num_var]   # 初设的全局精英解能耗代价、负载均衡指数、迁移时间
    HSI_values = []
    HSI_ts = []
    save_elite_cost = [0,0,0]
    time1 = time.time()                                                # 算法迭代进化开始时间戳

    for g in range(generation):                                        # 设置最大迭代次数
        #pop = sc.parallelize(init_population)                         #parallelize()：Distribute a local Python collection to form an RDD
        #init_population = pop.map(mbbode_migration).map(mbbode_mutation).map(mbbode_cost).map(mbbode_rank).collect()  #RDD.map():Return a new RDD by applying a function to each element of this RDD
        init_population[0] = mbbode_migration(init_population[0])
        init_population[0] = mbbode_mutation(init_population[0])
        init_population[0] = mbbode_cost(init_population[0])
        init_population[0] = mbbode_rank(init_population[0])


        tmp = random.randint(0,size-1)                                 # 从每个群岛的population中size个随机选出第tmp各解
        save_chrom = init_population[0]['population'][tmp]             # 随机挑选的第tmp个初始候选解，代表MBBO执行前vm-hm拓扑关系
        save_cost = (init_population[0]['power_cost'][tmp],init_population[0]['balance_cost'][tmp],init_population[0]['migration_time'][tmp]) # 第tmp个初始候选解的3个HSI代价值


        for i in range(father_size):                                   # 获取全局最优解的能耗代价、负载均衡指数、以及迁移时间
            if(elite_cost[0] > init_population[i]['elite_power'] and elite_cost[1] > init_population[i]['elite_balance']):
                elite_cost[0] = init_population[i]['elite_power']
                elite_cost[1] = init_population[i]['elite_balance']
                elite_cost[2] = init_population[i]['elite_migration_time']
        if (save_elite_cost[0] != elite_cost[0] or save_elite_cost[1] != elite_cost[1] or save_elite_cost[2] != elite_cost[2]):
            print elite_cost[0], elite_cost[1], elite_cost[2]
            save_elite_cost = elite_cost[:]
            HSI_values.append(save_elite_cost)
            HSI_ts.append(time.time() - time1)

    HSI_history = {'values': HSI_values, 'ts': HSI_ts}                  # HSI_values，HSI_ts分别保存每次迭代变化后的3个HSI cost值及该次迭代时间用于绘图
    time2 = time.time()
    time_sim = time2 - time1                                                # 算法迭代进化结束时间戳
    print 'Time cost: ', (time2 - time1), '\n'
    time1 = time.strftime('%H:%M:%S',time.localtime(time1))
    time2 = time.strftime('%H:%M:%S',time.localtime(time2))
    print time1,time2
    print 'the init chrom maybe is %s, use %s pms' %(save_chrom,len(set(save_chrom)))
    print 'after mbbo, chrom maybe is %s, use %s pms' %(init_population[0]['elite_chrom'],len(set(init_population[0]['elite_chrom'])))
    #sc.stop()
    performance = [generation,time1,time2,time_sim]
    if (createJSON(init_population[0],save_chrom,save_cost,HSI_history,performance)):
        print "json file has writen"

if __name__ == '__main__':
    main(10000,10,200,1.0)
