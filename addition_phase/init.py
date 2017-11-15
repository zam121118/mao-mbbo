#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-13
@Author : Amy
Goal: 用于生成新增时d-v-h架构初始状态，并尽量保留mbbo数据类型方便说明聚合时mbbo优于BFD算法;
      生成新增容器序列，引入replicas考虑，对于同服务多副本必须使用互斥调度原则，不可同VM
'''


import time
import random
import math
import json
import sys
import copy


def range2rect(size, num_var, type0):
    '''
    构造size * num_var 的矩阵
    ！！注意：python中list的引用可能造成全局参数的同时更改
    '''
    # 注意type0 是引用类型，若引用的是list，则更改type0的值导致所有通过type0进行list赋值的都会被更改
    res = [[type0 for j in xrange(num_var)] for i in xrange(size)]
    return res

def init_Docker(rp_u, rm_u, p, num_var):
    '''
    目标：随机生成容器cpu、mem二维尺寸
    参数：
    rp_u，rm_u指导对cpu，mem的最终需求量会以正态分布的形式落在以指导变量为期望的邻域附近
    p代表虚拟机的cpu和mem两种资源之间的相关系数，负责控制每台虚拟机对两种资源需求的关联程度
    num_var 初始状态中VM数量
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
    goal： 根据已有容器大小，初始化的d-v-h映射关系
    参数:
    rp_option和rm_option分别为VM可选的CPU、mem尺寸
    c_rp,c_rm为对应下标的容器尺寸
    num_var容器个数，初始假设vm数量与容器数量1：1
    返回：
    能够容纳对应编号容器的VM有效尺寸系列
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
        if rp >= c_rp[i] and rm >= c_rm[i]:
            v_rp.append(rp)
            v_rm.append(rm)
            i += 1
        else:
            continue


def make_population(size, num_var, c_rp, c_rm, v_rp, v_rm): #    作为全局变量，按照需要传入各方法中 f, p_mutate, time_base, lambdaa):
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
        'v_p_cost': range2rect(size, num_var, 0.0),               # size个num_var长list记录每个vm上所有容器的cpu总请求,初始为0
        'v_m_cost': range2rect(size, num_var, 0.0),               # 每个vm被容器请求的mem，初始为0
        'h_p_cost': range2rect(size, num_var, 0.0),               # 每个HM被请求的cpu，初始为0
        'h_m_cost': range2rect(size, num_var, 0.0),               # HM被请求的mem，初始为0
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
   
    if check_effective(popu1, size, num_var):
        print "Initailization population is effective"
        return popu1
    else:
        sys.exit("failed in initializating population")
        
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
                return False
    return True

def create_addition_list(rp_u, rm_u, p, addtion_nums):
    '''
    生成新增序列，记录新增容器的尺寸，以及集群需要维持的各类容器replicas数（注： 同服务的各replicas不可放于同VM）
    '''
    c_rp, c_rm = init_Docker(rp_u, rm_u, p, addtion_nums)   # 生成新增容器尺寸

    addtion0 = {
        'c_rp':c_rp,                        # 新增容器cpu占用量
        'c_rm':c_rm,                        # 新增容器mem占用量
        'replicas':[ random.randint(0,5) for i in xrange(addtion_nums)]                     # 新增的该服务容器所需副本数
    }
    return addtion0


def main(num_var, p, addtion_nums):
    # 1.算法主要参数设置
    rp_u = 0.25                            # 容器请求CPU的指导变量
    rm_u = 0.25                            # 容器请求MEM的指导变量
    p = p                                  # 控制容器cpu,mem的资源相关度
    rp_option = [1.0]                      # vm可选的cpu尺寸
    rm_option = [1.0]                      # vm可选的mem尺寸

    size = 1                               # 新增阶段只需单解

    # 2.初始化num_var个容器和vm，以及计算迁移率
    c_rp, c_rm = init_Docker(rp_u, rm_u, p, num_var)
    v_rp, v_rm = init_VM(c_rp, c_rm, rp_option, rm_option, num_var)

    print "开始主流程"

    ## 以下程序的流程按照先按照串行结构书写
    # 3. 初代种群的生成
    init_popu = make_population(size, num_var, c_rp, c_rm, v_rp, v_rm)
    init_popu = initialize_population(init_popu, size, num_var)

    # 4. 生成新增容器序列
    addtion0 = create_addition_list(rp_u, rm_u, p, addtion_nums)

    # print 'init_popu = {0}, \n addition0 = {1} \n'.format(init_popu, addtion0)

    # 5. 针对two-domensions（cpu,mem）使用FFDProd、FFDSum、Dot-product（此处进行改进，使用cosine）、L2（基于鸥几里得距离）
    # 注意： Swarm scheduler 的binpack strategy 即类似于 FFDSum，通过求weight进行打分，
    # 详见github.com/docker/swarm/blob/master/scheduler/strategy/weighted_node.go或者图库截图

    result0 = FFDProd()
    result1 = FFDSum()         # 此处FFDSum使用于swarm相同的strategy
    result2 = Dot_product()
    result3 = l2()


if __name__=='__main__':
    main(5, 1.0, 6)