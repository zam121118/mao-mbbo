#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-22
@Author : Amy
Goal : useful modules
Digest : 本模块定义了能够描述FFDSum以及Dot-Prod算法的有效模块，可以灵活的在第三方文件中引用
'''

import time
import random
import math
from init import *

def Dot_product(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    '''

    print " \n进入 Dot_product() 方法" 


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM计算向量间夹角余弦值，值最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM计算与VM向量间夹角余弦值，值最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = weightVMBins_DotProd(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = find_HM(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix, weightHMBins_DotProd)

                # 更新放入该object（容器）造成的bin（VM）资源变化
                bins['v_p_cost'][0][vm_suffix] += object_CPU
                bins['v_m_cost'][0][vm_suffix] += object_MEM
                
                # 将容器及其放置位置加入‘population’中
                bins['population'][0].append([vm_suffix, hm_suffix])
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)

                # 已经解决掉一个object
                i -= 1 
                continue
                
            # 否则，当前集群没有能容纳该object（容器）的bin（VM）
            else:
                # 随机生成一个足以容纳该容器的VM, 获取编号
                # vm = create_VM(object_CPU, object_MEM, rp_option, rm_option)
                vm = create_VM(object_CPU, object_MEM, vm_option)
                vm_suffix = len(bins['v_p_cost'][0])

                # 为该VM找寻HM,并更新HM资源变动及map_v_h
                hm_suffix = find_HM(bins, vm['rp'], vm['rm'], vm_suffix, weightHMBins_DotProd)

                # 更新放入容器后造成的VM资源变化
                bins['v_p_cost'][0].append(object_CPU)
                bins['v_m_cost'][0].append(object_MEM)

                # 追加系统容器、vm数量及资源分布
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)
                bins['v_rp'].append(vm['rp'])
                bins['v_rm'].append(vm['rm'])

                # 更新‘population’、‘map_v_h’
                bins['population'][0].append([vm_suffix, hm_suffix])

                # 已经解决掉一个object
                i -= 1
                continue

    # 说明性数据统计
    num = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "Dot-Prod used time is {} \n used the number of HMs is {}".format(used_time, len(num))
    return (bins, used_time)


def FFDSum(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    '''

    print " \n进入 FFDSum() 方法" 


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM打分，分最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM打分，分最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = weightVMBins_FFDSum(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = find_HM(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix, weightHMBins_FFDSum)

                # 更新放入该object（容器）造成的bin（VM）资源变化
                bins['v_p_cost'][0][vm_suffix] += object_CPU
                bins['v_m_cost'][0][vm_suffix] += object_MEM
                
                # 将容器及其放置位置加入‘population’中
                bins['population'][0].append([vm_suffix, hm_suffix])
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)

                # 已经解决掉一个object
                i -= 1 
                continue
                
            # 否则，当前集群没有能容纳该object（容器）的bin（VM）
            else:
                # 随机生成一个足以容纳该容器的VM, 获取编号
                # vm = create_VM(object_CPU, object_MEM, rp_option, rm_option)
                vm = create_VM(object_CPU, object_MEM, vm_option)
                vm_suffix = len(bins['v_p_cost'][0])

                # 为该VM找寻HM,并更新HM资源变动及map_v_h
                hm_suffix = find_HM(bins, vm['rp'], vm['rm'], vm_suffix, weightHMBins_FFDSum)

                # 更新放入容器后造成的VM资源变化
                bins['v_p_cost'][0].append(object_CPU)
                bins['v_m_cost'][0].append(object_MEM)

                # 追加系统容器、vm数量及资源分布
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)
                bins['v_rp'].append(vm['rp'])
                bins['v_rm'].append(vm['rm'])

                # 更新‘population’、‘map_v_h’
                bins['population'][0].append([vm_suffix, hm_suffix])

                # 已经解决掉一个object
                i -= 1
                continue

    # 说明性数据统计
    num = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "FFDSum used time is {} \n used the number of HMs is {}".format(used_time, len(num))
    return (bins, used_time)


def find_HM(bins, v_rp, v_rm, vm_suffix, handle):
    '''
    为VM找寻可容纳其的HM标号(系统已有/新增)，并更新所引起的hm资源编号，及map_v_h
    '''
    # 对集群已有的所有HMs进行打分
    # weightedHMBins = weightHMBins(bins, v_rp, v_rm)
    weightedHMBins = handle(bins, v_rp, v_rm)

    # 更新得分最高的HM资源
    if len(weightedHMBins) > 0:
        hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
        bins['h_p_cost'][0][hm_suffix] += v_rp
        bins['h_m_cost'][0][hm_suffix] += v_rm  
    # 更新新HM资源
    else:
        hm_suffix = len(bins['h_m_cost'][0])
        bins['h_p_cost'][0].append(v_rp)
        bins['h_m_cost'][0].append(v_rm)

    # 更新放入VM造成的新HM资源变化及map_v_h
    bins['map_v_h'][vm_suffix] = hm_suffix
    return hm_suffix


def deprecated_create_VM(c_rp, c_rm, rp_option, rm_option):

    '''
    依据实验可选的VMcpu、mem list尺寸(rp_option、rm_option)随机生成可以容纳(c_rp、c_rm)的VM
    '''
    print "\n 进入 create_VM() 方法"

    vm = {'rp':0, 'rm':0}
    while vm['rp'] == 0:
        rp = random.choice(rp_option)
        rm = random.choice(rm_option)
        if rp >= c_rp and rm >= c_rm:
            vm['rp'],vm['rm'] = rp,rm
    return vm

def create_VM(c_rp, c_rm, vm_option):

    '''
    为了防止完全随机的产生虚拟机尺寸，而希望可以人为的预先设置几种虚拟机尺寸(cpu, mem)
    [0.3, 0.3], [0.5, 0.4] [0.6, 0.5] [0.8, 0.7] [1.0, 0.8] [1.0, 1.0]
    '''
    print "\n 进入 create_VM() 方法"

    vm = {'rp':0, 'rm':0}
    for i in xrange(len(vm_option)):
        if vm_option[i][0] >= c_rp and vm_option[i][1] >= c_rm:
            vm['rp'], vm['rm'] = vm_option[i][0], vm_option[i][1]
            break
    return vm

def map_v2h(bins, size=0):
    '''
    将popu1中'population'字段中第size个解转为vm：hm的字典映射
    '''
    map_v_h = dict(bins['population'][size])
    return map_v_h

def weightVMBins_FFDSum(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    print "\n 进入weightVMBins_FFDSum() 方法"

    weightedVMBins = {}
    for j in xrange(len(bins['v_p_cost'][0])):
        bin_reservedCPU = bins['v_rp'][j] - bins['v_p_cost'][0][j]
        bin_reservedMEM = bins['v_rm'][j] - bins['v_m_cost'][0][j]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
            continue
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
            cpuScore = (bins['v_p_cost'][0][j] + object_CPU) * 100 / bins['v_rp'][j]
        if object_MEM > 0:
            memScore = (bins['v_m_cost'][0][j] + object_MEM) * 100 / bins['v_rm'][j]
        if cpuScore <= 100 and memScore <= 100:
            weightedVMBins.setdefault(j, cpuScore+memScore)
    return weightedVMBins

def weightHMBins_FFDSum(bins, object_CPU, object_MEM):
    '''
    计算集群bins(HMs)中所有bin的权重，并返回weightedHMBins记录有各个node(HM)得分的weightedHMBins
    '''
    print "\n 进入weightHMBins_FFDSum() 方法"

    weightedHMBins = {}
    for j in xrange(len(bins['h_p_cost'][0])):
        bin_reservedCPU = 1.0 - bins['h_p_cost'][0][j]
        bin_reservedMEM = 1.0 - bins['h_m_cost'][0][j]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
            continue
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
            cpuScore = (bins['h_p_cost'][0][j] + object_CPU) * 100 / 1.0
        if object_MEM > 0:
            memScore = (bins['h_m_cost'][0][j] + object_MEM) * 100 / 1.0
        if cpuScore <= 100 and memScore <= 100:
            weightedHMBins.setdefault(j, cpuScore+memScore)
    return weightedHMBins

def weightVMBins_DotProd(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin reserved vector(非capacity vector)与object(docker) vector数量积，
    此处为了更为精细选用 2 vector的cos值最大，说明 2 vector之间夹角越小，对资源的牺牲度更为均衡。
    并返回weightedVMBins记录有各个node(VM) cos值得分的weightedVMBins
    '''
    print "\n 进入weightVMBins_DotProd() 方法"

    weightedVMBins = {}
    for j in xrange(len(bins['v_p_cost'][0])):
        bin_reservedCPU = bins['v_rp'][j] - bins['v_p_cost'][0][j]
        bin_reservedMEM = bins['v_rm'][j] - bins['v_m_cost'][0][j]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
            continue
        cosScore = 1          # 即夹角最小0度
        if object_CPU > 0 and object_MEM > 0:
            # 2 vector数量积
            dotproduct = float(object_CPU * bin_reservedCPU + object_MEM * bin_reservedMEM)
            # object向量的模
            norm_object = object_CPU**2 + object_MEM**2
            # bin_reserved_resources向量的模
            norm_bin = bin_reservedCPU**2 + bin_reservedMEM**2
            # bins cos得分
            cosScore = dotproduct / math.sqrt(norm_object*norm_bin)
        if cosScore <= 1:
            weightedVMBins.setdefault(j, cosScore)
    return weightedVMBins


def weightHMBins_DotProd(bins, object_CPU, object_MEM):
    '''
    计算集群bins(HMs)中所有bin reserved vector(非capacity vector)与object(VM) vector数量积，
    此处为了更为精细选用 2 vector的cos值最大，说明 2 vector之间夹角越小，对资源的牺牲度更为均衡。
    并返回weightedHMBins记录有各个node(HM) cos值得分的weightedHMBins
    '''
    print "\n 进入weightHMBins_DotProd() 方法"

    weightedHMBins = {}
    for j in xrange(len(bins['h_p_cost'][0])):
        bin_reservedCPU = 1.0 - bins['h_p_cost'][0][j]
        bin_reservedMEM = 1.0 - bins['h_m_cost'][0][j]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
            continue
        cosScore = 1       # 即最大值，夹角为0度
        if object_CPU > 0 and object_MEM > 0:
            # 2 vector数量积
            dotproduct = float(object_CPU * bin_reservedCPU + object_MEM * bin_reservedMEM)
            # object向量的模
            norm_object = object_CPU**2 + object_MEM**2
            # bin_reserved_resources向量的模
            norm_bin = bin_reservedCPU**2 + bin_reservedMEM**2
            # bins cos得分
            cosScore = dotproduct / math.sqrt(norm_object*norm_bin)
        if cosScore <= 1:
            weightedHMBins.setdefault(j, cosScore)
    return weightedHMBins


def compute_costs(bins, size=1):
    '''
    计算bins中前size个方案对应的能耗、负载均衡方差代价值，由于新增阶段不涉及VM内存迁移，所以不考虑迁移时间
    power_cost、v_balance_cost、h_balance_cost
    以集群环境中所有running VMs/HMs作为计算对象（）
    '''
    print "进入能耗、负载方差计算"
    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'power_cost': 0.0,
        'v_balance_cost': 0.0,
        'v_average_load_index': 0.0,
        'h_balance_cost': 0.0,
        'h_average_load_index': 0.0,
        'used_vms': 0,
        'used_hms': 0,
        'used_time': 0.0
        }
    map_v_p = map_v2h(bins)
    used_vms = map_v_p.keys()
    used_hms = list(set(map_v_p.values()))
    

    # Then, 对bins中前size个方案计算代价值（在新增算法中，size只有0一种值）
    for i in xrange(size):
        h_load_index = []      # 各HM的负载均衡指数
        v_load_index = []      # 各VM的负载均衡指数

        # 计算总能耗及各running VM/HM负载均衡指数
        tmp0, tmp1 = len(used_vms), len(used_hms)
        cost['used_vms'] = tmp0
        cost['used_hms'] = tmp1
        while tmp0 > 0 or tmp1 > 0:
            if tmp0 > 0:
                v = used_vms[tmp0 - 1]
                index = 1.0 / (1.0005 - bins['v_p_cost'][i][v]) / (1.0005 - bins['v_m_cost'][i][v])
                v_load_index.append(index)
                tmp0 -= 1
            if tmp1 > 0:
                h = used_hms[tmp1 - 1]
                x = bins['h_p_cost'][i][h]
                # 能耗计算依据之前模拟的立方多项式模型
                cost['power_cost'] += 446.7 + 5.28*x - 0.04747*x**2 + 0.000334*x**3
                index = 1.0 / (1.0005 - bins['h_p_cost'][i][h]) / (1.0005 - bins['h_m_cost'][i][h])
                h_load_index.append(index)
                tmp1 -= 1

        
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

    # print 'cost={}'.format(cost)
    return cost

def compositive_func(bins, objects, s0, handle0, handle1):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    '''

    # print " \n进入 Dot_product() 方法"
    print " \n进入 {} 方法".format(s0)


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM计算向量间夹角余弦值，值最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM计算与VM向量间夹角余弦值，值最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = handle0(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = find_HM(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix, handle1)

                # 更新放入该object（容器）造成的bin（VM）资源变化
                bins['v_p_cost'][0][vm_suffix] += object_CPU
                bins['v_m_cost'][0][vm_suffix] += object_MEM
                
                # 将容器及其放置位置加入‘population’中
                bins['population'][0].append([vm_suffix, hm_suffix])
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)

                # 已经解决掉一个object
                i -= 1 
                continue
                
            # 否则，当前集群没有能容纳该object（容器）的bin（VM）
            else:
                # 随机生成一个足以容纳该容器的VM, 获取编号
                # vm = create_VM(object_CPU, object_MEM, rp_option, rm_option)
                vm = create_VM(object_CPU, object_MEM, vm_option)
                vm_suffix = len(bins['v_p_cost'][0])

                # 为该VM找寻HM,并更新HM资源变动及map_v_h
                hm_suffix = find_HM(bins, vm['rp'], vm['rm'], vm_suffix, handle1)

                # 更新放入容器后造成的VM资源变化
                bins['v_p_cost'][0].append(object_CPU)
                bins['v_m_cost'][0].append(object_MEM)

                # 追加系统容器、vm数量及资源分布
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)
                bins['v_rp'].append(vm['rp'])
                bins['v_rm'].append(vm['rm'])

                # 更新‘population’、‘map_v_h’
                bins['population'][0].append([vm_suffix, hm_suffix])

                # 已经解决掉一个object
                i -= 1
                continue

    # 说明性数据统计
    num = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "{} used time is {} \n used the number of HMs is {}".format(s0, used_time, len(num))
    return (bins, used_time)


if __name__ == '__main__':

    # 一、 1. 设置可选的虚机尺寸
    vm_option = [(0.3, 0.3), (0.5, 0.4), (0.6, 0.5), (0.8, 0.7), (1.0, 0.8), (1.0, 1.0)]

    # 初始集群状态及新增序列，test1
    # init_popu = {
    #     'c_rp': [0.4697016305356679, 0.29431926378647033, 0.22970477648767457, 0.32036803645328127, 0.4811686577824706, 0.39630054137437853, 0.1609631404578878, 0.2755880033213779, 0.38151011814458446, 0.023876102751119344],
    #     'c_rm': [0.280698996006043, 0.3440203847852634, 0.00011105303698105695, 0.2985981849500239, 0.4261539194747088, 0.333748152269725, 0.20113407453783236, 0.3387976831408542,0.45844925092062805, 0.07975242436510899],
    #     'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'population': [[[0, 9], [2, 3], [7, 8], [0, 9], [1, 2], [2, 3], [1, 2], [4, 7], [6, 0], [7, 8]]],
    #     'v_p_cost': [[0.7900696669889491, 0.6421317982403584, 0.6906198051608489, 0, 0.2755880033213779, 0, 0.38151011814458446, 0.2535808792387939, 0, 0]],
    #     'v_m_cost': [[0.5792971809560669, 0.6272879940125412, 0.6777685370549884, 0, 0.3387976831408542, 0, 0.45844925092062805, 0.07986347740209004, 0, 0]],
    #     'h_p_cost': [[1.0, 0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 1.0]],
    #     'h_m_cost': [[1.0, 0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 1.0]],
    #     'map_v_h': {0: 9, 1: 2, 2: 3, 4: 7, 6: 0, 7: 8}
    #     }
    # addtion0 = {
    #     'c_rp': [0.2534765051859606, 0.2948935628141042, 0.2224244890668316, 0.18127979201839872, 0.32156802827499703],
    #     'c_rm': [0.3020445793942861, 0.3768727547924075, 0.006082192833673228, 0.15746276310264423, 0.39400382229512343],
    #     'replicas': [4, 0, 4, 3, 0]
    # }

    # 二、 循环计算不同初始集群下，各算法表现出来代价指标
    cycle = [50]*5 + [100]*5 + [200]*5 + [300]*5 + [500]*5 + [800]*5 + [1000]*5 + [3000]*5 + [5000]*5 + [8000]*5 + [10000]*5
    for i in cycle:
        # 2. 初始化集群状态及新增序列，计算初始集群的各项指标代价，并深拷贝一份作为第二个算法实参
        init_popu0, addtion0 = main_init(100, 1.0, i)
        init_popu1 = copy.deepcopy(init_popu0)
        init_cost = compute_costs(init_popu0)
        # s0 = 'Start: \nThe initial Bins = {} \n\n\n The initial cost = {}\n'.format(init_popu0 ,init_cost)
        s0 = 'Start: \nWhen len(addtion0) = {},\nThe initial cost = {}\n'.format(i, init_cost)

        # 3. 分别在两个相同集群状态上执行调度算法，并分别计算最终集群的各项代价
        bins0, used_time0 = compositive_func(init_popu0, addtion0, 'FFDSum()', weightVMBins_FFDSum, weightHMBins_FFDSum)
        bins1, used_time1 = compositive_func(init_popu1, addtion0, 'Dot-Prod()', weightVMBins_DotProd, weightHMBins_DotProd)
        cost0, cost1 = compute_costs(bins0), compute_costs(bins1)
        cost0['used_time'], cost1['used_time'] = used_time0, used_time1
        
        # 4. 存档记录（s2记录比较详细，用来检验算法运行正确性）
        # s2 = '\n\n\nEnd:\n\n\nThe FFDSum cost of new state = {}\n\nThe FFDSum_Bins = {}  \
        # \n\n\nThe Dot-prod cost of new state = {}\n\nThe Dot-Prod_Bins = {} '.format(cost0, bins0, cost1, bins1)
        s1 = '\n\n\nEnd:\n\n\nThe FFDSum cost of new state = {}\n\n\nThe Dot-prod cost of new state = {}\n\n'.format(cost0, cost1)
        
        # print s0,s1
        with open('addtion_phase//tmp.py','a') as f:
            f.flush()
            f.write(s0)
            f.write(s1)
