#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-28
@Author : Amy
Goal : used FFDSum for container consolidation phase
Digest : 模拟将当前集群的所有容器全部拿出，按照启发式算法打分模式对所有容器重新放入VM（此处暂时认为VM不动）
         此处打分考虑powerScore、balanceScore 2种分值之和作为总打分。
         powerScore即放入容器后各位资源使用率最大化
         balanceScore即计算类似dot-prod的求夹角余弦最大值
更新 2017-11-30 15:40 pm临时决定将启发式打分方式更新为更能够负载均衡的dot-product方式，主要用于weightVMBins、weightHMBins方法中
因此实验设计:
      1. 在d-v-h架构下，仅用FFDSum对docker层进行聚合 VS 使用FFDSum同时聚合docker层和VM层；
      2. 在d-v-h下，仅用mbbo对vm层进行聚合 VS 使用mbbo同时对docker、vm层随机求解聚合；
      3. 在d-v-h下，比对同时以docker、vm作为调度单位时的FFDSum、Mbbo、GA算法等的聚合效果；

'''


import time
import random
import math
import copy
import sys
import addtion_phase.init as init
import addtion_phase.Contrast as Contrast
import addtion_phase.Contrast_with_safe as tolerance




# rp_option = [0.5]                      # vm可选的cpu尺寸
# rm_option = [0.5]                      # vm可选的mem尺寸
vm_option = [(0.3, 0.3), (0.5, 0.4), (0.6, 0.5), (0.8, 0.7), (1.0, 0.8), (1.0, 1.0)]
               

def FFDSum_Consol(bins):
    '''
    @param: bins 代表当前系统状态
    @return: 聚合容器后的集群bins状态
    '''

    # print " \n进入 FFDSum_Consol() 方法" 


    time0 = time.time()

    # d-v-h架构下聚合算法大致如此，由于docker迁移无状态的并不涉及到mem迁移而引起迁移时间，所以：
    # 1. 对当前集群状态中所有容器进行重新调度（仅在running的VMs上进行），
    #    目标为尽量减少running VMs数量（简介使得第二步减少整体running HMs的能耗）能耗以及VMs负载均衡均值及方差；
    # 2. 对于完全布置好的所有running VMs实行VMs聚合算法（即对于所有runnig VMs整体迁移，使得整体能耗降低），
    #    此处HMs选取的打分设计，可分为2种：仅考虑能耗、能耗+负载指数。

    # 将集群中所有容器拿出来当作所有需要重新安排放入的objects
    # 集群running VMs/HMs, 并清空所有v_p/m_cost、population
    running_vms = bins['map_v_h'].keys()
    bins['v_p_cost'][0] = [0.0] * len(bins['v_p_cost'][0])
    bins['v_m_cost'][0] = [0.0] * len(bins['v_p_cost'][0])
    bins['population'][0] = [[0, 0] for i in xrange(len(bins['c_rp']))]

    # 循环为所有容器重新安排vms映射
    for x in xrange(len(bins['c_rp'])):
        object_CPU, object_MEM, flag = bins['c_rp'][x], bins['c_rm'][x], True
        
        while flag:
            # 仅对该object(容器)计算running_vms bins（VMs）得分
            weightedVMBins = weightVMBins_FFDSum(bins, running_vms, object_CPU, object_MEM)

            # 由于是聚合阶段，所有当前running VMs必定能够容纳下所有容器，最坏情况也仅是维持原始状态
            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 仅对running_vms进行打分选择，故该VM必然已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 更新放入该object（容器）造成的bin（VM）资源变化
                bins['v_p_cost'][0][vm_suffix] += object_CPU
                bins['v_m_cost'][0][vm_suffix] += object_MEM
                
                # 更新容器在population的新d-v-h映射，并对已经安排好的容器在objects标记为-1
                bins['population'][0][x] = [vm_suffix, -1]
                # 已经解决掉一个object
                flag = False 
    
    # 循环为安排完所有容器的VMs聚合安排HMs
    # 选择所有v_p/m_cost均非0的VMs作为需要重新安排放入的objects（running_vms）
    running_vms = []
    for i in xrange(len(bins['v_p_cost'][0])):
        if bins['v_p_cost'][0][i] != 0.0 or bins['v_m_cost'][0][i] != 0.0:
            running_vms.append(i)

    # 集群running VMs/HMs, 并清空所有h_p/m_cost、bins['map_v_h']
    running_hms = set(bins['map_v_h'].values())
    bins['h_p_cost'][0] = [0.0] * len(bins['h_p_cost'][0])
    bins['h_m_cost'][0] = [0.0] * len(bins['h_p_cost'][0])
    bins['map_v_h'] = {}


    # 循环为所有running vms重新安排hms映射
    for x in running_vms:
        object_CPU, object_MEM, flag = bins['v_rp'][x], bins['v_rm'][x], True
        
        while flag:
            # 仅对该object(vm)计算running_hms bins（HMs）得分
            weightedHMBins = weightHMBins_FFDSum(bins, running_hms, object_CPU, object_MEM)

            # 由于是聚合阶段，所有当前running hms必定能够容纳下所有vms，最坏情况也仅是维持原始状态
            # 至少有hm可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                hm_suffix = max(weightedHMBins, key=weightedHMBins.get)

                # 记录为该VM选择的HM
                bins['map_v_h'][x] = hm_suffix

                # 更新放入该object（vm）造成的bin（HM）资源变化
                bins['h_p_cost'][0][hm_suffix] += object_CPU
                bins['h_m_cost'][0][hm_suffix] += object_MEM
                flag = False 

    # 整体安排完毕后更新population
    for i in xrange(len(bins['population'][0])):
        v, h = bins['population'][0][i]
        if h == -1:
            bins['population'][0][i] = [v, bins['map_v_h'][v]]

    # 说明性数据统计
    used_hms = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "FFDSum coslidation used time is {} \n used the number of HMs is {}".format(used_time, len(used_hms))
    return bins

def weightVMBins_FFDSum(bins, running_vms, object_CPU, object_MEM):
    '''
    计算集群bins runnin_vms 中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    # print "\n 进入weightVMBins_FFDSum() 方法"

    weightedVMBins = {}
    for v in running_vms:
        bin_reservedCPU = bins['v_rp'][v] - bins['v_p_cost'][0][v]
        bin_reservedMEM = bins['v_rm'][v] - bins['v_m_cost'][0][v]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
                continue
        # Dot-Prod(不加权求夹角余弦值)更偏向于负载均衡的方式
        # cosScore = 1
        # if object_CPU > 0 and object_MEM > 0:
        #         # 2 vector数量积
        #         dotproduct = float(object_CPU * bin_reservedCPU + object_MEM * bin_reservedMEM)
        #         # object向量的模
        #         norm_object = object_CPU**2 + object_MEM**2
        #         # bin_reserved_resources向量的模
        #         norm_bin = bin_reservedCPU**2 + bin_reservedMEM**2
        #         # bins cos得分
        #         cosScore = dotproduct / math.sqrt(norm_object*norm_bin)
        # if cosScore <= 1:
        #         weightedVMBins.setdefault(v, cosScore)

        # FFDSum求权重的打分方式
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
                cpuScore = (bins['v_p_cost'][0][v] + object_CPU) * 100 / bins['v_rp'][v]
        if object_MEM > 0:
                memScore = (bins['v_m_cost'][0][v] + object_MEM) * 100 / bins['v_rm'][v]
        if cpuScore <= 100 and memScore <= 100:
                weightedVMBins.setdefault(v, cpuScore+memScore)
    return weightedVMBins

def weightHMBins_FFDSum(bins, running_hms, object_CPU, object_MEM):
    '''
    计算集群running bins(HMs)中所有bin的权重，并返回weightedHMBins记录有各个node(HM)得分的weightedHMBins
    '''
    # print "\n 进入weightHMBins_FFDSum() 方法"

    weightedHMBins = {}
    for h in running_hms:
        bin_reservedCPU = 1.0 - bins['h_p_cost'][0][h]
        bin_reservedMEM = 1.0 - bins['h_m_cost'][0][h]
        if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
            continue
        # Dot-Prod(不加权求夹角余弦值)更偏向于负载均衡的方式
        cosScore = 1       # 即最大值，夹角为0度
        # if object_CPU > 0 and object_MEM > 0:
        #     # 2 vector数量积
        #     dotproduct = float(object_CPU * bin_reservedCPU + object_MEM * bin_reservedMEM)
        #     # object向量的模
        #     norm_object = object_CPU**2 + object_MEM**2
        #     # bin_reserved_resources向量的模
        #     norm_bin = bin_reservedCPU**2 + bin_reservedMEM**2
        #     # bins cos得分
        #     cosScore = dotproduct / math.sqrt(norm_object*norm_bin)
        # if cosScore <= 1.0:
        #     weightedHMBins.setdefault(h, cosScore)

        # FFDSum求权重的打分方式
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
            cpuScore = (bins['h_p_cost'][0][h] + object_CPU) * 100 / 1.0
        if object_MEM > 0:
            memScore = (bins['h_m_cost'][0][h] + object_MEM) * 100 / 1.0
        if cpuScore <= 100 and memScore <= 100:
            weightedHMBins.setdefault(h, cpuScore+memScore)
    return weightedHMBins

def map_v2h(bins, size=0):
    '''
    将popu1中'population'字段中第size个解转为vm：hm的字典映射
    '''
    map_v_h = dict(bins['population'][size])
    return map_v_h

def compute_costs(bins, size=1):
    '''
    计算bins中前size个方案对应的能耗、负载均衡方差代价值，由于新增阶段不涉及VM内存迁移，所以不考虑迁移时间
    power_cost、v_balance_cost、h_balance_cost
    以集群环境中所有running VMs/HMs作为计算对象（）
    '''
    # print "进入能耗、负载方差计算"
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

    return cost

def consolidation_cost(bins, size=1):
    '''
    仅计算聚合放置的优化目标，即能耗与资源碎片化指数与容错能力
    以集群环境中所有running VMs/HMs作为计算对象（）
    '''
    # print "进入能耗、负载方差计算"
    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'degree_of_concentration': 0.0,
        'power_cost': 0.0,
        'used_hms': 0,
        'tolerance': 0.0
        }

    map_h_v = map_h2v(bins)
    map_v_p = map_v2h(bins)
    used_vms = map_v_p.keys()
    used_hms = list(set(map_v_p.values()))
    

    # Then, 对bins中前size个方案计算代价值（在新增算法中，size只有0一种值）
    for i in xrange(size):
        utilization = 0

        # 计算总能耗及各running VM/HM负载均衡指数
        tmp0, tmp1 = len(used_vms), len(used_hms)
        cost['used_hms'] = tmp1
        while tmp0 > 0 or tmp1 > 0:
            if tmp1 > 0:
                h = used_hms[tmp1 - 1]   
                # 以docker作为实际负载进行代价计算
                true_load_cpu = sum([bins['v_p_cost'][i][v] for v in map_h_v[h]])
                true_load_mem = sum([bins['v_m_cost'][i][v] for v in map_h_v[h]])
                # 计算集群剩余资源量即各HM节点cpu、mem余量之乘积，所有active HM求和
                utilization += (1.0 - true_load_cpu) * (1.0 - true_load_mem)
                cost['power_cost'] += 446.7 + 5.28*true_load_cpu - 0.04747*true_load_cpu**2 + 0.000334*true_load_cpu**3
                tmp1 -= 1
        cost['degree_of_concentration'] = 100 * cost['used_hms'] - 13 * utilization

        # 计算VM迁移时间（仅聚合阶段）
        pass

        # 模拟宕机计算容错  (没写完)
        # cost['tolerance'] = tolerance.simulate_crash_HM(p_crash, max_suffix, bins, addtion0, map_d_s)
    return cost

def create_JSON(data, scale, degree_of_concentration, power_cost, tolerance, used_hms):
    '''
    将计算代价结果追加至data中便于后期记录文件
    '''
    data['scale'].append(scale)
    data['degree_of_concentration'].append(degree_of_concentration)
    data['power_cost'].append(power_cost)
    data['tolerance'].append(tolerance)
    data['used_hms'].append(used_hms)
    return data

if __name__ == '__main__':
    '''
    本模块测试算法是否运行正确
    '''
    # 由addtion_phase/init 模块main_init方法生成初始
    init_popu = init.main_init(100, 1.0)
    scale = len(init_popu['c_rp'])
    cycle = [100, 300, 500, 700, 900, 1300, 1500, 1700, 1900, 2100, 2300]
    count = 0  # 每增量放置3批，进行一次聚合
    data = {
        'scale' : [],
        'degree_of_concentration':[],
        'tolerance': [],
        'power_cost': [],
        'used_hms': []
    }
    # 记录初始代价
    cost0 = consolidation_costs(init_popu)
    data = create_JSON(data, scale, cost0['degree_of_concentration'], cost0['power_cost'], cost0['tolerance'], cost0['used_hms'])

    for scale in cycle:
        count += 1
        # 生成增量
        addtion0 = init.create_addtion(1.0, scale)

        # 首先进行增量批放置
        init_popu = Contrast.FFDSum_simple(init_popu, addtion0)
        scale += sum(addtion0['replicas'])
        cost1 = consolidation_costs(init_popu)
        data = create_JSON(data, scale, cost1['degree_of_concentration'], cost1['power_cost'], cost1['tolerance'], cost1['used_hms'])
        
        # 增量放置3次进行聚合
        if count == 3:
            count = 0  
            init_popu = FFDSum_Consol(init_popu)
            cost2 = consolidation_costs(init_popu)
            data = create_JSON(data, scale, cost2['degree_of_concentration'], cost2['power_cost'], cost2['tolerance'], cost2['used_hms'])
        

    with open('.//viz//consolidation-no-safe-{}-demo.json'.format(datetime.datetime.now()),'w') as f:
        f.flush()
        json.dump(data, f, indent=2)

