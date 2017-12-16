#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-12-11
@Author : Amy
Goal : 分别以VM，docker作为真正的负载，对比同时使用FFDSum时，最终结果
Digest : 分别定义2种FFDSum算法：
      一种在新容器到来时，模拟openstack向swarm提供当前VMs尺寸，由swarm自行选择放入，若无新的VM，则由openstack新建，并返回（v,h）给容器层；
      另一种则由swarm进行全局资源的管控，以docker作为真正的负载，首先针对各个HM打分再以其上各个VM打分，若要新建VM则以打分放入；
'''


import time
import random
import math
import copy
import collections



# 其中vm_option以资源降序排列
vm_option = [(1.0, 1.0), (1.0, 0.8), (0.8, 0.7), (0.6, 0.5), (0.5, 0.4), (0.3, 0.3)]

# rp_option = [0.5, 1.0]                      # vm可选的cpu尺寸
# rm_option = [0.5, 1.0]                      # vm可选的mem尺寸
               

def FFDSum_complex(bins, objects):
    '''
    面向降能耗，以docker作为实际负载考虑的新增放置策略
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    @note:  此算法进行HMs、VMs打分
    '''

    print " \n进入 FFDSum_complex() 方法" 
    time0 = time.time()

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算active bins（VMs）的得分，仅针对used VMs
            weightedVMBins = weightVMBins_complex(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，程序有问题
                else:
                    print "出错了，竟然使用中的VM没有对应的HM，程序将中止"
                    sys.exit()

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
                
            # 否则，集群已没有能容纳该object（容器）的bin（VM）
            else:
                flag = find_HM_complex(bins, object_CPU, object_MEM, vm_option)
                
                # 代表active HMs中有HM可以容纳能够放入该容器的最小VM
                if flag:
                    hm_suffix, min_vm = flag
                    vm_suffix = len(bins['v_p_cost'][0])

                    # 更新放入容器后造成的VM、HM资源变化
                    bins['v_p_cost'][0].append(object_CPU)
                    bins['v_m_cost'][0].append(object_MEM)
                    bins['h_p_cost'][0][hm_suffix] += min_vm[0]
                    bins['h_m_cost'][0][hm_suffix] += min_vm[1]

                    # 追加系统容器、vm数量及资源分布
                    bins['c_rp'].append(object_CPU)
                    bins['c_rm'].append(object_MEM)
                    bins['v_rp'].append(min_vm[0])
                    bins['v_rm'].append(min_vm[1])

                    # 更新‘population’、‘map_v_h’
                    bins['population'][0].append([vm_suffix, hm_suffix])
                    bins['map_v_h'][vm_suffix] = hm_suffix

                    # 已经解决掉一个object
                    i -= 1
                    continue


                # 若所有active HMs均不满足，则新建HM并新建VM，（所建VM规格先不加以控制）
                if not flag:
                    # 创建最大VM
                    vm = create_VM(object_CPU, object_MEM,vm_option)
                    vm_suffix = len(bins['v_p_cost'][0])
                    hm_suffix = len(bins['h_m_cost'][0])

                    # 更新放入容器后造成的VM、HM资源变化
                    bins['v_p_cost'][0].append(object_CPU)
                    bins['v_m_cost'][0].append(object_MEM)
                    bins['h_p_cost'][0].append(vm['rp'])
                    bins['h_m_cost'][0].append(vm['rm'])

                    # 追加系统容器、vm数量及资源分布
                    bins['c_rp'].append(object_CPU)
                    bins['c_rm'].append(object_MEM)
                    bins['v_rp'].append(vm['rp'])
                    bins['v_rm'].append(vm['rm'])

                    # 更新‘population’、‘map_v_h’
                    bins['population'][0].append([vm_suffix, hm_suffix])
                    bins['map_v_h'][vm_suffix] = hm_suffix

                    # 已经解决掉一个object
                    i -= 1
                    continue

    # 说明性数据统计
    num = set(bins['map_v_h'].values())
    time1 = time.time()
    print "Complex used time is {} \n used the number of HMs is {}".format(time1-time0, len(num))
    return bins

def FFDSum_simple(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    @note:  此算法仅进行VMs打分
    '''

    print " \n进入 FFDSum_simple() 方法" 


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM打分，分最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM打分，分最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = weightVMBins_simple(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = find_HM_simple(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix)

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
                vm = create_VM_random(object_CPU, object_MEM, vm_option)
                vm_suffix = len(bins['v_p_cost'][0])

                # 为该VM找寻HM,并更新HM资源变动及map_v_h
                hm_suffix = find_HM_simple(bins, vm['rp'], vm['rm'], vm_suffix)

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
    time1 = time.time()
    print "Simple used time is {} \n used the number of HMs is {}".format(time1-time0, len(num))
    return bins

def weightVMBins_simple(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    print "\n 进入weightVMBins_simple() 方法"

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

def weightVMBins_complex(bins, object_CPU, object_MEM):
    '''
    以最大化使用VM资源为目标，以docker作为实际负载考虑，引入基于打分机制的FFDSum算法，
    对各个VM计算放入object引起的资源占比与hosted HM引起的资源占比之和。
    CPU得分sum(reservedCPU/v_rp*100)
    MEM得分sum(reservedMEM/v_rm*100)
    '''
    print "\n 进入weightVMBins_complex() 方法"

    # 转换map_v_h为map_h_v
    map_h_v = map_h2v(bins)
    weightedVMBins = {}
    # 以active hm:vm的映射开始，其中vm为list
    for h, v in map_h_v.items():
        # 拿到每个HM实际运行的所有docker产生的负载
        true_hm_cpu = sum([bins['v_p_cost'][0][i] for i in v])
        true_hm_mem = sum([bins['v_m_cost'][0][i] for i in v])
        # 对每个active hm上的active vm进行打分
        for j in v:
            bin_reservedCPU = bins['v_rp'][j] - bins['v_p_cost'][0][j]
            bin_reservedMEM = bins['v_rm'][j] - bins['v_m_cost'][0][j]
            # 若物理机h上的每一个vm均无法容纳该容器，则该h要么还可以新建VM，要么该h已不能承载任何新VM（在主程序中处理）
            if bin_reservedCPU < object_CPU or bin_reservedMEM < object_MEM:
                    continue
            cpuScore = 100
            memScore = 100
            hmScore = 200

            if object_CPU > 0:
                cpuScore = (bins['v_p_cost'][0][j] + object_CPU) * 100 / bins['v_rp'][j]
                hmScore = (true_hm_cpu + object_CPU) * 100 / 1.0
            if object_MEM > 0:
                memScore = (bins['v_m_cost'][0][j] + object_MEM) * 100 / bins['v_rm'][j]
                hmScore += (true_hm_mem + object_MEM) * 100 / 1.0
            if cpuScore <= 100 and memScore <= 100 and hmScore <= 200:
                weightedVMBins.setdefault(j, cpuScore+memScore+hmScore)
    return weightedVMBins

def find_HM_complex(bins, c_rp, c_rm, vm_option):
    '''
    在集群当前active HMs中，
    1. 能够容纳该容器(c_rp, c_rm)的最小VM；
    2. 能够容纳该最小VM的所有active HMs，依据实际容器当作负载时资源占比进行打分；
    3. 分高者即满足约束且最为合适的方案，并对其剩余VM可申请资源全部分配，若无则需新引入HM。
    '''
    print '\n进入 find_HM_complex() 方法'

    min_vm = []
    map_h_v = map_h2v(bins)
    weightedHMBins = {}
    # 能够容纳容器(c_rp, c_rm)的最小VM
    for c, m in vm_option[::-1]:
        if c_rp <= c and c_rm <= m:
            min_vm = [c,m]
            break

    # 挑选能够容纳最小VM的所有active HMs
    # 对挑选出来的active HMs，以容器为实际负载进行资源占比打分
    # 首先判断哪些active HMs还能容纳完整VMs
    for h, v in map_h_v.items():
        reservedCPU = 1.0 - bins['h_p_cost'][0][h]
        reservedMEM = 1.0 - bins['h_m_cost'][0][h]
        if reservedCPU < min_vm[0] or reservedMEM < min_vm[-1]:
            continue
        true_reservedCPU = 1.0 - sum([ bins['v_p_cost'][0][i] for i in v])
        true_reservedMEM = 1.0 - sum([ bins['v_m_cost'][0][i] for i in v])
        if c_rm > 0 and c_rp > 0:
            hmScore = (true_reservedCPU + c_rp) * 100 / 1.0 + (true_reservedMEM + c_rm) * 100 / 1.0
        if hmScore <= 200:
            weightedHMBins.setdefault(h, hmScore)
        
        # 将最小VM换为最大VM，该HM可容纳的最大VM
        for c, m in vm_option:
            if reservedCPU <= c and reservedMEM <= m:
                min_vm = [c,m]

    # 分最高者hm作为容纳新VM的主机，若无满足hm则在主程序中统一起用新HM，创建新VM（控制VM创建规模暂不考虑）
    if len(weightedHMBins) > 0:
        hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
        return (hm_suffix, min_vm)
    else:
        return False

def find_HM_simple(bins, v_rp, v_rm, vm_suffix):
    '''
    为VM找寻可容纳其的HM标号(系统已有/新增)，并更新所引起的hm资源编号，及map_v_h
    '''
    print '\n进入 find_HM_simple() 方法'
    # 找到可满足资源约束的第一个HM
    hm_suffix = -1
    for j in xrange(len(bins['h_p_cost'][0])):
        bin_reservedCPU = 1.0 - bins['h_p_cost'][0][j]
        bin_reservedMEM = 1.0 - bins['h_m_cost'][0][j]
        if bin_reservedCPU >= v_rp and bin_reservedMEM >= v_rm:
            hm_suffix = j
            break

    # 更新得分最高的HM资源
    if hm_suffix != -1:
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

def create_VM_abs_random(c_rp, c_rm, rp_option, rm_option):
    '''
    依据实验可选的VM尺寸(rp_option、rm_option)随机生成可以容纳(c_rp、c_rm)的VM
    '''
    print "\n 进入 create_VM() 方法"

    vm = {'rp':0, 'rm':0}
    while vm['rp'] == 0:
        rp = random.choice(rp_option)
        rm = random.choice(rm_option)
        if rp >= c_rp and rm >= c_rm:
            vm['rp'],vm['rm'] = rp,rm
    return vm

def create_VM_random(c_rp, c_rm, vm_option):
    '''
    从vm_option中随机挑选满足约束的VM
    '''
    print "\n 进入 create_VM() 方法"
    # 部分随机的创建任意大小能够容纳该容器的vm
    vm = {'rp':0, 'rm':0}
    # 这种方法总是选择最大者放入
    # for i in xrange(len(vm_option)):
    #     if vm_option[i][0] >= c_rp and vm_option[i][1] >= c_rm:
    #         vm['rp'], vm['rm'] = vm_option[i][0], vm_option[i][1]
    #         break
    while vm['rp'] == 0:
        i = random.randint(0, len(vm_option)-1)
        if vm_option[i][0] >= c_rp and vm_option[i][0] >= c_rm:
            vm['rp'], vm['rm'] = vm_option[i][0], vm_option[i][1]
            break
    return vm

def create_VM(c_rp, c_rm, vm_option):
    '''
    从按照资源降序排列的vm_option中挑选满足约束条件的VM
    约束1： 该VM能够容纳容器（c_rp, c_rm）
    约束2： 不超过HM最大可申请资源（1.0, 1.0）的最大VM。
    '''
    print "\n 进入 create_VM() 方法"

    # 部分随机可容纳该容器且不会超过物理机剩余资源,vm_option中VM大小降序排列
    vm = {'rp':0, 'rm':0}
    for c, m in vm_option:
        if c <= 1.0 and m <= 1.0 and c >= c_rp and m >= c_rm:
            vm['rp'], vm['rm'] = c, m
    return vm

def map_v2h(bins, size=0):
    '''
    将popu1中'population'字段中第size个解转为vm：hm的字典映射
    '''
    map_v_h = dict(bins['population'][size])
    return map_v_h

def map_h2v(bins):
    '''
    依据bins中map_v_h，将其转为hm为key，vms list为value的字典
    '''
    # 转换map_v_h为map_h_v
    map_h_v = collections.defaultdict(list)
    for key,value in bins['map_v_h'].items():
        map_h_v[value].append(key)
    return map_h_v


def utilization_ratio_cost(bins, size=1):
    '''
    优化目标，新增场景提高各节点实际物理资源利用率，即集群中剩余资源利用率最大，减少碎片化资源
    '''   
    print "进入能耗、负载方差计算,集群剩余资源利用率"

    true_h_p = [0] * 1000
    true_h_m = [0] * 1000

    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'reserved_utilization': 0.0,
        'power_cost': 0.0,
        'v_balance_cost': 0.0,
        'v_average_load_index': 0.0,
        'h_balance_cost': 0.0,
        'h_average_load_index': 0.0,
        'used_vms': 0,
        'used_hms': 0,
        'used_time': 0.0,
        'true_h_p': true_h_p,
        'true_h_m': true_h_m

        }

    map_h_v = map_h2v(bins)
    map_v_p = map_v2h(bins)
    used_vms = map_v_p.keys()
    used_hms = list(set(map_v_p.values()))
    

    # Then, 对bins中前size个方案计算代价值（在新增算法中，size只有0一种值）
    for i in xrange(size):
        h_load_index = []      # 各HM的负载均衡指数
        v_load_index = []      # 各VM的负载均衡指数
        reserved_utilization = 0

        # 计算总能耗及各running VM/HM负载均衡指数
        tmp0, tmp1 = len(used_vms), len(used_hms)
        cost['used_vms'] = tmp0
        cost['used_hms'] = tmp1
        while tmp0 > 0 or tmp1 > 0:
            if tmp0 > 0:
                v = used_vms[tmp0 - 1]
                # 用VM配置尺寸与容器实际占用进行计算
                index = 1.0 / (bins['v_rp'][v] - bins['v_p_cost'][i][v] + 0.0005) / (bins['v_rm'][v] - bins['v_m_cost'][i][v] + 0.0005)
                v_load_index.append(index)
                tmp0 -= 1
            if tmp1 > 0:
                h = used_hms[tmp1 - 1]   
                # 以docker作为实际负载进行代价计算
                true_load_cpu = sum([bins['v_p_cost'][i][v] for v in map_h_v[h]])
                true_load_mem = sum([bins['v_m_cost'][i][v] for v in map_h_v[h]])
                true_h_p[h] = true_load_cpu
                true_h_m[h] = true_load_mem
                # 计算集群剩余资源量即各HM节点cpu、mem余量之乘积，所有active HM求和
                reserved_utilization += (1.0 - true_load_cpu) * (1.0 - true_load_mem)
                cost['power_cost'] += 446.7 + 5.28*true_load_cpu - 0.04747*true_load_cpu**2 + 0.000334*true_load_cpu**3
                index = 1.0 / (1.0005 - true_load_cpu) / (1.0005 - true_load_mem)
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
        cost['reserved_utilization'] = reserved_utilization

        # 计算VM迁移时间（仅聚合阶段）
        pass

    # print 'true cost={}'.format(cost)
    return cost

def compute_costs(bins, size=1):
    '''
    注意： 以HM上所有容器作为真实负载考虑
    计算bins中前size个方案对应的能耗、负载均衡方差代价值，由于新增阶段不涉及VM内存迁移，所以不考虑迁移时间
    power_cost、v_balance_cost、h_balance_cost
    以集群环境中所有active running VMs/HMs作为计算对象
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

    map_h_v = map_h2v(bins)
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
                # 用VM配置尺寸与容器实际占用进行计算
                index = 1.0 / (bins['v_rp'][v] - bins['v_p_cost'][i][v] + 0.0005) / (bins['v_rm'][v] - bins['v_m_cost'][i][v] + 0.0005)
                v_load_index.append(index)
                tmp0 -= 1
            if tmp1 > 0:
                h = used_hms[tmp1 - 1]   
                # 以docker作为实际负载进行代价计算
                true_load_cpu = sum([bins['v_p_cost'][i][v] for v in map_h_v[h]])
                true_load_mem = sum([bins['v_m_cost'][i][v] for v in map_h_v[h]])
                cost['power_cost'] += 446.7 + 5.28*true_load_cpu - 0.04747*true_load_cpu**2 + 0.000334*true_load_cpu**3
                index = 1.0 / (1.0005 - true_load_cpu) / (1.0005 - true_load_mem)
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

    # print 'true cost={}'.format(cost)
    return cost

def faked_cost(bins, size=1):
    '''
    注意： 这里负载以VM配置作为负载考虑
    计算bins中前size个方案对应的能耗、负载均衡方差代价值
    以集群环境中所有running VMs/HMs作为计算对象
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
    

    # Then, 对bins中第size方案计算代价值（在新增算法中，size只有0一种值）
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

    # print 'origin cost={}'.format(cost)
    return cost


if __name__ == '__main__':
    '''
    本模块测试算法是否运行正确
    '''
    # test 1
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

    #test2 init_main(10,1.0,50)
    # init_popu = {
    #     'c_rp': [0.49950862497815096, 0.49566299101104405, 0.19339860376391588, 0.22650079014580787, 0.4985697928665497, 0.23123095298795776, 0.08874821111583076, 0.21338379418561532, 0.19440106465844426,0.08929997048178007],
    #     'c_rm': [0.3909286789440798, 0.369809808223181, 0.00979746372201648, 0.025755088684076777, 0.33613683282363926, 0.09025060644602326, 0.03690588016174476, 0.1613365031750235, 0.1843056842347392, 0.1654617298885813],
    #     'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_p_cost': [[0.19339860376391588, 0.4985697928665497, 0.49950862497815096, 0, 0.08929997048178007, 0.3199791641037885, 0.6900640556694884, 0.22650079014580787, 0, 0.21338379418561532]],
    #     'v_m_cost': [[0.00979746372201648, 0.33613683282363926, 0.3909286789440798, 0, 0.1654617298885813, 0.12715648660776802, 0.5541154924579201, 0.025755088684076777, 0, 0.1613365031750235]],
    #     'h_p_cost': [[0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]],
    #     'h_m_cost': [[0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]],
    #     'population': [[[2, 8], [6, 4], [0, 7], [7, 5], [1, 9], [5, 6], [5, 6], [9, 3], [6, 4], [4, 1]]],
    #     'map_v_h': {0: 7, 1: 9, 2: 8, 4: 1,5: 6, 6: 4, 7: 5, 9: 3}
    #     }
    # addtion0 = {
    #     'c_rp': [0.11908248759706352, 0.2539499371680547, 0.020365365071704944, 0.3948180323801204, 0.16201211844666025, 0.09712859701028537, 0.31390062270434416, 0.3480375603464177, 0.15014449094820942, 0.04822244066927983, 0.3928791357646204, 0.032534810957771, 0.4651545189795368, 0.0474215706739573, 0.07162125780399875, 0.40903739793374416, 0.0539330604724928, 0.2355628289244136, 0.19700257808129235, 0.373566830122395, 0.17717460262217066, 0.43991572626550735, 0.37451472906275923, 0.3135592929534395,0.015668465353517125, 0.10403211142071572, 0.21390117473577447, 0.4713342566285714, 0.17040421305346137, 0.3260384854338912, 0.2244028315904087, 0.2312332531063797, 0.45247614392078866, 0.20553810157861957, 0.3064820365449853, 0.31058025758787433, 0.1650102907341277, 0.19784436750803397, 0.44271702585692496, 0.1435831818575356, 0.46550750164344235, 0.34333834380364575, 0.027396746345203393, 0.36407514538409447, 0.18766287048391472, 0.1881570123326235, 0.45031175220343606, 0.44156291337181935, 0.3881099941271592, 0.08966540806915951],
    #     'c_rm': [0.15371760989287112, 0.4727080131827223, 0.1312785397644661, 0.3148741699625581, 0.15490164061562212, 0.2188793775769965, 0.42599638018947206, 0.4296657758683523, 0.04960548585622013, 0.12163920336361042, 0.4155052522150541, 0.22584319726937863, 0.4298025137237217, 0.02073334664757892, 0.0406855119064691, 0.2899188786601343, 0.13482466565478549, 0.1381986097950461, 0.12833142672404127, 0.47013534312111604, 0.15751054415325544, 0.45265496951228257, 0.31177491087859177, 0.4547144122615391, 0.2149583781080965, 0.002010100339807669, 0.23583146593132182, 0.2668389587972696, 0.023147288153819612, 0.49235190501873116, 0.11524643818001151, 0.10224202413249506, 0.39278777898283634, 0.021373650453562182, 0.2750448545115652, 0.49570452049049685, 0.0463055590081595, 0.10080163807146658, 0.3602772552783736, 0.2452958069609209, 0.4291638547046067, 0.4994509837339639, 0.21256047037541928, 0.2802727216555664, 0.24083778776514506, 0.11761680222091694, 0.4740337239408656, 0.292596240387029, 0.37749334161166404, 0.1872898013788786],
    #     'replicas': [4, 5, 5, 0, 3, 4, 3, 4, 4, 2, 2, 2, 2, 2, 3, 3, 2, 4, 3, 2, 4, 0, 1, 5, 3, 5, 2, 2, 2, 2, 5, 3, 3, 2, 4, 0, 1, 1, 4, 0, 1, 4, 1, 1, 5, 4, 5, 1, 1, 2]
    #     }

    #test3 init_main(50,1.0,50)
    # init_popu = {
    #     'c_rp': [0.3656248590857726, 0.03626850274379101, 0.1566372476678421, 0.3382259494269996, 0.007411313301504685, 0.08104553439103984, 0.24235130663415894, 0.07354095911475678, 0.11169303351205129, 0.1012027484074492, 0.05385762071997363, 0.3316503120316005, 0.25482713175394955, 0.14474771451494317, 0.21378117173700723, 0.1638389695469049, 0.28379990468714833, 0.2921744339666951, 0.17026863055576913, 0.45378813322955797, 0.1101643602503179, 0.22587025034000757, 0.19028444915746007, 0.16065122764116097, 0.19569668575535415, 0.29617851537983514, 0.3948374007384242, 0.18835813226893156, 0.10127975615943663, 0.21197727833324115, 0.3688473818989928, 0.16191975705828981, 0.17376321707052683, 0.40958890883376947, 0.04202595090636607, 0.04422103985948056, 0.22326766625639616, 0.4248368906443618, 0.07908009737868421, 0.3845431735384491, 0.04062162998919322, 0.3246838005966225, 0.01783690136694449, 0.029763741192829152, 0.1826639290717853, 0.37762445855304966, 0.1985854382021045, 0.3013690952125407, 0.47548967374926343, 0.44551748954209325],
    #     'c_rm': [0.3229176116753448, 0.05779823357792749, 0.007582567466609985, 0.3677795819270936, 0.23817055535134565, 0.10495563144891101, 0.0656212782633164, 0.17091000022036146, 0.1000074310617198, 0.17352781772347017, 0.039832014748863415, 0.3055940519551792, 0.29856567453630023, 0.15175471605525273, 0.19576112152689815, 0.07842292299376011, 0.28024449331417617, 0.4980273668902767, 0.11057425762093323, 0.47801221590099474, 0.08613362277878531, 0.03431044636040326, 0.12851384905052918, 0.24750236064581535, 0.04512171078363142, 0.2785256644088949, 0.2863905736800203, 0.09879195259914153, 0.1203586316938543, 0.0770161901592957, 0.31970982857323094, 0.1871293393817813, 0.206649659503299, 0.4419099232349848, 0.03982921245904816, 0.2079136982887979, 0.2318531848123239, 0.27301447635814025, 0.18348481898716812, 0.306896725965626, 0.04582964356063912, 0.33158763919568296, 0.028991496171371728, 0.13527799513601174, 0.062016937361908, 0.47428330271049535, 0.16215673513098805, 0.3727768171741238, 0.41860202786533773, 0.38636113540912154],
    #     'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_p_cost': [[0, 0, 0.3951567166581016, 0.3316503120316005, 0.6657468160617961, 0.07354095911475678, 0.40958890883376947, 0.1566372476678421, 0.08104553439103984, 0.22587025034000757, 0.6086185724754314, 0, 0, 0, 0.6131950229132934, 0.20003237174859828, 0, 0, 0.47548967374926343, 0.6364520623013432, 0.3845431735384491, 0, 0, 0.1101643602503179, 0, 0.7411684234885809, 0.3433331527170477, 0.10127975615943663, 0, 0, 0.21197727833324115, 0.09613135501710157, 0, 0, 0.61928070661262, 0.29617851537983514, 0.5154421002230913, 0.32884271731434783, 0.05385762071997363, 0.3382259494269996, 0.11169303351205129, 0, 0, 0.5414634280999546, 0, 0, 0.6669939542983132, 0, 0.3246838005966225, 0]],
    #     'v_m_cost': [[0, 0, 0.5839299079851424, 0.3055940519551792, 0.5383593570803326, 0.17091000022036146, 0.4419099232349848, 0.007582567466609985, 0.10495563144891101, 0.03431044636040326, 0.4821516952069185, 0, 0, 0, 0.3718064289572818, 0.24585225275694497, 0, 0, 0.41860202786533773, 0.5400291532629027, 0.306896725965626, 0, 0, 0.08613362277878531, 0, 0.8117691507928969, 0.31391145118624075, 0.1203586316938543, 0, 0, 0.0770161901592957, 0.12661894220834738, 0, 0, 0.5930107949124206, 0.2785256644088949, 0.7298805517026006, 0.4872766526018302, 0.039832014748863415, 0.3677795819270936, 0.1000074310617198, 0, 0, 0.5527062257042554, 0, 0, 0.6956944288494686, 0, 0.33158763919568296, 0]],
    #     'h_p_cost': [[0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 0, 0, 0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 1.0]],
    #     'h_m_cost': [[0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 0, 0, 0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0, 1.0, 1.0, 0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 1.0]],
    #     'population': [[[46, 48], [31, 20], [7, 36], [39, 46], [37, 41], [8, 26], [37, 41], [5, 25], [40, 2], [4, 23], [38, 18], [3, 39], [25, 27], [26, 21], [10, 19], [43, 35], [25, 27], [36, 40], [15, 9], [19, 38], [23, 34], [9, 1], [2, 15], [2, 15], [4, 23], [35, 32], [10, 19], [14, 14], [27, 4], [30, 49], [4, 23], [25, 27], [34, 42], [6, 31], [31, 20], [2, 15], [36, 40], [14, 14], [37, 41], [20, 43], [25, 27], [48, 3], [31, 20], [15, 9], [19, 38], [43, 35], [26, 21], [46, 48], [18, 7], [34, 42]]],
    #     'map_v_h': {2: 15, 3: 39, 4: 23, 5: 25, 6: 31, 7: 36, 8: 26, 9: 1, 10: 19, 14: 14, 15: 9, 18: 7, 19: 38, 20: 43, 23: 34, 25: 27, 26: 21, 27: 4, 30: 49, 31: 20, 34: 42, 35: 32, 36: 40, 37: 41, 38: 18, 39: 46, 40: 2, 43: 35, 46: 48, 48: 3}
    #     } 
    # addtion0 = {
    #     'c_rp': [0.07621333555780102, 0.46375821846763693, 0.13465225553760746, 0.04086304733562157, 0.1009779680067246, 0.4861803821505196, 0.3083357279536146, 0.1972044038328345, 0.43967331875511817, 0.3749542227647979, 0.09127180441537164, 0.2777042086525858, 0.25529236992911575, 0.37278780653861293, 0.4777007341657317, 0.09688727332539177, 0.09206909459447732, 0.03512152190484974, 0.012591695146030812, 0.28086418323881, 0.024439559275153788, 0.052596682108753345, 0.09575465882930984, 0.41892317505603666, 0.37726618084985447, 0.3194620944653095, 0.32417636088940677, 0.4669291725694947, 0.043900226109121476, 0.10800555344670743, 0.16291921650949343, 0.439013333519231, 0.3671037096048017, 0.4266674082354822, 0.0983949713346251, 0.4820309895683887, 0.03273512707628157, 0.40012086598502294, 0.3376801067629004, 0.36466895110733644, 0.4184007640974132, 0.4498523111618689, 0.2976061136525239, 0.40296823374806623, 0.2915279038244716, 0.3206797971971431, 0.31136679730970424, 0.20838283698030108, 0.25799541146012306, 0.2350945096810504],
    #     'c_rm': [0.1704308828834483, 0.3347032580788516, 0.08734440553580572, 0.08489406425855237, 0.20867808263144344, 0.45928162740129275, 0.32092476262321223, 0.12323201713986104, 0.25792986790385053, 0.36051545545685026, 0.009281777087353005, 0.42049519620793135, 0.4205257004673737, 0.28099429863131226, 0.41867072776772213, 0.1301750990650145, 0.20168889176440216, 0.04357330830335035, 0.044344186181650175, 0.3495285114799963, 0.007930630837274355, 0.22402493697626502, 0.02077526230974744, 0.3988718344336295, 0.27150335635906114, 0.3857366319005715, 0.3497797772888227, 0.39581659358574706, 0.22771251427994285, 0.01896244554253476, 0.19435957820896646, 0.27644858374192144, 0.25200406349278487, 0.29236682954734633, 0.016913401059894417, 0.3178951763307213, 0.1401664925043941, 0.40159104559406694, 0.334079925083034, 0.4615439815640866, 0.30262459333641717, 0.40652724430259235, 0.38626546217750213, 0.4977658750512899, 0.28511456161213616, 0.333602528471873, 0.28093320870298816, 0.005212665997561955, 0.45384151930347927, 0.2025538352130676],
    #     'replicas': [4, 3, 5, 5, 1, 5, 5, 4, 1, 0, 5, 3, 0, 3, 3, 3, 0, 4, 2, 1, 2, 2, 2, 4, 1, 2, 3, 1, 0, 2, 1, 5, 0, 2, 3, 3, 2, 5, 3, 5, 4, 1, 2, 4, 1, 4, 2, 2, 3, 4]
    #     } 

    # test4 init_main(40, 1.0, 100)
    # init_popu = {
    #     'c_rp': [0.28398388598933155, 0.43653475071948256, 0.24429543501468687, 0.17937463904732348, 0.2508440340939888, 0.43598549745544823, 0.202317413589856, 0.10736745107747891, 0.3343771957724057, 0.0122574996218216, 0.3434828859496904, 0.20519834783743174, 0.30340797637151273, 0.42901120837264645, 0.495087459551011, 0.4280106639988896, 0.4924305080398353, 0.0849842336387095, 0.05780479146693146, 0.16422752159273069, 0.1825686675805568, 0.009523046151906245, 0.4329963361986103, 0.34054897080239194, 0.35375481216591587, 0.13615828561861493, 0.16473247697855703, 0.08050460535074533, 0.3812328686259671, 0.24873251325975826, 0.4006001526394016, 0.39234914574153784, 0.1405768029303564, 0.38397322082189034, 0.27419329097792083, 0.46390183337234003, 0.4339232137421214, 0.4587673661797638, 0.48343138541234076, 0.4143262437065572],
    #     'c_rm': [0.4006393962924599, 0.31865051508139924, 0.09202133828133774, 0.06670886664674028, 0.48460422282896143, 0.4191769381905748, 0.20855007872629053, 0.05749460574103887, 0.37483539589323084, 0.05767521120032773, 0.36369241717242107, 0.1490394508790149, 0.4231285104908037, 0.3041581605589131, 0.49016671051618993, 0.48400747459092885, 0.4962835262491471, 0.16033514847884522, 0.0744093053836217, 0.02525208740783169, 0.17930409259400848, 0.20343711695717623, 0.3129235237340196, 0.40921185758544776, 0.30866754248916517, 0.1561699438647555, 0.06989504408882916, 0.09257104265820834, 0.40542007242437383, 0.17289062535035835, 0.4880170814975995, 0.4332241967424908, 0.1523913243647724, 0.26641291146977353, 0.37340529498662844, 0.2704260190979928, 0.26566785411858723, 0.323835459938123, 0.41631107746598983, 0.25026223338575193],
    #     'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #     'v_p_cost': [[0, 0, 0.8273368345222587, 0.20519834783743174, 0, 0.583109709032164, 0.1825686675805568, 0.08050460535074533, 0, 0.4329963361986103, 0.3434828859496904, 0.31314826221899356, 0.0849842336387095, 0.6649492057557942, 0, 0.48343138541234076, 0.44398477930186914, 0.8645454147183722, 0, 0, 0.2508440340939888, 0, 0.8213603541141843, 0.4339232137421214, 0, 0.16422752159273069, 0.202317413589856, 0.34054897080239194, 0.05780479146693146, 0.495087459551011, 0.7982994645284476, 0.42367007406201035, 0, 0, 0.4006001526394016, 0, 0.46390183337234003, 0.35375481216591587, 0.4587673661797638, 0.4924305080398353]],
    #     'v_m_cost': [[0, 0, 0.8773109402240735, 0.1490394508790149, 0, 0.5477260212435892, 0.17930409259400848, 0.09257104265820834, 0, 0.3129235237340196, 0.36369241717242107, 0.28374019915391235, 0.16033514847884522, 0.9822624843681785, 0, 0.41631107746598983, 0.5755198348555761, 0.802657989672328, 0, 0, 0.48460422282896143, 0, 0.7373823573014039, 0.26566785411858723, 0, 0.02525208740783169, 0.20855007872629053, 0.40921185758544776, 0.0744093053836217, 0.49016671051618993, 0.5166751448555255, 0.15873020492807802, 0, 0, 0.4880170814975995, 0, 0.2704260190979928, 0.30866754248916517, 0.323835459938123, 0.4962835262491471]],
    #     'h_p_cost': [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 0, 1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 1.0, 1.0, 1.0]],
    #     'h_m_cost': [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 0, 1.0, 1.0, 1.0, 0, 1.0, 0, 0, 1.0, 1.0, 0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 1.0, 0, 0, 1.0, 0, 1.0, 1.0, 1.0, 1.0]],
    #     'population': [[[2, 12], [17, 3], [31, 0], [31, 0], [20, 8], [2, 12], [26, 26], [2, 12], [5, 13], [11, 30], [10, 4], [3, 24], [16, 31], [22, 1], [29, 18], [17, 3], [39, 5], [12, 21], [28, 2], [25, 36], [6, 38], [13, 37], [9, 27], [27, 39], [37, 19], [11, 30], [11, 30], [7, 28], [13, 37], [5, 13], [34, 11], [22, 1], [16, 31], [30, 34], [13, 37], [36, 22], [23, 7], [38, 25], [15, 15], [30, 34]]],
    #     'map_v_h': {2: 12, 3: 24, 5: 13, 6: 38, 7: 28, 9: 27, 10: 4, 11: 30, 12: 21, 13: 37, 15: 15, 16: 31, 17: 3, 20: 8, 22: 1, 23: 7, 25: 36, 26: 26, 27: 39, 28: 2, 29: 18, 30: 34, 31: 0, 34: 11, 36: 22, 37: 19, 38: 25, 39: 5}
    #     } 
    # addtion0 = {
    #     'c_rp': [0.17248459348735468, 0.16996146769523118, 0.02095301302317143, 0.3547814022227422, 0.27203832592059135, 0.24335263505148041, 0.1622209668795555, 0.016397374516197827, 0.1883998148678645, 0.01204078659485186, 0.33619708379953095, 0.2558525626350479, 0.000593233475131405, 0.08453014016398624, 0.04122557288565104, 0.2865963237319309, 0.3786979455649691, 0.0004014970996242262, 0.47603297478895995, 0.3693102587553133, 0.3723493925488835, 0.31743920184783153, 0.33623113220174317, 0.21319623120220793, 0.2985786634675791, 0.18631960529944563, 0.42391326251836337, 0.4739133616207441, 0.2583222182140685, 0.48858512919705743, 0.12982728014552564, 0.22528349100453154, 0.2253064686907021, 0.2678910500048797, 0.03135652123832455, 0.17858054198812878, 0.40624407491029574, 0.4904588759193698, 0.17909224843948357, 0.42508841374984174, 0.06112049391194585, 0.034360879752835805, 0.27570404011205624, 0.31359366628345176, 0.023410232400122244, 0.3207633472293461, 0.023537699524519118, 0.36014135011103365, 0.48803919998193074, 0.45504127181981363, 0.12681501277271956, 0.35840688244206576, 0.10837973178125199, 0.3342148188037637, 0.18972903885935555, 0.495747083543017, 0.34481943097006595, 0.09438530612748164, 0.18783555543928887, 0.007562742559416635, 0.15659780559409792, 0.010355289252458544, 0.4559139917496532, 0.20907552629815818, 0.13572120163770374, 0.4599412630017437, 0.18846413241427762, 0.36970347915848256, 0.03422558496714967, 0.4358227858136363, 0.16276985354631124, 0.28739166982230724, 0.46481993535901667, 0.1167818682209516, 0.26449229780259764, 0.48211339814472043, 0.33218762795134765, 0.1537108093280657, 0.31079215668323806, 0.2841886272940709, 0.49025543241064085, 0.1748587511616737, 0.4376081888947662, 0.02121317258761457, 0.49537360904750793, 0.0009323452713875247, 0.23120066381381954, 0.37078384450274227, 0.4637607059638064, 0.4811812493427495, 0.01849513281181081, 0.1965096864234127, 0.3400477329621142, 0.001364155833518177, 0.35954697746173436, 0.16986291979681223, 0.2566627599045783, 0.42617303350959335, 0.3228133292533839, 0.27828622504926964],
    #     'c_rm': [0.14856314369777895, 0.22396551158720984, 0.11389446562412592, 0.2874285172587516, 0.4152417836976194, 0.032374807723411086, 0.07434937491718613, 0.23218952857679753, 0.2161936345060865, 0.24886368213004492, 0.3638664599709515, 0.42450078040541, 0.14238004942704402, 0.11732495216492506, 0.11888544589045444, 0.3036242214131048, 0.42602735815039017, 0.2278450265511283, 0.393951125503342, 0.32652541459713774, 0.34799762417368635, 0.49495303012698066, 0.26643053777038567, 0.011062826177644036, 0.37309628825826635, 0.024426700273414897, 0.33133063784068884, 0.34912574509219557, 0.2774401105554112, 0.44569866334308694, 0.001615127278045525, 0.03466085305807526, 0.22556460832897499, 0.262000194397895, 0.1912935056874782, 0.19560607764673457, 0.45600531414884404, 0.4206823358390188, 0.10673444818575265, 0.31804008191030164, 0.22540035739481487, 0.08519951930315436, 0.4700188306783086, 0.40487898287090657, 0.22652528972993818, 0.46843766001231446, 0.15332414071410005, 0.4257416734713057, 0.3166757390749914, 0.2652873143967934, 0.2137031648231498, 0.47246544725424905, 0.19362786398481283, 0.29943969223863764, 0.11739901565483843, 0.2852366236171714, 0.2981645588076681, 0.15048795085647404, 0.12866362038903698, 0.15522461662303363, 0.12188155893055075, 0.03842114917539605, 0.45322319426233226, 0.2283296635881424, 0.03817347671426291, 0.41213450269010443, 0.08041982917937376, 0.41327084688603877, 0.087617116156572, 0.2527438559215338, 0.012518849716800812, 0.3900601181645068, 0.32317965866342324, 0.21239898124653778, 0.3117808463779589, 0.32892299867651087, 0.2895902881143163, 0.13319770547769738, 0.4214830878084943, 0.43308401083588455, 0.4980782546426058, 0.08567854870175526, 0.38251704137237863, 0.032326144564120585, 0.4955401663878976, 0.03803436472393998, 0.12146832817903555, 0.33513819274098744, 0.2880466794776122, 0.4143301456182311, 0.06722903187096399, 0.1558243734712564, 0.29884667796121533, 0.21990859134186627, 0.404198442741937, 0.11291867228402283, 0.3425063625165257, 0.448528779991605, 0.34937646940388456, 0.4737933334874257],
    #     'replicas': [1, 1, 2, 4, 0, 1, 3, 5, 4, 0, 2, 0, 3, 1, 5, 4, 3, 1, 2, 0, 5, 1, 5, 2, 2, 0, 3, 0, 3, 3, 0, 2, 4, 1, 1, 2, 1, 1, 2, 2, 3, 4, 2, 3, 3, 1, 2, 2, 1, 3, 2, 5, 2, 5, 2, 1, 5, 0, 2, 0, 0, 5, 0, 1, 0, 5, 5, 4, 0, 4, 1, 3, 2, 0, 3, 2, 3, 4, 1, 1, 4, 1, 0, 3, 1, 1, 4, 5, 0, 1, 1, 5, 3, 4, 2, 1, 1, 1, 0, 2]
    #     } 


    # test5 init_main(50, 1.0, 100) 使用vm_option以及新的create_VM()
    init_popu={
        'h_m_cost': [[0.4, 0.4, 0.3, 0, 0, 1.0, 0.8, 1.0, 0, 0.5, 0.8, 0, 0.8, 1.0, 0, 1.0, 0, 0.4, 1.0, 0.5, 1.0, 1.0, 0.7, 0, 0.4, 0, 0, 1.0, 0.8, 1.0, 0, 0.5, 0, 0.3, 0.4, 0.3, 0.7, 0.5, 0, 1.0, 0, 0.4, 0.5, 0.7, 1.0, 0.7, 0, 0, 0.8, 0.5]],
        'map_v_h': {2: 9, 3: 12, 4: 35, 5: 22, 6: 39, 7: 17, 8: 18, 9: 2, 10: 41, 11: 49, 14: 7, 16: 1, 17: 20, 18: 34, 19: 31, 22: 6, 23: 37, 24: 13, 25: 48, 26: 42, 27: 33, 28: 28, 29: 27, 30: 45, 32: 10, 33: 0, 36: 36, 37: 24, 38: 19, 39: 44, 41: 29, 42: 48, 44: 21, 45: 43, 46: 5, 47: 15},
        'c_rp': [0.39803995189060776, 0.1991658405314019, 0.39768889258222717, 0.3325366354778356, 0.1342777876545161, 0.01656148103282018, 0.05397241445867573, 0.1310434487858827, 0.2704227767280211, 0.008955044055479089, 0.1331721771022163, 0.4241489946289537, 0.3968269044094304, 0.33398198503451765, 0.2495301921879871, 0.08463941599263941, 0.48407314029569853, 0.33486458390354445, 0.14030090211415353, 0.04343243706425565, 0.26124013102124194, 0.3785576996809441, 0.24891073064760638, 0.38282191475385174, 0.21379682570484998, 0.24378931841585733, 0.3002020187123837, 0.1919340274682979, 0.46964883581045436, 0.4714404337487207, 0.06156666961513463, 0.021995671323702337, 0.38869392752558096, 0.12060983793092295, 0.07127347986816346, 0.3838773335994973, 0.37407500041696556, 0.13472434699437258, 0.04449859672699252, 0.36987986212047896, 0.3531740929128703, 0.3366870076071558, 0.16173162442617905, 0.15702730502599677, 0.03809488688757445, 0.08669477009365767, 0.05318386717506646, 0.16398068552521866, 0.2972309296170753, 0.39941631749265183],
        'v_m_cost': [[0, 0, 0.14800148868523197, 0.41801591843087094, 0.18152753484222625, 0.5440159638226236, 0.7458234444061824, 0.2940070530987197, 0.2927490230023475, 0.22850523363734732, 0.24019890890227028, 0.29857914697853616, 0, 0, 0.12279332999634093, 0, 0.2182348067642732, 0.9645704513714561, 0.24100621927613597, 0.42665785344140605, 0, 0, 0.4881140695231102, 0.06452735097775414, 0.371320197853085, 0.011984010378050941, 0.029893211192067864, 0.23579121395624217, 0.37809063210515087, 0.5844804118897265, 0.19750568192006432, 0, 0.7743002345296373, 0.3232851836249956, 0, 0, 0.4683640657503727, 0.3128431944021872, 0.4587901293671526, 0.048552451636542565, 0, 0.8131416406834183, 0.11710179440422402, 0, 0.496905627847963, 0.2300124473863819, 0.32058458723754407, 0.44937996238431505, 0, 0]],
        'v_rm': [1.0, 0.4, 0.5, 0.8, 0.3, 0.7, 1.0, 0.4, 1.0, 0.3, 0.4, 0.5, 0.8, 0.7, 1.0, 0.3, 0.4, 1.0, 0.4, 0.5, 0.5, 0.8, 0.8, 0.5, 1.0, 0.4, 0.5, 0.3, 0.8, 1.0, 0.7, 0.4, 0.8, 0.4, 0.8, 0.8, 0.7, 0.4, 0.5, 1.0, 0.4, 1.0, 0.4, 1.0, 1.0, 0.7, 1.0, 1.0, 0.4, 0.8],
        'h_p_cost': [[0.5, 0.5, 0.3, 0, 0, 1.0, 1.0, 1.0, 0, 0.6, 1.0, 0, 1.0, 1.0, 0, 1.0, 0, 0.5, 1.0, 0.6, 1.0, 1.0, 0.8, 0, 0.5, 0, 0, 1.0, 1.0, 1.0, 0, 0.6, 0, 0.3, 0.5, 0.3, 0.8, 0.6, 0, 1.0, 0, 0.5, 0.6, 0.8, 1.0, 0.8, 0, 0, 1.0, 0.6]],
        'c_rm': [0.37809063210515087, 0.14797875989440723, 0.446136333563489, 0.2846394747802726, 0.09475784196039902, 0.2182348067642732, 0.11710179440422402, 0.11099353151435348, 0.4389301157389788, 0.19750568192006432, 0.16627953082252578, 0.2996871108426934, 0.269498295337843, 0.4896607597493646, 0.14800148868523197, 0.22850523363734732, 0.3232851836249956, 0.4144842213761347, 0.0005388631986207315, 0.048552451636542565, 0.307887938597714, 0.44937996238431505, 0.18901768925024898, 0.3986574193072836, 0.14987527849489743, 0.2300124473863819, 0.42665785344140605, 0.20854072345543492, 0.371320197853085, 0.4346051333948291, 0.23579121395624217, 0.14212366009071636, 0.4881140695231102, 0.09807524881155391, 0.12772752227619394, 0.4308824936720783, 0.2927490230023475, 0.011984010378050941, 0.24100621927613597, 0.259224237003565, 0.2847917268190586, 0.4683640657503727, 0.12279332999634093, 0.06452735097775414, 0.029893211192067864, 0.1043024709467523, 0.18152753484222625, 0.18758561546418268, 0.32058458723754407, 0.4587901293671526],
        'v_rp': [1.0, 0.5, 0.6, 1.0, 0.3, 0.8, 1.0, 0.5, 1.0, 0.3, 0.5, 0.6, 1.0, 0.8, 1.0, 0.3, 0.5, 1.0, 0.5, 0.6, 0.6, 1.0, 1.0, 0.6, 1.0, 0.5, 0.6, 0.3, 1.0, 1.0, 0.8, 0.5, 1.0, 0.5, 1.0, 1.0, 0.8, 0.5, 0.6, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 0.8, 1.0, 1.0, 0.5, 1.0],
        'v_p_cost': [[0, 0, 0.2495301921879871, 0.7362936470549859, 0.05318386717506646, 0.7230539550333492, 0.8218378872111809, 0.20444565697037975, 0.37407500041696556, 0.08463941599263941, 0.14260550925462528, 0.29502413431110136, 0, 0, 0.16173162442617905, 0, 0.01656148103282018, 0.7885778979820345, 0.04449859672699252, 0.3002020187123837, 0, 0, 0.38869392752558096, 0.15702730502599677, 0.46964883581045436, 0.13472434699437258, 0.03809488688757445, 0.06156666961513463, 0.39803995189060776, 0.6852372594535707, 0.008955044055479089, 0, 0.6665186205123532, 0.48407314029569853, 0, 0, 0.3366870076071558, 0.2786287975619556, 0.39941631749265183, 0.04343243706425565, 0, 0.7176864986573962, 0.05397241445867573, 0, 0.5101508616688484, 0.24378931841585733, 0.2972309296170753, 0.3785576996809441, 0, 0]],
        'population': [[[28, 28], [3, 12], [6, 39], [32, 10], [17, 20], [16, 1], [42, 48], [11, 49], [17, 20], [30, 45], [7, 17], [6, 39], [3, 12], [32, 10], [2, 9], [9, 2], [33, 0], [41, 29], [3, 12], [39, 44], [44, 21], [47, 15], [44, 21], [41, 29], [29, 27], [45, 43], [19, 31], [37, 24], [24, 13], [29, 27], [27, 33], [10, 41], [22, 6], [10, 41], [7, 17], [17, 20], [8, 18], [25, 48], [18, 34], [5, 22], [5, 22], [36, 36], [14, 7], [23, 37], [26, 42], [37, 24], [4, 35], [11, 49], [46, 5], [38, 19]]]
        }

    addtion0={
        'c_rm': [0.12724923237168873, 0.2302721028812758, 0.02191444219166494, 0.3013645216685813, 0.48897446108798703, 0.0234901968008423, 0.3771913081071047, 0.22209734026425582, 0.41391081355188536, 0.2817032737249423, 0.030146492134660224, 0.4379983116779751, 0.09502065100887658, 0.3950141104427656, 0.19528376497506816, 0.20823149515114106, 0.44323803564487335, 0.0025428982348151274, 0.3249066662838954, 0.205567058133299, 0.21349346691730633, 0.30237438741784994, 0.39374958060505155, 0.05506299602245149, 0.2807617919186476, 0.3749591716213659, 0.15184529493233262, 0.39854966241326806, 0.33523353711422277, 0.4752541716099998, 0.25685674446234824, 0.10903770313561995, 0.4276976868405121, 0.43300638258350416, 0.0456029386292236, 0.46549040282748133, 0.17765338748853168, 0.0934661221926929, 0.3954775768765382, 0.49108265318676436, 0.40884428034542597, 0.364658773381155, 0.31315893636181635, 0.32003608849730597, 0.35205544108622877, 0.421400783872125, 0.340178671088145, 0.3207232886954098, 0.31301399729691504, 0.305957669028904, 0.2587998104719148, 0.14987701490987787, 0.12286710412690202, 0.1643105372162426, 0.2614597593841833, 0.20195967128241013, 0.1961957342865447, 0.20659250240237836, 0.20802818472201912, 0.3641306506288858, 0.18082887838479442, 0.42445094636545905, 0.3566837410007157, 0.3539965799485931, 0.049393884630116874, 0.05843407340139495, 0.4719686138987689, 0.14086556422744853, 0.4262395054831031, 0.0028956928738476106, 0.21830008720508656, 0.28599725253839714, 0.4486971164231134, 0.41541969276935015, 0.09695947985807693, 0.3214933547315539, 0.3319613979970855, 0.25634574843974856, 0.04470711151349721, 0.011807628954853572, 0.12630902545063444, 0.13677898557030524, 0.24399531235619873, 0.052103188808726664, 0.06876660472918, 0.4865100234848053, 0.11770199771313858, 0.466120667899827, 0.4731017893460968, 0.07333858310731534, 0.3419023692313965, 0.12904833952452358, 0.04544969341842153, 0.3718346237745156, 0.2594324249190014, 0.49685562667823757, 0.0629579825744293, 0.021576611683093105, 0.04592072537996808, 0.22864552449513367],
        'c_rp': [0.24287380004718884, 0.11732941819398013, 0.07679450149737188, 0.4825230566268437, 0.4113988337502151, 0.0014786751468847115, 0.33827959700425503, 0.21091676941432547, 0.28336517727156285, 0.3721422626805915, 0.05535705713215172, 0.34628354266195266, 0.043045697389501036, 0.4587298600292345, 0.13961225698695567, 0.12101478456908693, 0.43176140263221313, 0.12784023171147418, 0.3732434110283516, 0.0806503209181822, 0.013288237300968897, 0.3035811630452029, 0.38710621113764826, 0.015388306804734297, 0.45490208939266963, 0.3474555831278905, 0.02170225718712321, 0.3453365551704884, 0.4058359183522699, 0.3827483160405229, 0.35428148465634224, 0.12247784873747031, 0.38216094961196473, 0.4062941136001976, 0.03225462653971345, 0.4512180697552103, 0.2060560790899793, 0.17253856833520514, 0.34304131586777936, 0.3606980997343634, 0.39770875719001614, 0.43150196395382123, 0.39114418695925807, 0.40577932611200157, 0.272376355940989, 0.47765471190476344, 0.2850407683341675, 0.42011021365353524, 0.4625241942015957, 0.36662963367394463, 0.3822584783730816, 0.13558490086347585, 0.22954288793444205, 0.09976022956123104, 0.36911470853878087, 0.013207872580046465, 0.1254307497532945, 0.18631705158743622, 0.0061525930293457876, 0.42752834281498253, 0.2356845138641105, 0.47727463020324185, 0.2572533818555725, 0.48422210840068336, 0.11576165922168186, 0.1621165700552259, 0.33383219895003646, 0.07748829052048806, 0.43093048368701203, 0.10308121995835334, 0.15754324001673548, 0.3156727858609588, 0.2976206050698703, 0.47092888561740953, 0.04361034986052975, 0.47601519610315374, 0.2684921226313891, 0.36251552285823446, 0.08659161909582103, 0.18469917884158704, 0.1749137878158391, 0.09334594162582854, 0.05127291972721165, 0.21029684828330486, 0.1975479200870488, 0.4443544754934908, 0.039315444313542613, 0.39008544255427585, 0.46370478544053134, 0.057304261072659735, 0.49793763032797417, 0.12200490078019233, 0.055275747022489, 0.4460240817791273, 0.2557956942790181, 0.30371824473714826, 0.16026064896100195, 0.04363093290138742, 0.016685483290081016, 0.24168678506346758],
        'replicas': [2, 2, 1, 4, 0, 4, 4, 2, 5, 0, 4, 1, 0, 0, 0, 4, 3, 0, 5, 3, 1, 2, 0, 4, 2, 4, 2, 3, 3, 4, 2, 4, 0, 2, 3, 4, 2, 3, 1, 1, 5, 0, 3, 4, 4, 5, 1, 4, 1, 5, 5, 5, 4, 3, 1, 3, 0, 2, 3, 1, 3, 1, 1, 0, 1, 1, 5, 0, 3, 2, 5, 0, 5, 2, 2, 3, 2, 2, 3, 3, 5, 4, 3, 0, 1, 1, 3, 5, 0, 1, 2, 2, 3, 3, 4, 2, 3, 3, 3, 5]
        }

    cost0 = utilization_ratio_cost(init_popu)
    init_popu0 = copy.deepcopy(init_popu)
    s0 = 'Start: \ninit_popu = {}  \naddtion = {} \nThe initial cost = {}'.format(init_popu, addtion0, cost0)
   
    simple0 = FFDSum_simple(init_popu, addtion0)
    complex0 = FFDSum_complex(init_popu0, addtion0)
    cost_simple = utilization_ratio_cost(simple0)
    cost_complex = utilization_ratio_cost(complex0)

    s1 = '\n\n\nEnd:   \nBins_simple = {} \nThe cost_simple of new state = {}'.format(init_popu, cost_simple)    
    s2 = '\n\n\nEnd:   \nBins_complex = {} \nThe cost_comlex of new state = {}'.format(init_popu0, cost_complex)    
    print s0,'\n' ,s1,'\n',s2

    with open('addtion_phase//tmp.py','a') as f:
        f.flush()
        f.write(s0)
        f.write(s1)
        f.write(s2)

