#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-12-17
@Author : Amy
Goal : 分别以docker/VM，docker/HM作为资源利用率排序准则，对比同时使用FFDSum时的最终结果，并存于Result_Contrast.py
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
    3. 分高者即满足约束且最为合适的方案，(并对其剩余VM可申请资源全部分配)，若无则需新引入HM。
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
        # for c, m in vm_option:
        #     if reservedCPU <= c and reservedMEM <= m:
        #         min_vm = [c, m]
        #         break

    # 分最高者hm作为容纳新VM的主机，若无满足hm则在主程序中统一起用新HM，创建新VM（控制VM创建规模暂不考虑）
    if len(weightedHMBins) > 0:
        hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
        return (hm_suffix, min_vm)
    else:
        return False

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

def find_HM_simple(bins, v_rp, v_rm, vm_suffix):
    '''
    按照First Fit选择集群中能够容纳下新VM的 active或down的HM
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

def new_FFDSum_simple(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    @note:  此算法对于新建VM都会在active HMs上按照VM放入造成各HM所有维度资源最大占用程度排序选择
    '''

    print " \n进入 FFDSum_complex() 方法" 


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM打分，分最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM打分，分最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = new_weightVMBins_simple(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = new_find_HM_simple(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix)

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
                hm_suffix = new_find_HM_simple(bins, vm['rp'], vm['rm'], vm_suffix)

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
    print "Complex used time is {} \n used the number of HMs is {}".format(time1-time0, len(num))
    return bins

def new_weightVMBins_simple(bins, object_CPU, object_MEM):
    '''
    @note:  此算法对于新建VM都会在active HMs上按照VM放入造成各HM所有维度资源最大占用程度排序选择
    对放入新容器产生的docker/vm使得VM所有维度资源最大使用进行排序选择
    CPU得分sum(reservedCPU/v_rp*100)
    MEM得分sum(reservedMEM/v_rm*100)
    '''
    print "\n 进入weightVMBins_complex() 方法"

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

def new_find_HM_simple(bins, v_rp, v_rm, vm_suffix):
    '''
    @note:  此算法对于新建VM都会在active HMs上按照VM放入造成各HM所有维度资源最大占用程度排序选择
    为VM找寻可容纳其的HM标号(系统已有/新增)，并更新所引起的hm资源编号，及map_v_h
    '''
    print '\n进入 find_HM_complex() 方法'
    # 对集群已有的所有HMs进行打分
    weightedHMBins = new_weightHMBins_simple(bins, v_rp, v_rm)

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

def new_weightHMBins_simple(bins, object_CPU, object_MEM):
    '''
    @note:  此算法对于新建VM都会在active HMs上按照VM放入造成各HM所有维度资源最大占用程度排序选择
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
            break
    return vm

def create_VM_random(c_rp, c_rm, vm_option):
    '''
    从vm_option中随机挑选满足约束的VM
    '''
    print "\n 进入 create_VM() 方法"
    # 部分随机的创建任意大小能够容纳该容器的vm
    vm = {'rp':0, 'rm':0}
    # 这种方法总是选择最大者放入,故基本都是(1.0, 1.0)的VM
    # for i in xrange(len(vm_option)):
    #     if vm_option[i][0] >= c_rp and vm_option[i][1] >= c_rm:
    #         vm['rp'], vm['rm'] = vm_option[i][0], vm_option[i][1]
    #         break
    # 采用随机生成方式，模拟创建的VM
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
            break
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

def compute_cost(bins, size=1):
    '''
    优化目标，新增场景提高各节点实际物理资源利用率，即集群中剩余资源利用率最大，减少碎片化资源
    '''   
    print "进入能耗、负载方差计算,集群剩余资源利用率"

    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'degree_of_concentration': 0.0,
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
                # 计算集群剩余资源量即各HM节点cpu、mem余量之乘积，所有active HM求和
                utilization += (1.0 - true_load_cpu) * (1.0 - true_load_mem)
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
        cost['degree_of_concentration'] = 100 * cost['used_hms'] + 1 * utilization

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
    # test1 init_main(50, 1.0, 100) 使用vm_option以及新的create_VM()
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

    cost0 = compute_cost(init_popu)
    init_popu0 = copy.deepcopy(init_popu)
    s0 = 'Start: \ninit_popu = {}  \naddtion = {} \nThe initial cost = {}'.format(init_popu, addtion0, cost0)
   
    simple0 = new_FFDSum_simple(init_popu, addtion0)
    complex0 = FFDSum_complex(init_popu0, addtion0)
    cost_simple = compute_cost(simple0)
    cost_complex = compute_cost(complex0)

    s1 = '\n\n\nEnd:   \nBins_simple = {} \nThe cost_simple of new state = {}'.format(init_popu, cost_simple)    
    s2 = '\n\n\nEnd:   \nBins_complex = {} \nThe cost_comlex of new state = {}'.format(init_popu0, cost_complex)    
    print s0,'\n' ,s1,'\n',s2

    with open('addtion_phase//Result_Contrast.py','a') as f:
        f.flush()
        f.write(s0)
        f.write(s1)
        f.write(s2)

