#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
现在更改mbbo用在Docker上的思路：
原来： 每次一旦被迁移率或者突变率选中，则一定选取满足约束条件的放置位置，
现在： 直接进行突变以及迁移，只记录突变的位置，不进行实际资源占用以及约束解判断，
      在进化n代之后进行无效解的判断，以及采用类BFD算法去影响最差解
'''

import time
import random
import math
import json
import sys
#from pyspark import SparkContext

## 在整个代码中，一直重复遇到的问题：1. 每个vm到hm的映射应该是唯一的,不会出现 12-4, 12-17 并存的情况（已解决）
## 2. 多个分布于同一hm的vm资源不应该超过hm资源约束

def init_Docker(rp_u, rm_u, p, num_var):
    '''
    目标：随机生成测试虚拟机集中每个vm对cpu和mem的资源请求
    参数：
    rp_u是对cpu请求的指导变量，rm_u是对mem资源请求的指导变量，虚拟机对cpu，mem的最终需求量会以正态分布的形式落在以指导变量为期望的邻域附近
    p代表虚拟机的cpu和mem两种资源之间的相关系数，负责控制每台虚拟机对两种资源需求的关联程度
    num_var是需要生成的虚拟机个数
    '''
    # print "进入 init_Docker"
    c_rp = range(num_var)                                                  # 记录每个虚拟机cpu,mem请求量
    c_rm = range(num_var)
    for i in range(num_var):
        c_rp[i] = random.uniform(0, 2*rp_u)
        c_rm[i] = random.uniform(0, rm_u)
    for i in range(num_var):
        r = random.random()
        if (r < p and c_rp[i] >= rp_u) or (r >= p and c_rp[i] < rp_u):     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            c_rm[i] += rm_u
        if c_rm[i] >= 1.0:                                               # 控制mem请求量合理性
            c_rm[i] -= 1.0
    #print "len(c_rp)= %s,len(c_rm) = %s" %(len(c_rp),len(c_rm))
    return c_rp, c_rm

def init_VM(c_rp, c_rm, rp_option, rm_option, num_var):
    '''
    持续查找可以容纳所有容器的vm：
    传入cpu参考列表rp_option,和mem可选列表rm_option
    c_rp,c_rm为已知的num_var个docker容器的尺寸
    num_var是容器个数，初始假设vm个数等于docker个数
    返回：虚拟机的num_var个尺寸元组序列
    '''
    # print "进入init_VM"
    v_rp = []
    v_rm = []
    i = 0
    while True:
        if i == num_var:                        # 对num_var个docker选择随机的vm位置
            #print "len(v_rp)= %s,len(v_rm) = %s" %(len(v_rp),len(v_rm))
            return v_rp, v_rm
        rp = random.choice(rp_option)
        rm = random.choice(rm_option)
        if rp >= c_rp[i] and rm >= c_rm[i]:     # p相关系数vm对cpu,mem请求量的相关性，值越大相关性越强
            v_rp.append(rp)
            v_rm.append(rm)
            i += 1
        else:
            continue

def migrate_Rate(size):
    '''
    目标：compute the Cosine migration rates，候选解越优秀迁入率越低，迁出率越高
    参数：
    size，初始种群中候选解的个数，即每代population中有size个chrom，每个chrom中有num_var个SIV
    '''
    lambdaa = range(size)                       # 每个解对应一对迁入lambdaa迁出率mu,共有size个解
    mu = range(size)
    for i in range(size):
        lambdaa[i] = math.cos(float(size - (i + 1)) / size)     # 按照种群所有候选解排名后的顺序，依次求解余弦迁入率，rank值越小迁入率越小
        mu[i] = math.sin(float(size - (i + 1)) / size)                  # 迁出率
    return lambdaa, mu


def check_effective(popu1, size, num_var):
    '''
    判断候选解的有效性
    '''
    # print "进入check_effective"
    # 先清空各vm,pm的资源使用率
    for i in xrange(size):
        for j in xrange(num_var):
            popu1['v_p_cost'][i][j] = 0
            popu1['v_m_cost'][i][j] = 0
            popu1['h_p_cost'][i][j] = 0
            popu1['h_m_cost'][i][j] = 0
    ## 逐一按照候选解，计算实际占用的vm,hm资源
    for i in xrange(size):
        vm_used_id = {}                                # 避免相同vm同时被映射的不同hm的错误
        for j in xrange(num_var):                      # 容器编号
            v_id = popu1['population'][i][j][0]
            h_id = popu1['population'][i][j][1]
            if v_id in vm_used_id:                     # 若vm已经被安排过
                if h_id == vm_used_id[v_id]:           # 且所在的hm与安排过的hm相同，则跳过该次循环，不需要重新计算资源占用
                    continue
                else:                                  # 若hm不同于安排的hm编号，说明出现同一个vm映射到不同hm的错误，直接返回
                    # print "in this chrom %s, a vm has been hosted on different hm, totally wrong!! " %popu1['population'][i]
                    return False
            else:                                      # 其他情况包括,包括多vm映射到1个hm,按正常情况计算
                popu1['v_p_cost'][i][v_id] += popu1['c_rp'][j]
                popu1['v_m_cost'][i][v_id] += popu1['c_rm'][j]
                popu1['h_p_cost'][i][h_id] += popu1['v_rp'][v_id]
                popu1['h_m_cost'][i][h_id] += popu1['v_rm'][v_id]
                vm_used_id[v_id] = h_id
        for x in xrange(num_var):                      # 只要超出资源限约束，即报错
            if popu1['v_p_cost'][i][x] > popu1['v_rp'][x] or popu1['v_m_cost'][i][x] > popu1['v_rm'][x] or popu1['h_p_cost'][i][x] > 1.0 or popu1['h_m_cost'][i][x] > 1.0:
                # print popu1['v_p_cost'][i][x], popu1['v_rp'][x]
                # print popu1['v_m_cost'][i][x], popu1['v_rm'][x]
                # print popu1['h_p_cost'][i][x]
                # print popu1['h_m_cost'][i][x]
                # print "find a error: VM or hm has overhold" , popu1['population'][i], x, vm_used_id, '\n'
                return False
    return True


def range2rect(size, num_var, type0):
    '''
    构造size * num_var 的矩阵
    ！！注意：python中list的引用可能造成全局参数的同时更改
    '''
    # 注意type0 是引用类型，若引用的是list，则更改type0的值倒置所有通过type0进行list赋值的都会被更改
    res = [[type0 for j in xrange(num_var)] for i in xrange(size)]
    return res

def make_population(size, num_var, c_rp, c_rm, v_rp, v_rm, time_base): #    作为全局变量，按照需要传入各方法中 f, p_mutate, time_base, lambdaa):
    '''
    构造一个population，包含size个候选解chrom,每个chrom是num_var个分别记录该容器所在的vm和hm编号的元组
    '''
    # print "进入make_population"
    population0 = {
        'c_rp': c_rp,                                             # 每个容器的cpu请求
        'c_rm': c_rm,                                             # 每个容器的mem请求
        'v_rp': v_rp,                                             # 每个vm的cpu请求
        'v_rm': v_rm,                                             # 每个vm的mem请求
        'population': range2rect(size, num_var, [0, 0]),          # size个chrom，每个chrom有num_var个双元素list[vm,hm]对应每个容器放置的vm编号和物理机编号
        'init_save': range2rect(size, num_var, [0, 0]),           # 保存初始size个chroms
        'v_p_cost': range2rect(size, num_var, 0.0),               # size个num_var长list记录每个vm上所有容器的cpu总请求,初始为0
        'v_m_cost': range2rect(size, num_var, 0.0),               # 每个vm被容器请求的mem，初始为0
        'h_p_cost': range2rect(size, num_var, 0.0),               # 每个HM被请求的cpu，初始为0
        'h_m_cost': range2rect(size, num_var, 0.0),               # HM被请求的mem，初始为0
        'power_cost': [x*0.0 for x in xrange(size)],              # list(size),记录当前代population中，每个chrom的能耗代价
        'v_balance_cost': [x*0.0 for x in xrange(size)],          # 计算现存与vm上的所有容器导致的均衡方差
        'h_balance_cost': [x*0.0 for x in xrange(size)],          # list(size),每个chrom中对hm的资源负载均衡指数
        'migration_time': [x*0.0 for x in xrange(size)],          # list(size),记录迁移时间，这里指定为固定值
        'rank': [x*0 for x in xrange(size)],                      # list(size),记录每个chrom排名，rank值越大，排名越靠后
        'elite_power': 999999.0*num_var,                          # float,记录每代种群中最优秀解的能耗代价值
        'elite_v_balance': 999999.0*num_var,                      # float,记录每代种群中最优秀解的vm层负载均衡方差
        'elite_h_balance': 999999.0*num_var,                      # float,记录每代种群中最优秀解的hm层负载均衡方差
        'elite_migration_time': time_base*num_var,                # float,........的迁移时间
        'elite_chrom': range(num_var)                             # list(num_var)，保存每代种群中精英chrom
    }
    return population0


def initialize_population(popu1, size, num_var):
    '''
    初始化docker容器放置的vm编号，以及vm所能放置的hm编号，并计算初代种群的各项数值
    '''
    # print "进入initialize_population"
    # 为所有容器选择能够容纳其尺寸的vm_id
    for i in xrange(size):
        # 记录每个chrom中，vm-hm的映射，保证映射在相同vm的不同容器，所在的hm也相同
        vm_used_id = {}
        for j in xrange(num_var):
            # 为第j个容器选择要能容纳其尺寸的vm编号
            while True:
                tmp_v_id = random.randint(0, num_var-1)
                cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
                mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
                if cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]:
                    # popu1['population'][i][j]是第i个chrom的第j个容器放置的[vm_id,hm_id]
                    popu1['population'][i][j] = [tmp_v_id, 0]
                    popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                    popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v

                    # 找到容器-vm的拓扑后，继续寻找能够满足该vm尺寸的hm
                    flag = True
                    # 对与已经安排过vm-hm映射位置的容器，直接进行对应vm,hm的赋值，并设while循环初始为False
                    if tmp_v_id in vm_used_id:
                        popu1['population'][i][j] = [tmp_v_id, vm_used_id[tmp_v_id]]
                        flag = False
                    while flag:
                        # 对未安排hm的容器所对应的vm，循环查找满足vm尺寸的h
                        tmp_h_id = random.randint(0, num_var-1)
                        cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
                        mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
                        if cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0:
                            popu1['population'][i][j] = [tmp_v_id, tmp_h_id]
                            popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
                            popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
                            vm_used_id[tmp_v_id] = tmp_h_id
                            break
                    break
    # 保存初代种群
    for i in xrange(size):
        popu1['init_save'][i] = popu1['population'][i][:]
    if check_effective(popu1, size, num_var):
        # print "Initailization population is effective"
        return popu1
    else:
        sys.exit("failed in initializating population")


def mbbode_migration(popu1, size, num_var, f, lambdaa):
    '''
    一旦被迁移概率选中：只进行记录被迁移影响后的解位置，不计算具体的vm被请求的cpu,mem以及hm被请求的cpu,mem
    '''
    # print "进入mbbode_migration"
    for i in xrange(size):
        for j in xrange(num_var):
            rand_sum = random.random()
            # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
            lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])
            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
            if rand_sum < lambda_scale:
                index1 = random.randint(0, size-1)
                index2 = random.randint(0, size-1)
                while index1 == index2:
                    index2 = random.randint(0, size-1)
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                tmp_v_id = abs(int(popu1['population'][i][j][0] \
                          + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) \
                          + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] \
                          + 0.5)) % num_var)
                tmp_h_id = abs(int(popu1['population'][i][j][1] \
                          + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) \
                          + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] \
                          + 0.5)) % num_var)
                popu1['population'][i][j] = [tmp_v_id, tmp_h_id]

            # 每一代解的有效性以及实际vm、hm的资源占用尽在计算代价的时候进行
            popu1['v_p_cost'][i][j] = 0.00
            popu1['v_m_cost'][i][j] = 0.00
            popu1['h_p_cost'][i][j] = 0.00
            popu1['h_m_cost'][i][j] = 0.00
    return popu1


def mbbode_mutation(popu1, size, num_var, p_mutate):
    '''
    一旦被迁移概率选中：只记录突变后的vm,hm；不计算具体的vm,hm资源占用
    '''
    # print "进入mbbode_mutation"
    for i in xrange(size):
        for j in xrange(num_var):
            rand_sum = random.random()
            # 被突变概率选中，随机生成新的SIV
            if rand_sum < p_mutate:
                tmp_v_id = random.randint(0, num_var-1)
                tmp_h_id = random.randint(0, num_var-1)
                popu1['population'][i][j] = [tmp_v_id, tmp_h_id]
    return popu1


def fix_effective(popu1, size, num_var):
    '''
    判断候选解的有效性
    '''
    # print "进入fix_effective"
    # 先清空各vm,pm的资源使用率
    for i in xrange(size):
        for j in xrange(num_var):
            popu1['v_p_cost'][i][j] = 0
            popu1['v_m_cost'][i][j] = 0
            popu1['h_p_cost'][i][j] = 0
            popu1['h_m_cost'][i][j] = 0

    # 对size个chrom，注意判断解合理性vm-hm不存在一对多；再逐一对当前chrom进行约束判断，对于约束失败的直接进行fix
    for i in xrange(size):
        ## 以下所有的判断分别对每个chrom进行
        vm_used_id = {}
        # 判断并更改使得解合理
        for j in xrange(num_var):                      # 容器编号
            v_id = popu1['population'][i][j][0]
            h_id = popu1['population'][i][j][1]

            # 判断vm-hm映射关系是否唯一，如果不唯一，那么选择vm已有的hm替换之
            if v_id in vm_used_id:
                if h_id == vm_used_id[v_id]:           # 合理解
                    continue
                # 说明解中j容器的vm实际上已经存在其他hm上了，解无效；下面给出办法化为有效解：强制将其hm改为字典记录的vm:hm
                else:
                    # print "ops, a vm has been hosted on different hm, totally wrong!! fixing"
                    popu1['population'][i][j] = [v_id, vm_used_id[v_id]]
            # 新建vm:hm直接加入字典
            else:
                vm_used_id[v_id] = h_id

        # 统计资源
        ## HM资源占用以vm_used_id作为基准
        for v_id, h_id in vm_used_id.items():
            popu1['h_p_cost'][i][h_id] += popu1['v_rp'][v_id]
            popu1['h_m_cost'][i][h_id] += popu1['v_rm'][v_id]
        ## vm资源占用按照逐个容器去统计
        for x in xrange(num_var):               # 容器编号
            v_id = popu1['population'][i][x][0]
            popu1['v_p_cost'][i][v_id] += popu1['c_rp'][x]
            popu1['v_m_cost'][i][v_id] += popu1['c_rm'][x]

        # 对于超出vm约束的情况的fix
        for index in xrange(num_var):
            if popu1['v_p_cost'][i][index] > popu1['v_rp'][index] or popu1['v_m_cost'][i][index] > popu1['v_rm'][index]:
                # print "修改vm超载的情况",index,popu1['v_p_cost'][i][index],popu1['v_rp'][index]

                # 说明index号vm有问题，遍历size编号为i的chrom，查找index vm上的所有容器编号
                containers = [a for a, b in enumerate(popu1['population'][i]) if b[0] == index]
                # 一定要找到符合资源约束的方案，否则持续循环
                while True:
                    # 对这些索引的容器调整vm编号，以使其可以满足资源约束（可以将最小的迁出）
                    ids = [popu1['c_rp'][c] for c in containers]
                    c = containers[ids.index(min(ids))]
                    popu1['v_p_cost'][i][index] -= popu1['c_rp'][c]
                    popu1['v_m_cost'][i][index] -= popu1['c_rm'][c]
                    # print c, containers
                    containers.remove(c)            # 已经拿出的容器要及时删除
                    # print c, containers

                    # 在资源使用大于0.00的vm中，寻找可容纳容器c的vm
                    # 所有非空vm的字典
                    tmp_v = dict([[b, a] for a, b in enumerate(popu1['v_p_cost'][i]) if b > 0.000])
                    min_v = tmp_v[min(tmp_v.keys())]   # 资源使用最少的vm编号
                    cpu_tmp_v = popu1['v_p_cost'][i][min_v] + popu1['c_rp'][c]
                    mem_tmp_v = popu1['v_m_cost'][i][min_v] + popu1['c_rm'][c]

                    # 若最小vm可容纳，则进行放置
                    # 已找到合理位置，进行资源重新计算就行
                    if cpu_tmp_v <= popu1['v_rp'][min_v] and mem_tmp_v <= popu1['v_rm'][min_v]:
                        popu1['v_p_cost'][i][min_v] = cpu_tmp_v
                        popu1['v_m_cost'][i][min_v] = mem_tmp_v
                        popu1['population'][i][c] = [min_v, vm_used_id[min_v]]
                    else:
                        # 最小的都无法容纳，只能新建vm
                        while True:
                            location = random.randint(0, num_var-1)
                            if popu1['v_p_cost'][i][location] == 0.00:
                                # 在已使用的hm中选择一个占用最少的,即使会导致其超载，在下一步的hm处理中会重新处理
                                tmp_h = dict([[b, a] for a, b in enumerate(popu1['h_p_cost'][i]) if b > 0.000])
                                try:
                                    min_h = tmp_h[min(tmp_h.keys())]   # 资源使用最少的hm编号
                                except ValueError:
                                    # print "hm代价统计异常",popu1['h_p_cost'][i]
                                    sys.exit(0)
                                popu1['population'][i][c] = [location, min_h]
                                popu1['h_p_cost'][i][min_h] += popu1['v_rp'][location]
                                popu1['h_m_cost'][i][min_h] += popu1['v_rm'][location]
                                vm_used_id[location] = min_h     # 该次vm-hm放入vm_used_id中记录
                                break

                    # 若拿出容器c后 vm_index不再超载，则退出，检查下一个vm
                    if popu1['v_p_cost'][i][index] <= popu1['v_rp'][index] and popu1['v_m_cost'][i][index] <= popu1['v_rm'][index]:
                        break
                    # 否则，继续while循环取次小的容器，并选择放置

        # 对于超出hm约束的情况的fix
        for index in xrange(num_var):
            if popu1['h_p_cost'][i][index] > 1.0 or popu1['h_m_cost'][i][index] > 1.0:
                # print "过载的hm编号是： ",index
                # 说明index号hm有问题，根据之前记录的字典vm_used_id放于该hm上vms的编号
                vms = [v for v, h in vm_used_id.items() if h == index]
                # print "该物理机上放置的虚拟机为： ",vms
                # 一定要找到符合资源约束的方案，否则持续循环
                while True:
                    # 找到尺寸最小的vm，并迁出
                    # print "该物理机上的虚拟机：",[popu1['v_rp'][v] for v in vms]
                    ids = [popu1['v_rp'][v] for v in vms]
                    v = vms[ids.index(min(ids))]
                    # print v
                    popu1['h_p_cost'][i][index] -= popu1['v_rp'][v]
                    popu1['h_m_cost'][i][index] -= popu1['v_rm'][v]
                    vms.remove(v)            # 已经拿出的vm要及时删除

                    # 查找vm编号为v的所有容器
                    cons = [ sux for sux, siv in enumerate(popu1['population'][i]) if siv[0] == v]

                    # 在资源使用大于0.00的hm中，寻找可容纳vm的hm
                    # 所有非空hm的字典
                    tmp_h = dict([[b, a] for a, b in enumerate(popu1['h_p_cost'][i]) if b > 0.000])
                    min_h = tmp_h[min(tmp_h.keys())]   # 资源使用最少的hm编号
                    cpu_tmp_h = popu1['h_p_cost'][i][min_h] + popu1['v_rp'][v]
                    mem_tmp_h = popu1['h_m_cost'][i][min_h] + popu1['v_rm'][v]

                    # 若最小hm可容纳，则进行放置
                    # 已找到合理位置，进行资源重新计算就行
                    if cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0:
                        popu1['h_p_cost'][i][min_h] = cpu_tmp_h
                        popu1['h_m_cost'][i][min_h] = mem_tmp_h
                        # 更改放于vm编号为v的所有容器对应的hm编号为min_h
                        for con in cons:
                            popu1['population'][i][con] = [v, min_h]
                        # 更改vm_used_id字段
                        vm_used_id[v] = min_h
                    else:
                        # 最小的都无法容纳，只能新建hm
                        while True:
                            location = random.randint(0, num_var-1)
                            if popu1['h_p_cost'][i][location] == 0.00:
                                # 更改放于vm编号为v的所有容器对应的hm编号为min_h
                                for con in cons:
                                    popu1['population'][i][con] = [v, location]
                                # 修改资源
                                popu1['h_p_cost'][i][location] += popu1['v_rp'][v]
                                popu1['h_m_cost'][i][location] += popu1['v_rm'][v]
                                break

                    # 若拿出vm v后, hm_index不再超载，则退出，检查下一个hm
                    if popu1['h_p_cost'][i][index] <= 1.0 and popu1['h_m_cost'][i][index] <= 1.0:
                        break
                    # 否则继续while循环，取出次小的vm
    return popu1


# def mbbode_cost(popu1, size, num_var, time_base):
#     '''
#     首先计算本次迭代后实际vm,hm的资源占用情况，接着判断解的有效性
#     对与不满足解的有效性：1. 同一个vm不可出现在不同hm上
#                       2. 放于同一vm上的容器实际请求的vm cpu，mem资源不可超过vm尺寸
#                       3. 放于hm上的vm不可超过hm实际尺寸
#     '''

#     # 首先，check_effective()进行解的有效性判断，对于无效解进行处理
#     if not check_effective(popu1, size, num_var):
#         fix_effective(popu1, size, num_var)

#     # 再具体进行各项HSI的计算
#     ## 计算能耗 —— 能耗计算，仅以hm实际被vm占用的cpu作为唯一参数进行计算
#     for i in xrange(size):
#         for j in xrange(num_var):
#             x = popu1['h_p_cost'][i][j]
#             if x > 0.0:
#                 popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)

#     ## 计算负载均衡指数
#     # 同时计算容器在vm上放置产生的负载均衡情况，以各vm的被容器请求的实际资源v_p_cost,v_m_cost为依据; 和vm在hm上产生的负载均衡情况，以h_p_cost,h_m_cost为计算依据
#     for i in xrange(size):
#         v_load_index = range(num_var)        # vm的负载均衡指数列表，每个chrom共num_var个（以容器实际使用vm的资源计算）
#         v_average_load_index = 0.0
#         h_load_index = range(num_var)        # hm的负载均衡指数列表，每个chrom共num_var个（以vm实际使用hm的资源计算）
#         h_average_load_index = 0.0
#         for j in xrange(num_var):         # vm的标号/hm的编号
#             v_load_index[j] = 1.0 / (1.0005 - popu1['v_p_cost'][i][j]) / (1.0005 - popu1['v_m_cost'][i][j])
#             v_average_load_index += v_load_index[j]
#             h_load_index[j] = 1.0 / (1.0005 - popu1['h_p_cost'][i][j]) / (1.0005 - popu1['h_m_cost'][i][j])
#             h_average_load_index += h_load_index[j]
#         v_average_load_index /= num_var
#         h_average_load_index /= num_var
#         for j in xrange(num_var):        # 同时计算vm层、hm层的load-index方差，反映整体的分布情况
#             popu1['v_balance_cost'][i] = popu1['v_balance_cost'][i] + (v_load_index[j] - v_average_load_index)*(v_load_index[j] - v_average_load_index)
#             popu1['h_balance_cost'][i] = popu1['h_balance_cost'][i] + (h_load_index[j] - h_average_load_index)*(h_load_index[j] - h_average_load_index)
#         popu1['v_balance_cost'][i] = math.sqrt(popu1['v_balance_cost'][i] / num_var)
#         popu1['h_balance_cost'][i] = math.sqrt(popu1['h_balance_cost'][i] / num_var)

#     ## 计算迁移时间 —— 由于容器是无状态迁移，所以不需要考虑容器的迁移时间，仅考虑虚拟机的迁移
#     for i in xrange(size):
#         a = dict(popu1['population'][i])                           # 进化后的(vm,hm)字典
#         b = dict(popu1['init_save'][i])                            # 初始的(vm,hm)字典
#         for x, y in a.items():
#             if x in b and y != b[x]:            # 若x不在b,说明是进化后新建的;若a中没有的vm，有可能b有，那就是进化后删除了，或者b也没有;均不需要考虑迁移时间
#                 popu1['migration_time'][i] += time_base

#         # # # 剔除无效迁移  —— 在vm限定若干种尺寸规格的情况下，剔除无效迁移很必要——还没写完
#         # for x,y in a.items():
#         #     for l,m in b.items():
#         #         if popu1['v_rp'][x] == popu1['v_rp'][l] and popu1['v_rm'][x] == popu1['v_rm'][l] and y == m:   # 两个vm尺寸相同，并且A的新hm是B的源hm,则B不动，A直接迁入B的新hm中
#         #             a[x] = a[l]
#         #             a[l] = m        # a[l] = (b[l] == m)                         # 如此更改不会影响到能耗，两层负载等的计算，只是减免1次迁移时间
#         #             popu1['migration_time'][i] -= time_base
#         #             print x,y,l,m,a,b
#         #             print "find an invalid migration\n"
#     return popu1
def mbbode_cost(popu1, size, num_var, time_base):
    '''
    首先计算本次迭代后实际vm,hm的资源占用情况，接着判断解的有效性
    对与不满足解的有效性：1. 同一个vm不可出现在不同hm上
                      2. 放于同一vm上的容器实际请求的vm cpu，mem资源不可超过vm尺寸
                      3. 放于hm上的vm不可超过hm实际尺寸
    '''
    # print "进入mbbode_cost"
    # 首先，check_effective()进行解的有效性判断，对于无效解进行处理
    if not check_effective(popu1, size, num_var):
        popu1 = fix_effective(popu1, size, num_var)

    # 再具体进行各项HSI的计算
    ## 计算能耗 —— 能耗计算，仅以hm实际被vm占用的cpu作为唯一参数进行计算
    for i in xrange(size):
        popu1['power_cost'][i] = 0.0           # 每代清空代价重新计算
        popu1['v_balance_cost'][i] = 0.0
        popu1['h_balance_cost'][i] = 0.0
        popu1['migration_time'][i] = 0.0

        v_load_index = range(num_var)        # vm的负载均衡指数列表，每个chrom共num_var个（以容器实际使用vm的资源计算）
        v_average_load_index = 0.0
        h_load_index = range(num_var)        # hm的负载均衡指数列表，每个chrom共num_var个（以vm实际使用hm的资源计算）
        h_average_load_index = 0.0
        for j in xrange(num_var):            # vm的标号/hm的编号
            x = popu1['h_p_cost'][i][j]
            if x > 0.0:
                popu1['power_cost'][i] += (446.7 + 5.28*x - 0.04747*x*x + 0.000334*x*x*x)

    ## 计算负载均衡指数
    # 同时计算容器在vm上放置产生的负载均衡情况，以各vm的被容器请求的实际资源v_p_cost,v_m_cost为依据;
    # 和vm在hm上产生的负载均衡情况，以h_p_cost,h_m_cost为计算依据
            v_load_index[j] = 1.0 / (1.0005 - popu1['v_p_cost'][i][j]) / (1.0005 - popu1['v_m_cost'][i][j])
            v_average_load_index += v_load_index[j]
            h_load_index[j] = 1.0 / (1.0005 - popu1['h_p_cost'][i][j]) / (1.0005 - popu1['h_m_cost'][i][j])
            h_average_load_index += h_load_index[j]

        v_average_load_index /= num_var
        h_average_load_index /= num_var
        for j in xrange(num_var):        # 同时计算vm层、hm层的load-index方差，反映整体的分布情况
            popu1['v_balance_cost'][i] += (v_load_index[j] - v_average_load_index)*(v_load_index[j] - v_average_load_index)
            popu1['h_balance_cost'][i] += (h_load_index[j] - h_average_load_index)*(h_load_index[j] - h_average_load_index)
        popu1['v_balance_cost'][i] = math.sqrt(popu1['v_balance_cost'][i] / num_var)
        popu1['h_balance_cost'][i] = math.sqrt(popu1['h_balance_cost'][i] / num_var)

    ## 计算迁移时间 —— 由于容器是无状态迁移，所以不需要考虑容器的迁移时间，仅考虑虚拟机的迁移
        a = dict(popu1['population'][i])                           # 进化后的(vm,hm)字典
        b = dict(popu1['init_save'][i])                            # 初始的(vm,hm)字典
        # print a,b
        for x, y in a.items():
            if x in b and y != b[x]:            # 若x不在b,说明是进化后新建的;若a中没有的vm，有可能b有，那就是进化后删除了，或者b也没有;均不需要考虑迁移时间
                # print "发现一个迁移的"
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
    # print "本代代价结果：", popu1['power_cost'], popu1['v_balance_cost'], popu1['h_balance_cost'], popu1['migration_time']

    return popu1

def mbbode_rank(popu1, size):
    '''
    4个目标同时进行比较，（可以为每个目标设置权重表示该目标的重要性）
    '''
    # print "进入mbbode_rank"
    # 非支配解排名在size个解之间
    for i in xrange(size):
        popu1['rank'][i] = 0
    for i in xrange(size):
        for j in xrange(i+1, size):
            if popu1['power_cost'][i] <= popu1['power_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['power_cost'][i] > popu1['power_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['v_balance_cost'][i] <= popu1['v_balance_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['v_balance_cost'][i] > popu1['v_balance_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['h_balance_cost'][i] <= popu1['h_balance_cost'][j]:
                popu1['rank'][j] += 1
            elif popu1['h_balance_cost'][i] > popu1['h_balance_cost'][j]:
                popu1['rank'][i] += 1
            if popu1['migration_time'][i] <= popu1['migration_time'][j]:
                popu1['rank'][j] += 1
            elif popu1['migration_time'][i] > popu1['migration_time'][j]:
                popu1['rank'][i] += 1

    # 寻找当前经过迁移突变后种群的排名rank最小值
    rank = popu1['rank'].index(min(popu1['rank']))
    # print popu1['rank'], rank
    # print "上代结果：" , popu1['elite_power'], popu1['elite_v_balance'], popu1['elite_h_balance'], popu1['elite_migration_time']
    if popu1['elite_power'] > popu1['power_cost'][rank]:# and popu1['elite_v_balance'] > popu1['v_balance_cost'][rank] and popu1['elite_h_balance'] > popu1['h_balance_cost'][rank]:
        popu1['elite_power'] = popu1['power_cost'][rank]                        # 若当代rank最小的解优于上代保存的精英解，则替换精英解
        popu1['elite_v_balance'] = popu1['v_balance_cost'][rank]
        popu1['elite_h_balance'] = popu1['h_balance_cost'][rank]
        popu1['elite_migration_time'] = popu1['migration_time'][rank]
        popu1['elite_chrom'] = popu1['population'][rank][:]
        # print "本代结果替代后：" , popu1['elite_power'], popu1['elite_v_balance'], popu1['elite_h_balance'], popu1['elite_migration_time']
    else:                                                                       # 若精英解仍旧最优，则用上代精英解随机替换当代的size=0 的候选解
        popu1['population'][0] = popu1['elite_chrom'][:]
    return popu1


def main(generation, size, num_var, p):
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
    rp_option = [1.0]                      # vm可选的cpu尺寸
    rm_option = [1.0]                      # vm可选的mem尺寸

    # 2.初始化num_var个容器和vm，以及计算迁移率
    c_rp, c_rm = init_Docker(rp_u, rm_u, p, num_var)
    v_rp, v_rm = init_VM(c_rp, c_rm, rp_option, rm_option, num_var)
    lambdaa, mu = migrate_Rate(size)

    print "开始主流程"
    ## 以下程序的流程按照先按照串行结构书写
    # 3. 初代种群的生成、代价计算及排序
    init_popu = make_population(size, num_var, c_rp, c_rm, v_rp, v_rm, time_base)
    init_popu = initialize_population(init_popu, size, num_var)
    init_popu = mbbode_cost(init_popu, size, num_var, time_base)
    init_popu = mbbode_rank(init_popu, size)

    # 随机保存一个初代候选解
    tmp = random.randint(0, size-1)                                # 从每个群岛的population中size个随机选出第tmp各解
    save_chrom = init_popu['population'][tmp]                      # 随机挑选的第tmp个初始候选解，代表MBBO执行前vm-hm拓扑关系
    save_cost = (init_popu['power_cost'][tmp], init_popu['v_balance_cost'][tmp], init_popu['h_balance_cost'][tmp], init_popu['migration_time'][tmp])                                               # 第tmp个初始候选解的3个HSI代价值

    elite_cost = [9999.9*num_var, 9999.9*num_var, 9999.9*num_var, time_base*num_var]   # 初设的全局精英解能耗代价、负载均衡方差、迁移时间
    save_elite_cost = [0, 0, 0, 0]                                 # 用于保存每一代的全局最优解，并在新的一代时比较有否变化，只有改变后才会打印，否则不打印
    time1 = time.time()                                            # 算法迭代进化开始时间戳

    ## 开始种群迭代进化
    for g in range(generation):                                    # 设置最大迭代次数
        init_popu = mbbode_migration(init_popu, size, num_var, f, lambdaa)
        init_popu = mbbode_mutation(init_popu, size, num_var, p_mutate)
        init_popu = mbbode_cost(init_popu, size, num_var, time_base)
        init_popu = mbbode_rank(init_popu, size)

        ## 获取全局最优解的能耗代价、负载均衡指数、以及迁移时间
        if elite_cost[0] > init_popu['elite_power']:# and elite_cost[1] > init_popu['elite_v_balance'] and elite_cost[2] > init_popu['elite_h_balance']:
            elite_cost[0] = init_popu['elite_power']
            elite_cost[1] = init_popu['elite_v_balance']
            elite_cost[2] = init_popu['elite_h_balance']
            elite_cost[3] = init_popu['elite_migration_time']
            # print "执行全局精英解替换"

        # 记录每次迭代 改变的 全局最优解值
        if save_elite_cost[0] != elite_cost[0] or save_elite_cost[1] != elite_cost[1] or save_elite_cost[2] != elite_cost[2] or save_elite_cost[3] != elite_cost[3]:
            print "执行全局精英解替换：", elite_cost[0], elite_cost[1], elite_cost[2], elite_cost[3]
            save_elite_cost = elite_cost[:]

    # 结果展示
    time2 = time.time()
    print 'Time cost: ', (time2 - time1), '\n'
    save_chrom = dict(save_chrom)
    elite_chrom = dict(init_popu['elite_chrom'])
    print 'the init chrom maybe is %s, use %s pms, the cost is %s' %(save_chrom, len(set(save_chrom.values())), save_cost)
    print 'after mbbo, chrom is %s, use %s pms' %(elite_chrom, len(set(elite_chrom.values()))), '\n', elite_cost
    print init_popu

if __name__ == '__main__':
    main(1000, 10, 200, 1.0)
