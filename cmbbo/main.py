#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2017-5-2
@author: Amy
'''
import time
import random
import math
import json
import sys
#from pyspark import SparkContext

def initDocker(rp_u,rm_u,p,num_var):
    '''
    目标：随机生成测试虚拟机集中每个vm对cpu和mem的资源请求
    参数：
    rp_u是对cpu请求的指导变量，rm_u是对mem资源请求的指导变量，虚拟机对cpu，mem的最终需求量会以正态分布的形式落在以指导变量为期望的邻域附近
    p代表虚拟机的cpu和mem两种资源之间的相关系数，负责控制每台虚拟机对两种资源需求的关联程度
    num_var是需要生成的虚拟机个数
    '''
    c_rp = range(num_var)                                                  # 记录每个虚拟机cpu,mem请求量
    c_rm = range(num_var)
    for i in range(num_var):
        c_rp[i] = random.uniform(0, 2*rp_u)
        c_rm[i] = random.uniform(0, rm_u)
    for i in range(num_var):
        r = random.random()
        if((r < p and c_rp[i] >= rp_u) or (r >= p and c_rp[i] < rp_u)):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            c_rm[i] += rm_u
        if(c_rm[i] >= 1.0):                                               # 控制mem请求量合理性
            c_rm[i] -= 1.0
    #print "len(c_rp)= %s,len(c_rm) = %s" %(len(c_rp),len(c_rm))
    return c_rp,c_rm

def initVM(c_rp,c_rm,rp_option,rm_option,num_var):
    '''
    持续查找可以容纳所有容器的vm：
    传入cpu参考列表rp_option,和mem可选列表rm_option
    c_rp,c_rm为已知的num_var个docker容器的尺寸
    num_var是容器个数，初始假设vm个数等于docker个数
    返回：虚拟机的num_var个尺寸元组序列
    '''
    v_rp = []
    v_rm = []
    i = 0
    while (True):
        if (i == num_var):
            #print "len(v_rp)= %s,len(v_rm) = %s" %(len(v_rp),len(v_rm))
            return v_rp,v_rm
        rp = random.choice(rp_option)
        rm = random.choice(rm_option)
        if( rp >= c_rp[i] and rm >= c_rm[i]):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            v_rp.append(rp)
            v_rm.append(rm)
            i += 1
        else:
            continue

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


def checkeffective(popu1,size,num_var):
    '''
    判断候选解的有效性
    '''
    # 先清空各vm,pm的资源使用率
    for i in xrange(size):
        for j in xrange(num_var):
            popu1['v_p_cost'][i][j] = 0
            popu1['v_m_cost'][i][j] = 0
            popu1['h_p_cost'][i][j] = 0
            popu1['h_m_cost'][i][j] = 0
    # 逐一按照候选解，计算实际占用的vm,hm资源
    vm_used_id = [ [] for x in xrange(size)]        # 避免相同vm同时被映射的不同hm的错误
    for i in xrange(size):
        for j in xrange(num_var):                   # 容器编号
            flag = True
            v_id = popu1['population'][i][j][0]
            h_id = popu1['population'][i][j][1]
            popu1['v_p_cost'][i][v_id] += popu1['c_rp'][j]
            popu1['v_m_cost'][i][v_id] += popu1['c_rm'][j]
            for x,y in vm_used_id[i]:                     # 保证已安排映射的vm被再次安排
                if (x == v_id):
                    flag = False
            if flag:
                popu1['h_p_cost'][i][h_id] += popu1['v_rp'][v_id]
                popu1['h_m_cost'][i][h_id] += popu1['v_rm'][v_id]
                vm_used_id[i].append((v_id,h_id))
        for x in xrange(num_var):
            if (popu1['v_p_cost'][i][x] > popu1['v_rp'][x] or popu1['v_m_cost'][i][x] > popu1['v_rm'][x] or popu1['h_p_cost'][i][x] > 1.0 or popu1['h_m_cost'][i][x] > 1.0):
                return False
    return True


def range2rect(size,num_var,type0):
    '''
    构造size * num_var 的矩阵
    ！！注意：python中list的引用可能造成全局参数的同时更改
    '''
    # if type0 == [0,0]:     # 注意type0 是引用类型，若引用的是list，则更改type0的值倒置所有通过type0进行list赋值的都会被更改
    #     res = [[ [0,0] for j in range(num_var)] for i in range(size)]
    # else:
    res = [[ type0 for j in range(num_var)] for i in range(size)]
    return res

def make_population(size, num_var,c_rp,c_rm,v_rp,v_rm,time_base): #    作为全局变量，按照需要传入各方法中 f, p_mutate, time_base, lambdaa):
    '''
    构造一个population，包含size个候选解chrom,每个chrom是num_var个分别记录该容器所在的vm和hm编号的元组
    '''
    population0 = {
        'c_rp': c_rp,                                                       # 每个容器的cpu请求
        'c_rm': c_rm,                                                       # 每个容器的mem请求
        'v_rp': v_rp,                                                       # 每个vm的cpu请求
        'v_rm': v_rm,                                                       # 每个vm的mem请求
        'population': range2rect(size, num_var,[0,0]),                            # size个chrom，每个chrom有num_var个双元素list[vm,hm]对应每个容器放置的vm编号和物理机编号
        'init_save': range2rect(size, num_var,[0,0]),                             # 保存初始size个chroms
        'v_p_cost': range2rect(size, num_var,0.0),                              # size个num_var长list记录每个vm上所有容器的cpu总请求,初始为0
        'v_m_cost': range2rect(size, num_var,0.0),                              # 每个vm被容器请求的mem，初始为0
        'h_p_cost': range2rect(size, num_var,0.0),                              # 每个HM被请求的cpu，初始为0
        'h_m_cost': range2rect(size, num_var,0.0),                              # HM被请求的mem，初始为0
        'power_cost': [x*0.0 for x in xrange(size)],                           # list(size),记录当前代population中，每个chrom的能耗代价
        'v_balance_cost': [x*0.0 for x in xrange(size)],          # ？？？？待讨论，衡量已经存在的vm放置容器后倒置的不均匀分布
        'h_balance_cost': [x*0.0 for x in xrange(size)],                         # list(size),每个chrom中对hm的资源负载均衡指数
        'migration_time': [x*0.0 for x in xrange(size)],                       # list(size),记录迁移时间，这里指定为固定值
        'rank': [x*0 for x in xrange(size)],                                 # list(size),记录每个chrom排名，rank值越大，排名越靠后
        'elite_power': 999999.0*num_var,                                    # float,记录每代种群中最优秀解的能耗代价值
        'elite_v_balance': 999999.0*num_var,                                  # float,记录每代种群中最优秀解的vm层负载均衡方差
        'elite_h_balance': 999999.0*num_var,                                  # float,记录每代种群中最优秀解的hm层负载均衡方差
        'elite_migration_time': time_base*num_var,                          # float,........的迁移时间
        'elite_chrom': range(num_var)                                       # list(num_var)，保存每代种群中精英chrom
    }
    #print population0['population']
    return population0


def initialize_population(popu1,size,num_var):
    '''
    初始化docker容器放置的vm编号，以及vm所能放置的hm编号，并计算初代种群的各项数值
    '''
    # 为所有容器选择能够容纳其尺寸的vm_id
    vm_used_id = [ [] for i in xrange(size) ]                                 # 记录每个chrom中，vm-hm的映射，保证映射在相同vm的不同容器，所在的hm也相同
    for i in xrange(size):
        for j in xrange(num_var):
            while(True):                                                      # 为第j个容器选择要能容纳其尺寸的vm编号
                tmp_v_id = random.randint(0,num_var-1)
                cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
                mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
                if (cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):
                    popu1['population'][i][j] = [tmp_v_id,0]                           # popu1['population'][i][j]是第i个chrom的第j个容器放置的[vm_id,hm_id]
                    popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                    popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v

                    # 找到容器-vm的拓扑后，继续寻找能够满足该vm尺寸的hm
                    flag = True
                    for x,y in vm_used_id[i]:
                        if (tmp_v_id == x):                                  # 对与已经安排过vm-hm映射位置的容器，直接进行对应vm,hm的赋值，并设while循环初始为False
                            popu1['population'][i][j]=[x,y]
                            flag = False
                    while(flag):
                        tmp_h_id = random.randint(0,num_var-1)               # 对未安排hm的容器所对应的vm，循环查找满足vm尺寸的hm
                        cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
                        mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
                        if (cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0):
                            popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
                            #print "population %s = %s" %(j,popu1['population'][i])
                            popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
                            popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
                            vm_used_id[i].append((tmp_v_id,tmp_h_id))
                            break
                    break
    #     print popu1['population'][i],'\n'      #为了测试赋值情况
    #     print popu1['v_p_cost'][i],'\n'
    #     print popu1['v_m_cost'][i],'\n'
    #     print popu1['h_p_cost'][i],'\n'
    #     print popu1['h_m_cost'][i],'\n'
    # print popu1['c_rp'],'\n'
    # print popu1['c_rm'],'\n'
    # print popu1['v_rp'],'\n'
    # print popu1['v_rm'],'\n'

    ## 保存初代种群
    for i in xrange(size):
        popu1['init_save'][i] = popu1['population'][i][:]
    if checkeffective(popu1,size,num_var):
        #print "it's effective, population = %s" %popu1['population']
        return popu1
    else:
        sys.exit("not effective in compute initialize_population")


def mbbode_migration(popu1,size,num_var,f,lambdaa):
    '''
    ！！！！！！！！迁移代码有错，出现 [[4, 13], [3, 13]， [8, 8],[13, 8], [5, 11]， [7, 11], [4, 7], [4, 13], [1, 9], [1, 0]],这种vm-hm的分布情况
    一旦被迁移概率选中：则进行2个层次的迁移——docker所在的vm编号迁移，vm所在的hm编号迁移(只有两层迁移，才可能调整vm-hm分布方式)
    '''
    for i in range(0,size):
        for j in xrange(0,num_var):
            rand_sum = random.random()
            lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
            if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
                index1 = random.randint(0, size-1)
                index2 = random.randint(0, size-1)
                while(index1 == index2):
                    index2 = random.randint(0, size-1)
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                tmp_v_id = abs(int(popu1['population'][i][j][0] + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] + 0.5)) % num_var)
                tmp_h_id = abs(int(popu1['population'][i][j][1] + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] + 0.5)) % num_var)
                while(True):
                    cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
                    mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
                    cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
                    mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
                    if(cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id] and cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0):                  # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
                        origin_v_id = popu1['population'][i][j][0]
                        origin_h_id = popu1['population'][i][j][1]
                        popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
                        popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                        popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
                        popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
                        popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
                        #
                        popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
                        popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
                        popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
                        popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
                        print "have migrate successfully!,i=%s,j=%s\n" %(i,j)
                        break
                    else:
                        tmp_v_id = (tmp_v_id + 1) % num_var
                        tmp_h_id = (tmp_h_id + 1) % num_var
    # 尽量清零
    for i in xrange(size):
        for j in xrange(num_var):
            if(popu1['v_p_cost'][i][j] < 0.0001):
                popu1['v_p_cost'][i][j] = 0
            elif(popu1['v_m_cost'][i][j] < 0.0001):
                popu1['v_m_cost'][i][j] = 0
            elif(popu1['h_p_cost'][i][j] < 0.0001):
                popu1['h_p_cost'][i][j] = 0
            elif(popu1['h_m_cost'][i][j] < 0.0001):
                popu1['h_m_cost'][i][j] = 0

    print popu1
    if checkeffective(popu1,size,num_var):
        #print "it's effective, population = %s" %popu1['population']
        return popu1
    else:
        sys.exit("not effective in compute mbbode_migration")


def mbbode_mutation(popu1,size,num_var,p_mutate):
    '''
    一旦被突变概率选中：则进行2个层次的突变——容器所在vm编号改变，vm所在的hm编号也在改变
    '''
    for i in xrange(size):
        for j in xrange(num_var):
            rand_sum = random.random()
            if (rand_sum < p_mutate):
                tmp_v_id = random.randint(0,num_var-1)
                tmp_h_id = random.randint(0,num_var-1)
                while(True):
                    cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
                    mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
                    cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
                    mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
                    if(cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id] and cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0):                  # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
                        origin_v_id = popu1['population'][i][j][0]
                        origin_h_id = popu1['population'][i][j][1]
                        popu1['population'][i][j] = [tmp_v_id,tmp_h_id]           # 更改容器对vm的资源占用
                        popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                        popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
                        popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
                        popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
                        popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h                # 更改vm对hm的资源使用
                        popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
                        popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
                        popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
                        print "have mutate successfully!\n"
                        break
                    else:
                        tmp_v_id = (tmp_v_id + 1) % num_var
                        tmp_h_id = (tmp_h_id + 1) % num_var
    # 尽量清零
    for i in xrange(size):
        for j in xrange(num_var):
            if(popu1['v_p_cost'][i][j] < 0.0001):
                popu1['v_p_cost'][i][j] = 0
            elif(popu1['v_m_cost'][i][j] < 0.0001):
                popu1['v_m_cost'][i][j] = 0
            elif(popu1['h_p_cost'][i][j] < 0.0001):
                popu1['h_p_cost'][i][j] = 0
            elif(popu1['h_m_cost'][i][j] < 0.0001):
                popu1['h_m_cost'][i][j] = 0

    print popu1
    if checkeffective(popu1,size,num_var):
        #print "population = %s" %popu1['population']
        return popu1
    else:
        sys.exit("not effective in compute mbbode_mutation")


def mbbode_cost(popu1,size, num_var,time_base):
    '''
    能耗代价：应该以vm的cpu使用率进行计算，能够直接反映所有容器占用的hm资源的多少
    负载均衡指数方差：应该分别计算vm直接放置在hm产生的负载均衡方差 和 由容器放置于vm产生的vm的负载均衡方差
    迁移代价：由于容器是无状态的且共享存储挂载volume的，所以不需要考虑容器的迁移，但是必须考虑vm的迁移
    '''
    # 计算能耗 —— 能耗计算，仅以hm实际被vm占用的cpu作为唯一参数进行计算
    for i in xrange(size):
        for j in xrange(num_var):
            x = popu1['h_p_cost'][i][j]
            if (x > 0.0):
                popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)

    # 计算负载均衡指数
    # 同时计算容器在vm上放置产生的负载均衡情况，以各vm的被容器请求的实际资源v_p_cost,v_m_cost为依据; 和vm在hm上产生的负载均衡情况，以h_p_cost,h_m_cost为计算依据
    for i in xrange(size):
        v_load_index = range(num_var)        # vm的负载均衡指数列表，每个chrom共num_var个（以容器实际使用vm的资源计算）
        v_average_load_index = 0.0
        h_load_index = range(num_var)        # hm的负载均衡指数列表，每个chrom共num_var个（以vm实际使用hm的资源计算）
        h_average_load_index = 0.0
        for j in xrange(num_var):         # vm的标号/hm的编号
            v_load_index[j] = 1.0 / (1.0005 - popu1['v_p_cost'][i][j]) / (1.0005 - popu1['v_m_cost'][i][j])
            v_average_load_index += v_load_index[j]
            h_load_index[j] = 1.0 / (1.0005 - popu1['h_p_cost'][i][j]) / (1.0005 - popu1['h_m_cost'][i][j])
            h_average_load_index += h_load_index[j]
        v_average_load_index /= num_var
        h_average_load_index /= num_var
        for j in xrange(num_var):        # 同时计算vm层、hm层的load-index方差，反映整体的分布情况
            popu1['v_balance_cost'][i] = popu1['v_balance_cost'][i] + (v_load_index[j] - v_average_load_index)*(v_load_index[j] - v_average_load_index)
            popu1['h_balance_cost'][i] = popu1['h_balance_cost'][i] + (h_load_index[j] - h_average_load_index)*(h_load_index[j] - h_average_load_index)
        popu1['v_balance_cost'][i] = math.sqrt(popu1['v_balance_cost'][i] / num_var)
        popu1['h_balance_cost'][i] = math.sqrt(popu1['h_balance_cost'][i] / num_var)

    #  计算迁移时间 —— 由于容器是无状态迁移，所以不需要考虑容器的迁移时间，仅考虑虚拟机的迁移
    for i in xrange(size):
        a = {}                           # 进化后的(vm,hm)字典
        b = {}                           # 初始的(vm,hm)字典
        for j in xrange(num_var):                      # vm标号
            a[popu1['population'][i][j][0]] = popu1['population'][i][j][1]
            b[popu1['init_save'][i][j][0]] = popu1['init_save'][i][j][1]
        for x,y in a.items():
            if x in b and y != b[x]:            # 若x不在b,说明是进化后新建的;若a中没有的vm，有可能b有，那就是进化后删除了，或者b也没有;均不需要考虑迁移时间
                popu1['migration_time'][i] += time_base

        # # # 剔除无效迁移  —— 在vm限定若干种尺寸规格的情况下，剔除无效迁移很必要——还没写完
        # for x,y in a.items():
        #     for l,m in b.items():
        #         if popu1['v_rp'][x] == popu1['v_rp'][l] and popu1['v_rm'][x] == popu1['v_rm'][l] and y == m:   # 两个vm尺寸相同，并且A的新hm是B的源hm,则B不动，A直接迁入B的新hm中
        #             a[x] = a[l]
        #             a[l] = m        # a[l] = (b[l] == m)                         # 如此更改不会影响到能耗，两层负载等的计算，只是减免1次迁移时间
        #             popu1['migration_time'][i] -= time_base
        #             print x,y,l,m,a,b
        #             print "find an invalid migration\n"
    # if checkeffective(popu1,size,num_var):
    #     return popu1
    # else:
    #     sys.exit("not effective in compute mbbode_cost")
    return popu1

def mbbode_rank(popu1,size, num_var):
    '''
    4个目标同时进行比较，（可以为每个目标设置权重表示该目标的重要性）
    '''
    # 非支配解排名在size个解之间
    for i in xrange(size):
        for j in xrange(i+1,size):
            if (popu1['power_cost'][i] <= popu1['power_cost'][j]):
                popu1['rank'][j] += 1
            elif (popu1['power_cost'][i] > popu1['power_cost'][j]):
                popu1['rank'][i] += 1
            if(popu1['v_balance_cost'][i] <= popu1['v_balance_cost'][j]):
                popu1['rank'][j] += 1
            elif(popu1['v_balance_cost'][i] > popu1['v_balance_cost'][j]):
                popu1['rank'][i] += 1
            if(popu1['h_balance_cost'][i] <= popu1['h_balance_cost'][j]):
                popu1['rank'][j] += 1
            elif(popu1['h_balance_cost'][i] > popu1['h_balance_cost'][j]):
                popu1['rank'][i] += 1
            if(popu1['migration_time'][i] <= popu1['migration_time'][j]):
                popu1['rank'][j] += 1
            elif(popu1['migration_time'][i] > popu1['migration_time'][j]):
                popu1['rank'][i] += 1

    # 寻找当前经过迁移突变后种群的排名rank最小值
    rank = popu1['rank'].index(min(popu1['rank']))
    if (popu1['elite_power'] > popu1['power_cost'][rank] and popu1['elite_v_balance'] > popu1['v_balance_cost'][rank] and popu1['elite_h_balance'] > popu1['h_balance_cost'][rank]):
        popu1['elite_power'] = popu1['power_cost'][rank]                        # 若当代rank最小的解优于上代保存的精英解，则替换精英解
        popu1['elite_v_balance'] = popu1['v_balance_cost'][rank]
        popu1['elite_h_balance'] = popu1['h_balance_cost'][rank]
        popu1['elite_migration_time'] = popu1['migration_time'][rank]
        popu1['elite_chrom'] = popu1['population'][rank][:]
    else:                                                                       # 若精英解仍旧最优，则用上代精英解随机替换当代的size=0 的候选解
        popu1['population'][0] = popu1['elite_chrom'][:]
    return popu1

def main(generation,size,num_var,p):
    '''
    主程序流程：初代解-代价计算-排名-迁移-突变-代价计算-排名-精英解替换-继续迭代
    主要算法参数：
    generation，    种群迭代次数
    size，          population中chrom个数
    num_var，       每个chrom中SIV个数
    p，             VM对CPU,MEM两种资源请求的相关系数
    '''
    # 1.算法主要参数设置
    p_mutate = 0.02                        # 高斯突变率（这里直接给出值没有进行计算）0.01
    f = 0.6                                # 差分因子
    rp_u = 0.25                            # 容器请求CPU的指导变量
    rm_u = 0.25                            # 容器请求MEM的指导变量
    p = p                                  # 控制容器cpu,mem的资源相关度
    time_base = 65                         # 单台vm迁移的基准时间（实际上不对，因为vm的mem尺寸不一样，基数也应该不一样）
    rp_option = [1.0]                         # vm可选的cpu尺寸
    rm_option = [1.0]                         # vm可选的mem尺寸

    # 2.初始化num_var个容器和vm，以及计算迁移率
    c_rp,c_rm = initDocker(rp_u,rm_u,p,num_var)
    v_rp,v_rm = initVM(c_rp,c_rm,rp_option,rm_option,num_var)
    lambdaa,mu = migrateRate(size)

    ## 以下程序的流程按照先按照串行结构书写
    # 3. 初代种群的生成、代价计算及排序
    init_popu = make_population(size, num_var,c_rp,c_rm,v_rp,v_rm,time_base)
    init_popu = initialize_population(init_popu,size, num_var)
    print init_popu
    init_popu = mbbode_cost(init_popu,size, num_var,time_base)
    init_popu = mbbode_rank(init_popu,size, num_var)
    #print init_popu,'\n'
    init_popu = mbbode_migration(init_popu,size,num_var,f,lambdaa)
    init_popu = mbbode_mutation(init_popu,size,num_var,p_mutate)
    init_popu = mbbode_cost(init_popu,size, num_var,time_base)
    init_popu = mbbode_rank(init_popu,size, num_var)
    #print init_popu,'\n'

    # # 随机保存一个初代候选解
    # tmp = random.randint(0,size-1)                                 # 从每个群岛的population中size个随机选出第tmp各解
    # save_chrom = init_popu['population'][tmp]                      # 随机挑选的第tmp个初始候选解，代表MBBO执行前vm-hm拓扑关系
    # save_cost = (init_popu['power_cost'][tmp],init_popu['v_balance_cost'][tmp],init_popu['h_balance_cost'][tmp],init_popu['migration_time'][tmp])                                               # 第tmp个初始候选解的3个HSI代价值
    #
    # elite_cost = [9999.9*num_var, 9999.9*num_var,9999.9*num_var, time_base*num_var]   # 初设的全局精英解能耗代价、负载均衡方差、迁移时间
    # save_elite_cost = [0,0,0,0]                                          # 用于保存每一代的全局最优解，并在新的一代时比较有否变化，只有改变后才会打印，否则不打印
    # time1 = time.time()                                                # 算法迭代进化开始时间戳
    # ## 开始种群迭代进化
    # for g in range(generation):                                        # 设置最大迭代次数
    #     init_popu = mbbode_migration(init_popu,size,num_var,f,lambdaa)
    #     init_popu = mbbode_mutation(init_popu,size,num_var,p_mutate)
    #     init_popu = mbbode_cost(init_popu,size, num_var,time_base)
    #     init_popu = mbbode_rank(init_popu,size, num_var)
    #
    #     ## 获取全局最优解的能耗代价、负载均衡指数、以及迁移时间
    #     if(elite_cost[0] > init_popu['elite_power'] and elite_cost[1] > init_popu['elite_v_balance'] and elite_cost[2] > init_popu['elite_h_balance']):
    #         elite_cost[0] = init_popu['elite_power']
    #         elite_cost[1] = init_popu['elite_v_balance']
    #         elite_cost[2] = init_popu['elite_h_balance']
    #         elite_cost[3] = init_popu['elite_migration_time']
    #
    #     # 记录每次迭代 改变的 全局最优解值
    #     if (save_elite_cost[0] != elite_cost[0] or save_elite_cost[1] != elite_cost[1] or save_elite_cost[2] != elite_cost[2] or save_elite_cost[3] != elite_cost[3]):
    #         print elite_cost[0], elite_cost[1], elite_cost[2],elite_cost[3]
    #         save_elite_cost = elite_cost[:]
    # time2 = time.time()
    # print 'Time cost: ', (time2 - time1), '\n'
    # print 'the init chrom maybe is %s, use %s pms, the cost is %s' %(save_chrom,len(set(save_chrom[j][1] for j in xrange(num_var))),save_cost)
    # print 'after mbbo, chrom maybe is %s, use %s pms' %(init_popu['elite_chrom'],len(set(init_popu['elite_chrom'][j][1] for j in xrange(num_var))))

if __name__ == "__main__":
    main(1,3,15,1.0)
