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
        if((r < p and rp[i] >= rp_u) or (r >= p and rp[i] < rp_u)):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            c_rm[i] += rm_u
        if(c_rm[i] >= 1.0):                                               # 控制mem请求量合理性
            c_rm[i] -= 1.0
    return c_rp,c_rm

def initVM(c_rp,c_rm,rp_u,rm_u,num_var):
    '''
    持续查找可以容纳所有容器的vm：
    传入cpu参考列表rp_u,和mem可选列表rm_u
    c_rp,c_rm为已知的num_var个docker容器的尺寸
    num_var是容器个数，初始假设vm个数等于docker个数
    返回：虚拟机的num_var个尺寸元组序列
    '''
    v_rp = []
    v_rm = []
    i = 0
    while (True):
        if len(v_rp) == 200 and len(v_rm) == 200:
            return v_rp,v_rm
        rp = random.choice(rp_u)
        rm = random.choice(rm_u)
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


def checkeffective(pass):
    pass

def range2rect(pass):
    pass

def make_population(size, num_var,c_rp,c_rm,v_rp,v_rm): #    作为全局变量，按照需要传入各方法中 f, p_mutate, time_base, lambdaa):
    '''
    构造一个population，包含size个候选解chrom,每个chrom是num_var个分别记录该容器所在的vm和hm编号的元组
    '''
    population = {
        #'size': size,                                                       # int,population中chrom的个数
        #'num_var': num_var,                                                 # int,chrom元素个数，即vm个数（同时假设HM个数也是num_var）
        'c_rp': c_rp,                                                       # 每个容器的cpu请求
        'c_rm': c_rm,                                                       # 每个容器的mem请求
        'v_rp': v_rp,                                                       # 每个vm的cpu请求
        'v_rm': v_rm,                                                       # 每个vm的mem请求
        #'f': f,                                                             # float，差分因子，系统运行前必须指定
        #'p_mutate': p_mutate,                                               # float,突变概率
        #'time_base': time_base,                                             # float,时间基数
        #'lambdaa': tuple(lambdaa),                                          # tuple(size),所有chrom候选解的迁入率，rank值越小，越优秀，迁入率越小
        'population': range2rect(size, num_var),                            # size x num_var的矩阵，每代population的size个解集合
        'init_save': range2rect(size, num_var),                             # 保存初始population的所有chroms
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

def initialize_population(pass):
    pass

def mbbode_migration(pass,f, lambdaa):
    pass

def mbbode_mutation(pass,p_mutate):
    pass

def mbbode_cost(pass,time_base):
    pass

def mbbode_rank(pass):
    pass





















def main(generation,size,num_var,p):
    '''
    控制整个迭代循环流程
    以及参数generation,size,num_var,p 传入
    '''
    # p_mutate = 0.02                        # 高斯突变率（这里直接给出值没有进行计算）0.01
    # f = 0.6                                # 差分因子
    # rp_u = 0.25                            # VM请求CPU的指导变量
    # rm_u = 0.25                            # VM请求MEM的指导变量
    # p = 1.0
    f = 0.6
    p_mutate = 0.02
    time_base = 65                                    # 要不要考虑vm的迁移  (作为单台虚拟机迁移的基准时间)
    c_rp,c_rm = initDocker(rp_u,rm_u,p,num_var)       # 初始化docker容器尺寸
    v_rp,v_rm = initVM(c_rp,c_rm,rp_u,rm_u,num_var)   # 初始化可容纳所有docker容器的vm尺寸
    lambdaa,mu = migrateRate(size)                    # 初始化size个候选解的迁移率

    # 初代种群的生成、代价计算及排序
    init_popu = make_population(pass)
    init_popu = init_population(pass)
    init_popu = mbbode_cost(pass)
    init_popu = mbbode_rank(pass)

    elite_cost = [9999.9*num_var, 9999.9*num_var, time_base*num_var]   # 初设的全局精英解能耗代价、负载均衡指数、迁移时间
    time1 = time.time()                                                # 算法迭代进化开始时间戳


    # 开始种群迭代进化
    for g in range(generation):                                        # 设置最大迭代次数
        init_popu = mbbode_migration(pass)
        init_popu = mbbode_mutation(pass)
        init_popu = mbbode_cost(pass)
        init_popu = mbbode_rank(pass)


        tmp = random.randint(0,size-1)                                 # 从每个群岛的population中size个随机选出第tmp各解
        save_chrom = pass                                              # 随机挑选的第tmp个初始候选解，代表MBBO执行前vm-hm拓扑关系
        save_cost = pass                                               # 第tmp个初始候选解的3个HSI代价值


        # 获取全局最优解的能耗代价、负载均衡指数、以及迁移时间
        if(elite_cost[0] > init_popu['elite_power'] and elite_cost[1] > init_popu['elite_balance']):
            pass
            # elite_cost[0] = init_popu['elite_power']
            # elite_cost[1] = init_popu['elite_balance']
            # elite_cost[2] = init_popu['elite_migration_time']

        # 记录每次迭代 改变的 全局最优解值
        if (save_elite_cost[0] != elite_cost[0] or save_elite_cost[1] != elite_cost[1] or save_elite_cost[2] != elite_cost[2]):
            pass
            print elite_cost[0], elite_cost[1], elite_cost[2]
            # save_elite_cost = elite_cost[:]
            # HSI_values.append(save_elite_cost)
            # HSI_ts.append(time.time() - time1)

    print 'Time cost: ', (time2 - time1), '\n'
