#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on: 2017-4-12
Change on: 2017-12-1
@author: Amy
Goal: 这个mbbo算法是针对vm-hm架构的，单纯以VM为粒度的聚合算法
      为了说明在d-v-h架构下，单纯考虑docker作为聚合单位 or vm单纯作为聚合单位
      其聚合效果均不如同时以容器、vm作为聚合单位的效果好，因此实验设计:
      1. 在d-v-h架构下，仅用FFDSum对docker层进行聚合 VS 使用FFDSum同时聚合docker层和VM层；
      2. 在d-v-h下，仅用mbbo对vm层进行聚合 VS 使用mbbo同时对docker、vm层随机求解聚合；
      3. 在d-v-h下，比对同时以docker、vm作为调度单位时的FFDSum、Mbbo、GA算法等的聚合效果；
2017-12-1 新思考——对于负载均衡问题的理解：
      1. 数据中心长时间服务后，必然存在部分服务器承载少量VM，部分HM的cpu、mem几乎超过100%的负载不均情况，
         这种情况包括整个集群各个hm间cpu利用不均衡、mem利用不均衡、以及hm内部cpu、mem之间不均衡；
      2. 根据WoodT的多维资源归一化处理，引入load index，对于load index值越大那么该hm承载新的vm可能性越低，
         而load index越小该hm承载新的vm的可能性越大；
         引入集群的负载方差，方差越大说明hms之间负载差异性越高（能够承载新VM可能性差异大），负载越不均衡。
      3. 因此在对比算法性能代价时，应该综合考虑集群load index average和方差，方差越大说明集群负载更不均衡，
         但是若方差差异不大，那么load index average越小的集群承载更多VM的可能性越大。
说明： 在构造的表示集群状态数据结构中，v_rp,v_rm list代表num_var个不同编号下标的VM demands资源大小，
      对于running VMs均有大于0.0的资源请求，仅down Vms资源均为0.0;
      而population记录的是所有num_var的v-h或d-(v,h)映射，这并不说明所有的VM均都处于running态，
      因此可以通过v_rp/rm均为0.0或者v_p/m_cost均为0.0来得知VM是否running,
      这会直接影响到代价计算的均值分母。

2017-12-22 更新： vm_mbbo思想就是通过拿到集群所有active状态的HMs（最大可用hm下标代表了），
                 获取各实际激活态vm尺寸，随机生成v-h的合理映射，通过代价函数引导求解方向。
    !!! 在与加入docker聚合的聚合算法对比时，需要从集群中提炼出当前处于激活态的虚拟机的rp,rm以及这些虚拟机上实际由容器引起的负载v_p_cost、v_m_cost。
    
'''
import time
import random
import math
import json
import sys
import copy
import collections
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

def compute_true_cost(chrom, rp, rm, v_p_cost, v_m_cost, size=1):
    '''
    对传入的chrom,统计实际running vms占用的hms数量，因为在做对比实验时，为了方便对所有的VMs设置了尺寸，
    并参与了放置population，不过仅有running Vms有实际的cpu、mem占用，其他非running Vms均为0.0；
    返回running vms-running hms的字典映射
    '''
    cost = {
        'power_cost': 0.0,
        'v_balance_cost': 0.0,
        'v_average_load_index': 0.0,
        'h_balance_cost': 0.0,
        'h_average_load_index': 0.0,
        'degree_of_concentration':0.0,
        'tolerance': 0.0,
        'used_hms': 0
        }
    # 统计map_v_p
    map_v_p = {}
    for v in xrange(len(chrom)):
        if rp[v] != 0.0 or rm[v] != 0.0:
            h = chrom[v]
            map_v_p[v] = h
    # 根据map_v_p统计map_h_v
    map_h_v = collections.defaultdict(list)
    for key, value in map_v_p.items():
        map_h_v[value].append(key)
    
    # 统计使用的vms 与 hms
    used_vms = map_v_p.keys()
    used_hms = list(set(map_v_p.values()))
    tmp0, tmp1 = len(used_vms), len(used_hms)
    cost['used_hms'] = tmp1
    
    h_load_index = []      # 各HM的负载均衡指数
    v_load_index = []      # 各VM的负载均衡指数
    utilization = 0
    # 计算总能耗及各running VM/HM负载均衡指数
    while tmp0 > 0 or tmp1 > 0:
        if tmp0 > 0:
            v = used_vms[tmp0 - 1]
            # 用VM配置尺寸与容器实际占用进行计算
            index = 1.0 / (1.0005 - v_p_cost[v]) / (1.0005 - v_m_cost[v])
            v_load_index.append(index)
            tmp0 -= 1
        if tmp1 > 0:
            h = used_hms[tmp1 - 1]
            # 以docker为实际负载进行代价计算
            true_load_cpu = sum([v_p_cost[v] for v in map_h_v[h]])
            true_load_mem = sum([v_m_cost[v] for v in map_h_v[h]])
            # 计算集群剩余资源量即各HM节点cpu、mem余量之乘积，所有active HM求和
            utilization += (1.0 - true_load_cpu) * (1.0 - true_load_mem)
            # 能耗计算依据之前模拟的立方多项式模型
            cost['power_cost'] += 446.7 + 5.28*true_load_cpu - 0.04747*true_load_cpu**2 + 0.000334*true_load_cpu**3
            index = 1.0 / (1.0005 - true_load_cpu) / (1.0005 - true_load_mem)
            h_load_index.append(index)
            tmp1 -= 1

    cost['degree_of_concentration'] = 100 * cost['used_hms'] - 13 * utilization
    
    # 计算所有running VMs/HMs间的负载方差
    tmp0, tmp1 = len(used_vms), len(used_hms)
    v_average_load_index = sum(v_load_index) / tmp0
    h_average_load_index = sum(h_load_index) / tmp1
    cost['v_average_load_index'] = v_average_load_index
    cost['h_average_load_index'] = h_average_load_index
    while tmp0 > 0 or tmp1 > 0:
        if tmp0 > 0:
            cost['v_balance_cost'] += (v_load_index[tmp0 - 1] - v_average_load_index)**2
            tmp0 -= 1
        if tmp1 > 0:
            cost['h_balance_cost'] += (h_load_index[tmp1 - 1] - h_average_load_index)**2
            tmp1 -= 1

    # 计算负载平均差（方差算数平方跟）
    cost['v_balance_cost'] = math.sqrt(cost['v_balance_cost'] / len(used_vms))
    cost['h_balance_cost'] = math.sqrt(cost['h_balance_cost'] / len(used_hms))
    # 计算VM迁移时间（仅聚合阶段）
    pass
    return cost

def range2rect(size, num_var):
    '''
    构造size x num_var 的矩阵
    '''
    res = range(size)
    for i in xrange(size):
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
        'p_mutate': p_mutate,                                               # float,突变概率
        'f': f,                                                             # float，差分因子，系统运行前必须指定
        'time_base': time_base,                                             # float,时间基数
        'lambdaa': tuple(lambdaa),                                          # tuple(size),所有chrom候选解的迁入率，rank值越小，越优秀，迁入率越小
        'rp': rp,                                                           # list(num_var),所有vm的cpu demand
        'rm': rm,                                                           # list(num_var),所有vm的mem demand
        'population': range2rect(size, num_var),                            # size x num_var的矩阵，每代population的size个解集合
        'population0': range2rect(size, num_var),                           # 保存初始population的所有chroms
        'p_cost': range2rect(size, num_var),                                # size x num_var的矩阵，记录每个HM被请求的CPU总量
        'm_cost': range2rect(size, num_var),                                # size x num_var的矩阵，记录每个HM被请求的MEM总量
        'power_cost': [x*0 for x in range(size)],                           # list(size),记录当前代population中，每个chrom的能耗代价
        'concentration_cost': [x*0 for x in range(size)],
        'h_balance_cost': [x*0 for x in range(size)],                       # list(size),记录当前population中,每个chrom的负载均衡指数
        'migration_time_cost': [x*0+time_base*num_var for x in range(size)],     # list(size),记录迁移时间，这里指定为固定值
        'rank': [x*0 for x in range(size)],                                 # list(size),记录每个chrom排名，rank值越大，排名越靠后
        'elite_power': 999999.0*num_var,                                    # float,记录每代种群中最优秀解的能耗代价值
        'elite_concentration': 999999.0*num_var,
        'elite_h_balance': 999999.0*num_var,                                # float,记录每代种群中最优秀解的负载均衡指数
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
                if tmp_p_cost <= 1.0 and tmp_m_cost <= 1.0:
                    popu1['population'][i][j] = tmp_position
                    popu1['p_cost'][i][tmp_position] = tmp_p_cost                    # 满足约束条件即可放入，即一个合理的候选解
                    popu1['m_cost'][i][tmp_position] = tmp_m_cost
                    break
    for i in range(popu1['size']):
        popu1['population0'][i] = copy.deepcopy(popu1['population'][i])
        # popu1['population0'][i] = tuple(popu1['population'][i])                      # 对初始化后的种群进行保存
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
                    # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
                    if tmp_p_cost <= 1.0 and tmp_m_cost <= 1.0:
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
            if popu1['p_cost'][i][j] <= 0.000001:
                popu1['p_cost'][i][j] = 0
            if popu1['m_cost'][i][j] <= 0.000001:
                popu1['m_cost'][i][j] = 0
    # 在单纯v-h架构下，聚合VM时每次进行迁移、突变等都会去判断新解的有效性；
    # 实际上应该在每一次迭代（迁移、突变等操作完全完成的情况下）完成之后，再对所有无效解统一进行有效化，这样才符合mbbo的最初设想
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
            # chromi的第j元素(vmj) 被突变率选中,随机生成新的SIV值，进行替换
            if rand_num < popu1['p_mutate']:
                tmp_position = random.randint(0, popu1['num_var'] - 1)
                while True:
                    tmp_p_cost = popu1['p_cost'][i][tmp_position] + popu1['rp'][j]
                    tmp_m_cost = popu1['m_cost'][i][tmp_position] + popu1['rm'][j]
                    if tmp_p_cost <= 1.0 and tmp_m_cost <= 1.0:
                        original_position = popu1['population'][i][j]
                        popu1['population'][i][j] = tmp_position
                        popu1['p_cost'][i][tmp_position] = tmp_p_cost
                        popu1['m_cost'][i][tmp_position] = tmp_m_cost
                        popu1['p_cost'][i][original_position] -= popu1['rp'][j]
                        popu1['m_cost'][i][original_position] -= popu1['rm'][j]
                        break
                    else:
                        tmp_position = (tmp_position + 1) % popu1['num_var']
    # 在单纯v-h架构下，聚合VM时每次进行迁移、突变等都会去判断新解的有效性；
    # 实际上应该在每一次迭代（迁移、突变等操作完全完成的情况下）完成之后，再对所有无效解统一进行有效化，这样才符合mbbo的最初设想
    if checkeffective(popu1):
        return popu1
    else:
        print "not effective in compute mbbode_mutation"
        sys.exit()

def true_hm_cost(popu1, v_p_cost, v_m_cost):
    '''
    通过size个population与实际v_
    '''

def mbbode_cost(popu1):
    '''
        2017-12-22 更新： 代价计算应以HM上所有实际docker作为负载，即所有v_p_cost之和
        compute the costs of three objectives in MBBO/DE algorithm
       更新： 由于集群中h_p/m_cost为0.0的代表down状态HMs，不应被算入各项指标中，故更新计算方式
    '''
    # compute the power (down HMs的h_p/m_cost为0.0故不影响能耗计算）
    for i in xrange(popu1['size']):
        count = 0
        popu1['power_cost'][i] = 0.0
        popu1['concentration_cost'][i] = 0.0
        utilization = 0          # 用于统计资源碎片化
        for j in range(popu1['num_var']):
            x, y = popu1['p_cost'][i][j], popu1['m_cost'][i][j]
            if x != 0.0 or y != 0.0:
                utilization += (1.0 - x) * (1.0 - y)
                popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)             # 计算size个chrom的能耗值  能耗与cpu使用率紧密关系
                count += 1
        popu1['concentration_cost'][i] = 100 * count - 13 * utilization              # 各chrom的负载均衡代价值


    # compute the h_balance cost of popu1(仅针对非down 状态HMs进行计算)
    for i in xrange(popu1['size']):
        count = 0
        popu1['h_balance_cost'][i] = 0.0
        load_index = []
        for j in xrange(popu1['num_var']):
            if popu1['p_cost'][i][j] != 0.0 or popu1['m_cost'][i][j] != 0.0:
                count += 1
                index = 1.0 / (1.0005 - popu1['p_cost'][i][j]) / (1.0005 - popu1['m_cost'][i][j])
                load_index.append(index)
        average_load_index = sum(load_index) / count
        for load in load_index:
            popu1['h_balance_cost'][i] += (load - average_load_index)**2
        popu1['h_balance_cost'][i] = math.sqrt(popu1['h_balance_cost'][i] / count)

    # # compute the migration_time_cost of popu1 without getting rid of invalid migration
    # for i in range(popu1['size']):
    #     popu1['migration_time_cost'][i] = 0
    #     for j in range(popu1['num_var']):
    #         if(popu1['population'][i][j] != popu1['population0'][i][j]):
    #             popu1['migration_time_cost'][i] += popu1['time_base']

    # compute the migration_time_cost of popu1 with getting rid of invalid migration
    for i in xrange(popu1['size']):
        popu1['migration_time_cost'][i] = 0
        for j in xrange(popu1['num_var']):
            vm0 = popu1['population0'][i][j]
            vm = popu1['population'][i][j]
            if popu1['rp'][vm] == 0.0 and popu1['rm'][vm] == 0.0:
                continue
            else:
                if vm != vm0:
                    popu1['migration_time_cost'][i] += popu1['time_base']                                 # 改变源，目标hm的vm需要迁移
                    # 剔除无效迁移
                    for x in xrange(j+1, popu1['num_var']):
                        if popu1['rp'][j] == popu1['rp'][x] and popu1['rm'][j] == popu1['rm'][x]:  # 若有2个虚拟机尺寸cpu,mem一样
                            if popu1['population0'][i][j] == popu1['population'][i][x]:            # vm_x将迁入的目标hm是vm_j的源hm,则直接将vm_x的目标hm改为vm_j的目标hm，vm_j不用进行迁移
                                popu1['population'][i][x] = popu1['population'][i][j]
                                popu1['population'][i][j] = popu1['population0'][i][j]
                                popu1['migration_time_cost'][i] -= popu1['time_base']                     # 节省1次迁移用时
                            elif popu1['population0'][i][x] == popu1['population'][i][j]:          # vm_j将迁入的目标hm是vm_x的源hm,则直接将vm_j的目标hm改为vm_x的目标hm，vm_x不用进行迁移
                                popu1['population'][i][j] = popu1['population'][i][x]
                                popu1['population'][i][x] = popu1['population0'][i][x]
                                popu1['migration_time_cost'][i] -= popu1['time_base']                     # 节省1次迁移用时

    # 既然进行迁移时间的计算，就不应该再判断解的有效性
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
    # 此处仅针对聚合优化目标进行
    for i in xrange(popu1['size']):
        for j in xrange(i+1, popu1['size']):
            if popu1['power_cost'][i] <= popu1['power_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['power_cost'][i] > popu1['power_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['concentration_cost'][i] <= popu1['concentration_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['concentration_cost'][i] > popu1['concentration_cost'][j]:
                popu1['rank'][i] += 1


    # 以下是针对所有优化目标的
    # for i in range(popu1['size']):
    #     for j in range(i+1, popu1['size']):                                                            # 按照非支配解排序non-dominated sorting
    #         if popu1['power_cost'][i] < popu1['power_cost'][j]:
    #             popu1['rank'][j] += 1
    #         elif popu1['power_cost'][i] > popu1['power_cost'][j]:
    #             popu1['rank'][i] += 1
    #         if popu1['h_balance_cost'][i] < popu1['h_balance_cost'][j]:
    #             popu1['rank'][j] += 1
    #         elif popu1['h_balance_cost'][i] > popu1['h_balance_cost'][j]:
    #             popu1['rank'][i] += 1
    #         if popu1['migration_time_cost'][i] < popu1['migration_time_cost'][j]:
    #             popu1['rank'][j] += 1
    #         elif popu1['migration_time_cost'][i] > popu1['migration_time_cost'][j]:
    #             popu1['rank'][i] += 1

    # 寻找当前经过迁移突变后种群的排名rank最小值对应的解下标
    rank = popu1['rank'].index(min(popu1['rank']))
    # 写一个总的方法，由外部传入函数需要对比的代价目标，统一进行精英解判断，根据情况进行精英解替换
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
        popu1['elite_concentration'] = popu1['concentration_cost'][rank]
        popu1['elite_h_balance'] = popu1['h_balance_cost'][rank]
        popu1['elite_migration_time'] = popu1['migration_time_cost'][rank]
        popu1['elite_chrom'] = popu1['population'][rank][:]
    else:
        popu1['population'][0] = copy.deepcopy(popu1['elite_chrom'])
    return popu1

def mbbode_get_best_chr(popu1, popu2):
    '''get the best chrom from RDD'''
    if popu1.power_cost < popu2.power_cost and popu1.h_balance_cost < popu2.h_balance_cost:
        return popu1
    return popu2

def get_best_cost(popu1, popu2):
    '''get the best cost from best_chrom'''
    best_cost = [0.0, 0.0, 0.0]
    if popu1['elite_power'] > popu2['elite_power'] and popu1['elite_h_balance'] > popu2['elite_h_balance']:
        best_cost[0] = popu2['elite_power']
        best_cost[1] = popu2['elite_h_balance']
        best_cost[2] = popu2['elite_migration_time']
    else:
        best_cost[0] = popu1['elite_power']
        best_cost[1] = popu1['elite_h_balance']
        best_cost[2] = popu1['elite_migration_time']
    return best_cost

def createVMResrcs(rp_u, rm_u, p, num_var):
    '''
    目标：Gao Y提出的基于相关系数生成测试数据集的方式来生成VM
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
    lambdaa = range(size)                                       # 每个解对应一对迁入lambdaa迁出率mu,共有size个解
    mu = range(size)
    for i in range(size):
        lambdaa[i] = math.cos(float(size - (i + 1)) / size)     # 按照种群所有候选解排名后的顺序，依次求解余弦迁入率，rank值越小迁入率越小
        mu[i] = math.sin(float(size - (i + 1)) / size)          # 迁出率
    return lambdaa, mu

def main(generation, size, num_var, p, hsi_list, rp, rm, v_p_cost, v_m_cost):
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
    p = p                                  # 生成VM的指导变量
    time_base = 65                         # 作为单台虚拟机迁移的基准时间

    # compute each chrom immgrate rate and emgrate rate of all sorted chroms
    lambdaa, mu = migrateRate(size)
    # random create num_var vms with cpu,mem requirements
    #rp, rm = createVMResrcs(rp_u, rm_u, p, num_var)
    
    # 为了与cmbbo做对比，这里采用cmbbo随机生成的方式进行赋值  


    # 与FFDSum使用d-v-h架构聚合时的各个vm尺寸
    # （尺寸为0.0表示在初始的集群结构中并没被使用，所以即使在mbbo中被安排population，却不会引起多余能耗，并且v_balance_cost与初始集群中一样）
    rp = rp
    rm = rm
    v_p_cost = v_p_cost
    v_m_cost = v_m_cost

    # 初始populations
    init_population = make_population(size, num_var, rp, rm, f, p_mutate, time_base, lambdaa)
    init_population = initialize_population(init_population)
    init_population = mbbode_cost(init_population)
    init_population = mbbode_rank(init_population, hsi_list)

    ## 记录随机一个初始种群的chrom和代价
    tmp = random.randint(0, size-1)
    save_chrom = copy.deepcopy(init_population['population'][tmp])
    save_cost = {
        'power_cost':init_population['power_cost'][tmp],
        'concentration_cost':init_population['concentration_cost'][tmp],
        'migration_time_cost': init_population['migration_time_cost'][tmp]
        }

    # 初设的全局精英解能耗代价、负载均衡指数、迁移时间
    elite_cost = {
        'power': 9999.9*num_var,
        'concentration': 9999.9*num_var,
        'migration_time': time_base*num_var
        }

    # 保存每一次迭代后的全局最优解，与全局最优解每次迭代后对比，当2者值不同则打印，并被赋为最新全局最优解
    save_elite_cost = {'power': 0, 'concentration': 0, 'migration_time': 0}
    time0 = time.time()

    # 设置最大迭代次数
    for g in range(generation):

        init_population = mbbode_migration(init_population)
        init_population = mbbode_mutation(init_population)
        init_population = mbbode_cost(init_population)
        init_population = mbbode_rank(init_population, hsi_list)

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
            elite_cost['concentration'] = init_population['elite_concentration']
            elite_cost['h_balance'] = init_population['elite_h_balance']
            elite_cost['migration_time'] = init_population['elite_migration_time']

        # 展示改变后的全局最优解
        if save_elite_cost['power'] != elite_cost['power'] or save_elite_cost['concentration'] != elite_cost['concentration'] or save_elite_cost['migration_time'] != elite_cost['migration_time']:    # 每一代全局最优解有变化时才会记录并打印
            print elite_cost
            save_elite_cost = copy.deepcopy(elite_cost)


    # 计算初始随机解、及最终保留下来的所有迭代次数中最优解，其各项真实代价
    before_cost = compute_true_cost(save_chrom, rp, rm, v_p_cost, v_m_cost)
    after_costs = compute_true_cost(init_population['elite_chrom'], rp, rm, v_p_cost, v_m_cost)
    return after_costs, init_population['elite_chrom']

if __name__ == '__main__':
    '''
    hsi_list：可选String： power、h_balance(集群中HMs间负载方差)
    '''
    hsi_list = ['power']#,'h_balance']
    main(1000, 10, 50, 1.0, hsi_list)
