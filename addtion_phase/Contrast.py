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
from init import *


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

    # # print " \n进入 FFDSum_complex() 方法" 
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
                    # print "出错了，竟然使用中的VM没有对应的HM，程序将中止"
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
    used_time = time.time() - time0
    print "Complex used time is {} \n used the number of HMs is {}".format(used_time, len(num))
    return (bins, used_time)

def weightVMBins_complex(bins, object_CPU, object_MEM):
    '''
    以最大化使用VM资源为目标，以docker作为实际负载考虑，引入基于打分机制的FFDSum算法，
    对各个VM计算放入object引起的资源占比与hosted HM引起的资源占比之和。
    CPU得分sum(reservedCPU/v_rp*100)
    MEM得分sum(reservedMEM/v_rm*100)
    '''
    # print "\n 进入weightVMBins_complex() 方法"

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
    # print '\n进入 find_HM_complex() 方法'

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

    # print " \n进入 FFDSum_simple() 方法" 


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
    used_time = time.time() - time0
    print "Simple used time is {} \n used the number of HMs is {}".format(used_time, len(num))
    return (bins, used_time)

def weightVMBins_simple(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    # print "\n 进入weightVMBins_simple() 方法"

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
    # print '\n进入 find_HM_simple() 方法'
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

    # print " \n进入 FFDSum_complex() 方法" 


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
    used_time = time.time() - time0
    print "new Simple used time is {} \n used the number of HMs is {}".format(used_time, len(num))
    return (bins, used_time)

def new_weightVMBins_simple(bins, object_CPU, object_MEM):
    '''
    @note:  此算法对于新建VM都会在active HMs上按照VM放入造成各HM所有维度资源最大占用程度排序选择
    对放入新容器产生的docker/vm使得VM所有维度资源最大使用进行排序选择
    CPU得分sum(reservedCPU/v_rp*100)
    MEM得分sum(reservedMEM/v_rm*100)
    '''
    # print "\n 进入weightVMBins_complex() 方法"

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
    # print '\n进入 find_HM_complex() 方法'
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
    # print "\n 进入weightHMBins_FFDSum() 方法"

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
    # print "\n 进入 create_VM() 方法"

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
    # print "\n 进入 create_VM() 方法"
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
    # print "\n 进入 create_VM() 方法"

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
    for key, value in bins['map_v_h'].items():
        map_h_v[value].append(key)
    return map_h_v

def compute_costs(bins, size=1):
    '''
    优化目标，新增场景提高各节点实际物理资源利用率，即集群中剩余资源利用率最大，减少碎片化资源
    '''   
    # print "进入能耗、负载方差计算,集群剩余资源利用率"

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
        utilization = 0

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

    # # print 'true cost={}'.format(cost)
    # return cost
    return cost['used_hms']

def faked_cost(bins, size=1):
    '''
    注意： 这里负载以VM配置作为负载考虑
    计算bins中前size个方案对应的能耗、负载均衡方差代价值
    以集群环境中所有running VMs/HMs作为计算对象
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

    # # print 'origin cost={}'.format(cost)
    return cost

def createJSON(data, addtion_scale, cost0, cost1, cost2=0, cost3=0):
    '''
    goal: 构造符合Echarts平行坐标图的json数据,并覆盖写入file_name文件
    params: cost0 - 4 分别为FFDsum_simple、FFDSum_complex、safe_FFDSum_simple、safe_FFDSum_complex的代价结果
    '''

    # 构造填入各个算法列表的序列，该顺序必须严格按照平行坐标顺序：
    # FFDsum_simple、FFDSum_complex、safe_FFDSum_simple、safe_FFDSum_complex
    data['scale'].append(addtion_scale)
    data['simple'].append(cost0)
    data['complex'].append(cost1)
    data['safe_simple'].append(cost2)
    data['safe_complex'].append(cost3)
    return data


if __name__ == '__main__':
    '''
    对于Docker+VM与Docker+VM+HM架构下，分别不同的排序单位vm，docker进行的FFDSum排序算法，批量对比与画图
    '''
    # test3 main_init(50, 1.0, 600)
    # init_popu={
    #     'h_m_cost': [[0, 0.7, 0, 0.5, 0.5, 0, 0.7, 0.5, 0.8, 0, 1.0, 0.8, 1.0, 0.8, 1.0, 0, 0, 0.5, 0.5, 1.0, 1.0, 0.3, 0.7, 0, 0, 0.4, 0.4, 1.0, 0, 0.3, 0, 0.8, 0.8, 0.4, 0.8, 0.3, 0, 0, 0.8, 0, 0.7, 0, 0.7, 0.4, 0, 1.0, 1.0, 0.5, 0, 0]],
    #     'map_v_h': {0: 3, 1: 32, 2: 20, 3: 12, 6: 27, 7: 19, 8: 7, 9: 11, 11: 13, 12: 8, 13: 46, 14: 14, 15: 13, 16: 26, 17: 40, 18: 10, 20: 34, 23: 31, 24: 4, 25: 45, 27: 1, 28: 17, 30: 34, 33: 47, 35: 21, 36: 33, 37: 22, 38: 42, 39: 25, 42: 38, 43: 35, 44: 18, 46: 29, 47: 43, 48: 6},
    #     'c_rp': [0.46753713484069664, 0.04636662319671786, 0.36371410421672207, 0.4397808694328428, 0.4520105196828375, 0.31461687878874167, 0.3084256333815727, 0.4742530600854063, 0.017754557750803313, 0.2312214598223868, 0.24854485264716403, 0.12117745138186053, 0.08411418388687258, 0.4813761608575876, 0.4584421878210625, 0.4311042102652728, 0.06030912629059282, 0.3546110038595228, 0.2436129220414398, 0.4395827964180183, 0.026328558782577338, 0.26766806339929994, 0.006353103024922424, 0.09959422261955131, 0.22130101987189532, 0.016946830056633833, 0.35476164307933156, 0.4841656305638405, 0.23428761143518467, 0.08205125986030393, 0.3092315521768564, 0.1274451485902971, 0.23279820556475678, 0.14945648131649303, 0.2312650054751273, 0.054880766329289676, 0.4995655577264974, 0.48778459417937425, 0.36418955523344476, 0.1499584651749215, 0.0008667751566664439, 0.36070225961836067, 0.3915062248864705, 0.23398259755537487, 0.3868337465598162, 0.44604448020561355, 0.09225837623573824, 0.04888351328699364, 0.1507781185704513, 0.08993184619937827],
    #     'v_m_cost': [[0.40206563669168577, 0.395672014084409, 0.7278715738116328, 0.5764138102472568, 0, 0, 0.5774414606596321, 0.959555131472364, 0.2809412119846755, 0.317306724557739, 0, 0.20008118367666572, 0.40450467583570693, 0.32939835167536746, 0.05152646699594893, 0.164431857780547, 0.21894466415527922, 0.3178541924587413, 0.9146710859406961, 0, 0.0837220241419647, 0, 0, 0.4071688603133601, 0.41646356801546236, 0.5859872501820467, 0, 0.09383084325781946, 0.43286443648377915, 0, 0.21425453828369292, 0, 0, 0.4497682224419286, 0, 0.03036755720668652, 0.17571875757737992, 0.5262524190389926, 0.3738339515362714, 0.11207395576043322, 0, 0, 0.2159899214861732, 0.04549673532072929, 0.315909771808345, 0, 0.24647529340792082, 0.39649545740251935, 0.1315936360904222, 0]], 
    #     'v_rm': [0.5, 0.8, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.8, 1.0, 0.4, 0.8, 1.0, 1.0, 0.4, 0.4, 0.7, 1.0, 0.7, 0.4, 0.5, 0.4, 0.8, 0.5, 1.0, 0.7, 0.7, 0.5, 1.0, 0.4, 0.3, 0.3, 0.5, 0.3, 0.3, 0.4, 0.7, 0.7, 0.4, 0.5, 0.5, 0.8, 0.3, 0.5, 0.8, 0.3, 0.4, 0.7, 0.5], 
    #     'h_p_cost': [[0, 0.8, 0, 0.6, 0.6, 0, 0.8, 0.6, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 0.6, 0.6, 1.0, 1.0, 0.3, 0.8, 0, 0, 0.5, 0.5, 1.0, 0, 0.3, 0, 1.0, 1.0, 0.5, 1.0, 0.3, 0, 0, 1.0, 0, 0.8, 0, 0.8, 0.5, 0, 1.0, 1.0, 0.6, 0, 0]],
    #     'c_rm': [0.41646356801546236, 0.24739699398976775, 0.3889996083957719, 0.3790975481868236, 0.45990303310677655, 0.3178541924587413, 0.4497682224419286, 0.30685818984825136, 0.010189429553198737, 0.21425453828369292, 0.14865947314328073, 0.20008118367666572, 0.14827502009464125, 0.315909771808345, 0.27058327081138067, 0.3102296672940231, 0.03987486975677568, 0.40206563669168577, 0.21894466415527922, 0.43763989050828445, 0.11207395576043322, 0.3785383593803085, 0.03079564948473476, 0.17571875757737992, 0.03036755720668652, 0.06360428424224832, 0.47703119543241174, 0.4296681049814891, 0.24647529340792082, 0.04549673532072929, 0.32939835167536746, 0.164431857780547, 0.14612971564735883, 0.1935476963719354, 0.028630500933051584, 0.1315936360904222, 0.2865110750730042, 0.40450467583570693, 0.39649545740251935, 0.02226911158125605, 0.1874142018514849, 0.3775929458957118, 0.34877402562480914, 0.09383084325781946, 0.4105953249025231, 0.49965209836558755, 0.08739351561274009, 0.05152646699594893, 0.04384715438518902, 0.2159899214861732],
    #     'v_rp': [0.6, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 0.8, 1.0, 0.8, 0.5, 0.6, 0.5, 1.0, 0.6, 1.0, 0.8, 0.8, 0.6, 1.0, 0.5, 0.3, 0.3, 0.6, 0.3, 0.3, 0.5, 0.8, 0.8, 0.5, 0.6, 0.6, 1.0, 0.3, 0.6, 1.0, 0.3, 0.5, 0.8, 0.6], 
    #     'v_p_cost': [[0.3546110038595228, 0.13048080708359044, 0.8312870943193134, 0.3645808793733885, 0, 0, 0.9326952479064687, 0.898054999888451, 0.24171485755223127, 0.5059186607514199, 0, 0.12117745138186053, 0.48778459417937425, 0.3092315521768564, 0.04888351328699364, 0.1274451485902971, 0.2436129220414398, 0.31461687878874167, 0.7943444394973498, 0, 0.21108724486104413, 0, 0, 0.49893306887442723, 0.46753713484069664, 0.7347183938794006, 0, 0.23398259755537487, 0.5367922117347377, 0, 0.2312214598223868, 0, 0, 0.3084256333815727, 0, 0.22130101987189532, 0.09959422261955131, 0.6092471122655247, 0.4480510403219066, 0.026328558782577338, 0, 0, 0.08993184619937827, 0.08205125986030393, 0.4813761608575876, 0, 0.23428761143518467, 0.36418955523344476, 0.054880766329289676, 0]],
    #     'population': [[[24, 4], [1, 32], [3, 12], [2, 20], [7, 19], [17, 40], [33, 47], [6, 27], [25, 45], [30, 34], [37, 22], [11, 13], [1, 32], [44, 18], [6, 27], [38, 42], [20, 34], [0, 3], [16, 26], [18, 10], [39, 25], [23, 31], [9, 11], [36, 33], [35, 21], [38, 42], [18, 10], [25, 45], [46, 29], [43, 35], [13, 46], [15, 13], [25, 45], [8, 7], [23, 31], [48, 6], [9, 11], [12, 8], [47, 43], [28, 17], [3, 12], [37, 22], [2, 20], [27, 1], [28, 17], [7, 19], [8, 7], [14, 14], [20, 34], [42, 38]]]
    # }

    # addtion0={
    #     'c_rm': [0.37186574350901574, 0.4165091557639013, 0.47480830960171416, 0.44651334770861395, 0.2961709326780183, 0.4297780657277471, 0.37096497523868377, 0.4340253092995384, 0.3000643746249745, 0.45176905716932925, 0.025905679526446013, 0.27686828332273994, 0.0435487512082216, 0.4896802932035266, 0.08157194232401355, 0.03257871119238895, 0.22295847154296772, 0.0697779377433553, 0.18447013561042763, 0.1381592942888916, 0.25057003431525593, 0.12356390820844909, 0.14982515842577013, 0.42912813605218053, 0.19823435610518597, 0.36266387601831784, 0.3243716072219618, 0.239389814330686, 0.3183561553611596, 0.49569395092501645, 0.28485795236586714, 0.3261090120570394, 0.23261764216552847, 0.30579709458937443, 0.03658643112222809, 0.04361156799134794, 0.15859137940569373, 0.27805453039043915, 0.15974932749697107, 0.03685759001541139, 0.42667914363366233, 0.24162512231542962, 0.1724622541347531, 0.41768513380349015, 0.4649275481692375, 0.10367898563876324, 0.29652686397176575, 0.40746837467530705, 0.43491596451989967, 0.10862551619973373, 0.4881166896209102, 0.36810032130968673, 0.3250848448428578, 0.279694489960741, 0.18162203789563455, 0.12133127907137131, 0.13936967386749968, 0.32631595574818545, 0.04390947952066396, 0.11443945697006658, 0.2491779456995943, 0.036518303945034386, 0.033171519106168446, 0.2912708427571312, 0.2598735903089284, 0.10866976349731791, 0.3647790571410142, 0.15941353990031543, 0.06985524274350224, 0.17735499944777658, 0.017360963104863236, 0.46385673953529727, 0.23067437288193596, 0.06119155069163246, 0.18700290760971133, 0.45723279539129924, 0.22459301719204583, 0.4560313253829514, 0.19108111144123352, 0.13216610627885278, 0.1526790276078844, 0.18915053627432094, 0.4424268507057554, 0.050907842823829624, 0.12948896048958394, 0.09681853608485219, 0.24020313975126292, 0.222932275909643, 0.0630251050531897, 0.19159246468154587, 0.19779068621643014, 0.016607488521059532, 0.4225734355404382, 0.31956679316022574, 0.13335817951350684, 0.36294344902314524, 0.21390052409101604, 0.020069858832430315, 0.031563134177735486, 0.31733283983136273, 0.2612616261043156, 0.4901978646392669, 0.1822585550742889, 0.10189485167015286, 0.15836179311747747, 0.1735337517128837, 0.2509999993876843, 0.33073558041309553, 0.392027350699464, 0.18448940786953394, 0.14641150576010656, 0.039393361477761984, 0.4284376821383463, 0.31795373405370475, 0.1286786887615868, 0.027050445955327712, 0.2908346101666075, 0.10560789302275789, 0.2151424501339909, 0.009610747937471964, 0.025911456850036735, 0.0991105089886587, 0.44958281018399715, 0.06221273108932082, 0.4788710482015005, 0.3370311728784082, 0.08033137219602118, 0.4922703043947412, 0.4958064769176814, 0.30431918827794835, 0.23426801262512686, 0.47725710702208696, 0.2692053102869282, 0.07666703355591453, 0.1366822237546619, 0.096212681437128, 0.28305692323240333, 0.31257738562354265, 0.4812849939149194, 0.29361176599844696, 0.40775828109456447, 0.4462774904699932, 0.20205601493252076, 0.22262164697683082, 0.26358180196412534, 0.3243089269096472, 0.4898838601082382, 0.39606990793331814, 0.3101509307737651, 0.1365646701695994, 0.4423696941623717, 0.08705449326928322, 0.3954136205595406, 0.07072671636873429, 0.48667391139525773, 0.13861872892374597, 0.041586017170815476, 0.4247183812770222, 0.009394012472246666, 0.3111627719006852, 0.19837069427244008, 0.22365552959794546, 0.3655716024132649, 0.24475676872130395, 0.07653348263317095, 0.27562310323492833, 0.35513981883814705, 0.4331941994881573, 0.27728204699158254, 0.39718129786737527, 0.3788937650563507, 0.35540780317508036, 0.24158704684652607, 0.06700472674178223, 0.15469546387977248, 0.09532356126070013, 0.18936582221529227, 0.181206803964337, 0.28657837894968335, 0.08083289845975883, 0.48500571276418625, 0.3693952149610521, 0.31324680035247454, 0.4319819905179228, 0.4497314237599393, 0.3221293032806861, 0.3953161327980943, 0.03152454291115683, 0.38933498787366505, 0.037851259101837315, 0.2730788204290633, 0.050773487398160205, 0.20646964478025262, 0.04433674647532662, 0.4404281270961163, 0.01569481647424284, 0.3468000858476531, 0.17783409469996872, 0.08085683952140346, 0.11222808315162983, 0.14646014585648381, 0.287280148771895, 0.3100959046940429, 0.044476846845800944, 0.4589218218519512, 0.23764142646618006, 0.2979786403303784, 0.15400359764853316, 0.28252613553064854, 0.44163384637376, 0.1232422330924926, 0.05005564947797844, 0.1575060763917627, 0.176743466614971, 0.1211956396213037, 0.4462489880636383, 0.23077885756321778, 0.4314907484331479, 0.33963992522556546, 0.4969046026253558, 0.21265415020491918, 0.35792666204481594, 0.1350212912492205, 0.15459043102387138, 0.4586550980752039, 0.12804381108580018, 0.4636767488264291, 0.027118957811320538, 0.24379818225520913, 0.35931195338488364, 0.3941696658801176, 0.2409017797525234, 0.31170499251315287, 0.46024883207099565, 0.09879252993785434, 0.3071250296216007, 0.13380842114820402, 0.1953058607220961, 0.4486226966457955, 0.23907333364658317, 0.010485555368688781, 0.41249487283650443, 0.1676902777380918, 0.3466473354000649, 0.43273385758230337, 0.02929359715258517, 0.18654046722986478, 0.05607298796927923, 0.12081350951536698, 0.4266126891192913, 0.14750399004251058, 0.32711944893627765, 0.23880371027348096, 0.1944415132692643, 0.029923664931516297, 0.1870962972129366, 0.08212230274068924, 0.06005524356336528, 0.24965375424785438, 0.3832880240195119, 0.06523531692833828, 0.0953520010845113, 0.3041737475145774, 0.39543425770177376, 0.24461529699559012, 0.43052568691491244, 0.20539900543745382, 0.06077528060593365, 0.04300107348972845, 0.4586741409742616, 0.4798468056135088, 0.31543483422547364, 0.03193725807845421, 0.1730126131569832, 0.27911855465169644, 0.31400218625616727, 0.3635667467429542, 0.1265195194633813, 0.22326151207974854, 0.1315692603120025, 0.0037961477415163203, 0.44907417155141105, 0.1373395611998061, 0.08220735228631032, 0.13733598230941882, 0.0537032106335853, 0.10739281735490658, 0.27351453490285227, 0.43783301662026197, 0.16001013750639803, 0.18765544600997516, 0.06517163060803241, 0.4128776260935768, 0.11149155223140489, 0.026619823430797107, 0.03459413123454022, 0.34760296017647496, 0.2302268348659491, 0.45448137300501706, 0.20642738865701776, 0.03823834203629786, 0.0007753729953149657, 0.22174570508374195, 0.39618115870065607, 0.07833924392571062, 0.49369201616328817, 0.24754217467448425, 0.4220036027957617, 0.2568851442329897, 0.03740702905705262, 0.016940333430792986, 0.38296448121948634, 0.35345491984603405, 0.3718791533257564, 0.052238852337570474, 0.1664898601406886, 0.14704531829880388, 0.3572905541501804, 0.06379097366979444, 0.008729369156874833, 0.20885151424848644, 0.22384378718358655, 0.0383085370173428, 0.06978290173308863, 0.20114311617553302, 0.48416505833489687, 0.47003363094011485, 0.0729377105753945, 0.320288828178974, 0.05656814088671072, 0.20125899759873206, 0.15734930935949226, 0.4360444720861231, 0.27134951839330557, 0.16624945102124714, 0.31534818535607106, 0.03958639668243347, 0.38526245580192364, 0.2845275028561286, 0.2072631621954612, 0.23279141155406655, 0.14322808519584734, 0.047662138349305105, 0.3983392223462474, 0.13454292141576873, 0.29005838883568913, 0.08604498153308626, 0.44874457600692164, 0.16128113923613605, 0.4651869310247969, 0.2917064840972865, 0.3819560474450556, 0.10598616846789563, 0.3423797995156745, 0.37917151242503144, 0.4776715249409881, 0.033816566246092084, 0.42849599472664074, 0.061954453882369476, 0.33671468622441214, 0.05811894071420892, 0.16719067503560917, 0.037928358716759064, 0.16897357004587826, 0.3562465529710728, 0.34775432890860514, 0.4997444161563169, 0.4975384774576561, 0.421349520139142, 0.12051406340349563, 0.19284903567540507, 0.16143321140704864, 0.16811622952410754, 0.1857940804366549, 0.035240214647034, 0.35859534256061154, 0.25200886505645514, 0.003875881071891324, 0.452778274003573, 0.26618504176514346, 0.04712194082067947, 0.29319761530808075, 0.2498009275682448, 0.40348967138546843, 0.2275540657687761, 0.485494731102874, 0.2698467202758207, 0.181644609750766, 0.14932766726891436, 0.33622199270068504, 0.4414763241706361, 0.05981915955464334, 0.24330823638686974, 0.23678657139260875, 0.4447594561848196, 0.4668675667929868, 0.0641139652666346, 0.08323841959322523, 0.4580895236938832, 0.47003140071109817, 0.1638295899226412, 0.29127744908976905, 0.3757803809040036, 0.49011617460172174, 0.2997970408645596, 0.12067014174607496, 0.4031457478090167, 0.3662179367986232, 0.1722479854875871, 0.4226463245463712, 0.3609609847658265, 0.3508917912184096, 0.35935791567844416, 0.40778860095906877, 0.32151668059031996, 0.08092134956198554, 0.4298224127949589, 0.11753311384619822, 0.18498527288036826, 0.2231019368667597, 0.4138908688888082, 0.3424760855863912, 0.21921216762340498, 0.1405978427178143, 0.24187459847222356, 0.00738960871901187, 0.463917796204644, 0.2049753091080488, 0.15204302986039178, 0.40833424712026883, 0.47085666959755035, 0.21682933212913377, 0.34443363063434296, 0.08509035838606238, 0.12386327420025905, 0.40077475690419373, 0.20985957984040435, 0.2861252125328251, 0.12085365210580096, 0.08506759970168787, 0.2473044818924713, 0.1966374511685269, 0.37698607184554, 0.3980093212420181, 0.3449196637076407, 0.1761329888418641, 0.27856444882544096, 0.46800227585186455, 0.1331240275725011, 0.04516082204838248, 0.19837766828744471, 0.2537247709910397, 0.09708878058815085, 0.4942435363318268, 0.11799283353467332, 0.08031891547743522, 0.4406721431575652, 0.20363129636914423, 0.44016718449154646, 0.4871137315358923, 0.03965678878295387, 0.21236270365307017, 0.21902313170305138, 0.22926298065542383, 0.42916592444470303, 0.23850759994866577, 0.29866000688050776, 0.2783530226808073, 0.09797818957140672, 0.018112751378431824, 0.4897421629609034, 0.24250897669958196, 0.061461428496457055, 0.3190689658650796, 0.044672489131371035, 0.14721708816132947, 0.43382938394563075, 0.24923545045208928, 0.2652884973171458, 0.40372194082045, 0.11019275797749123, 0.2381058467487387, 0.49128903999612245, 0.3488018522410332, 0.46882500290696105, 0.35532646819738667, 0.15679375454851402, 0.129308827740912, 0.04977202395369887, 0.09697446743831672, 0.39255626062351623, 0.30794079202635705, 0.09475701505718803, 0.07562327596379168, 0.3013442872746356, 0.0036421213974237865, 0.45874281452975646, 0.1462327245744063, 0.2610152465632267, 0.2745243144372929, 0.08019076832792274, 0.47180906516916693, 0.2507683636498813, 0.2556127564389057, 0.48127018625839335, 0.41941059392957536, 0.026555503599668295, 0.039325276548780874, 0.2587928734364193, 0.02354441367232374, 0.23330058780134766, 0.33723475489604116, 0.37399243390928966, 0.1372220111739931, 0.41051365834633247, 0.3373721672910944, 0.3001049569423673, 0.2269369442190587, 0.21644263672541167, 0.3112689238076273, 0.3054894831292154, 0.3200393760868323, 0.012790244816163199, 0.025386078421429342, 0.31846203198567025, 0.02558232489034243, 0.26396585067592815, 0.26434542179153164, 0.1301694169282346, 0.10626004299750075, 0.09115506894042677, 0.13591571037179592, 0.3074198007914759, 0.34275522350577925, 0.24109847455355907, 0.36740526588451433, 0.42693832210408544, 0.03009443466014372, 0.4865875846162281, 0.4534753329894743, 0.43669096419851283, 0.13035959169587608, 0.3917758461803158, 0.4673898122717218, 0.25158834233116045, 0.17968307757833654, 0.12420553739464357, 0.05919276680915944, 0.28048003267300314, 0.479629240389001, 0.22102431323394084, 0.35552223456150467, 0.41619168826924907, 0.15197637296798716, 0.33002553220175274, 0.01172981486525801, 0.40863165810673174, 0.43281493150621886, 0.4941458849082052, 0.3402771006545873, 0.29932142924735167, 0.33571396818956395, 0.40088289329073057, 0.31931030209475036, 0.07226107914400157, 0.27584447041649784, 0.22390443885921485, 0.44137200869606297, 0.05679954764408987, 0.3538787195742129, 0.08231716786716486, 0.3306093310558673, 0.4088761590298735, 0.005701646102374641, 0.0079407978636018, 0.02513534323015776, 0.020462690993900162, 0.20925325681889204, 0.48299629051078335, 0.2526271459405319, 0.1067456538729373, 0.05609332872864581, 0.3648953775146927, 0.4906739596634956, 0.4939894409098967, 0.02727515767778632, 0.18592186052538587, 0.0003212801587708647, 0.14053566758979222, 0.30506616683919585, 0.4289836931749391, 0.117926263652746, 0.47303925843095906, 0.19695734163665013, 0.15584274082317026, 0.3281175084414856, 0.25483461082253395, 0.013327699845649826, 0.4348668920523323, 0.011000457039012146],
    #     'c_rp': [0.4833697458455798, 0.3755515869455199, 0.46990091217999114, 0.3763602746575489, 0.4543654546324348, 0.41269482311966044, 0.4981683607872964, 0.4707832480778932, 0.46997736886096486, 0.40651442819922656, 0.00929025530282207, 0.35042851986314905, 0.08367938113515766, 0.36552992962433906, 0.2248022739255227, 0.028477990432169475, 0.001020694745996642, 0.10934342376943229, 0.2487739014331941, 0.118373850391221, 0.483472563552339, 0.16985751014944755, 0.15238846001222855, 0.40317198082696776, 0.22925858242971525, 0.31673916594587764, 0.4132790520402505, 0.13259729967690825, 0.3887650139448799, 0.3606897008148494, 0.314380873107692, 0.3435948552881879, 0.24594622589392562, 0.32914763147163484, 0.23538308282673093, 0.14234804004905782, 0.01857201938582481, 0.2635115707298967, 0.1358019701091046, 0.04803323257386638, 0.361463410797461, 0.023968689782179253, 0.12096437409341965, 0.2844173555155676, 0.3057142872085872, 0.16785121397863523, 0.3688047788373409, 0.28272830767490487, 0.46378389781776813, 0.01170419764533237, 0.4670271645105812, 0.48382636260590545, 0.42703235824430946, 0.3751666736026679, 0.15374978572411796, 0.23541381268880163, 0.0824301575017023, 0.46279642126989357, 0.14325036177336187, 0.0407024335206837, 0.18857019851086465, 0.036466293546731754, 0.23477776706837777, 0.3324291062779458, 0.4327077080103193, 0.06141884653239249, 0.4454217684774466, 0.07101371109704513, 0.06928177047711098, 0.08087750341475597, 0.15836905892384973, 0.31870819428922387, 0.1727741187413801, 0.030208660527103304, 0.06017188331698531, 0.2739635712091708, 0.18918630176668882, 0.42123039681848967, 0.08561007215633637, 0.21198441603181556, 0.048172422179332264, 0.16153427697723016, 0.41070458359140555, 0.0731217825371066, 0.2171931650368621, 0.13219303317089287, 0.19475293150877454, 0.2013428055284378, 0.23687248257788418, 0.09121267304646502, 0.04678819592561867, 0.14672847164193803, 0.3435769264844819, 0.49242020406542814, 0.0409664112790068, 0.36475451227284755, 0.09570676041581277, 0.23890168963808106, 0.20628741644572857, 0.3313512882014375, 0.31582134951414337, 0.2962823493533754, 0.08598334833891602, 0.23681344186737224, 0.17285152387566016, 0.1400732292764877, 0.3236515467581221, 0.4716695133760555, 0.3128417664544814, 0.0850787948504742, 0.1912452786529571, 0.06936794464238927, 0.4204325161542431, 0.35960584872287715, 0.04165655867165108, 0.0486168987725793, 0.26277840449400136, 0.17671586553475233, 0.02751113233356739, 0.1659247697143757, 0.03813989356453079, 0.1974726282923468, 0.49917538295861336, 0.001743278408789517, 0.4729034825381834, 0.31885141054237154, 0.13681615153658466, 0.3973065661402, 0.31507068157757223, 0.41931334880676135, 0.23574979345915775, 0.41995818309220595, 0.44247891104105, 0.24412185388208085, 0.1506196222369861, 0.21215793135643574, 0.4564678389238802, 0.4222802740691941, 0.31482318977858476, 0.33988911336464955, 0.4628959703378222, 0.42966674522435666, 0.21983785344487988, 0.04322069202059753, 0.3643487385988137, 0.4352866691777107, 0.32950162718438475, 0.26424374549907176, 0.25294223217515416, 0.10395002293304423, 0.35108991615448953, 0.002702517971561069, 0.43869003062429457, 0.22986526882049957, 0.4856332192065889, 0.1874860466780231, 0.0026644800125128487, 0.3956899891989233, 0.03199395165380953, 0.4634981593877173, 0.21583224769306647, 0.1792158670640383, 0.4658888700926561, 0.008036984101598421, 0.08553612760670787, 0.2507776880258077, 0.4176733505143218, 0.37322020468723205, 0.2576207240284359, 0.48420929791959083, 0.25505146654247923, 0.3171203114863912, 0.16384530602054342, 0.024495883094568627, 0.05948913785217075, 0.22163276917498625, 0.09175151912267321, 0.018101201827941504, 0.33915977991102236, 0.13416238470279468, 0.3715654909215476, 0.4973797212065931, 0.4547734321466362, 0.2879410944399666, 0.3816661254905886, 0.40499255010778734, 0.29177324232590746, 0.05311443975256813, 0.4153729592894382, 0.09742481867849556, 0.3459547831507878, 0.006594329541183552, 0.08674250460013083, 0.043157734322362584, 0.34466340792092987, 0.08271111420735056, 0.32799913454332125, 0.16650674805300303, 0.10704526491089444, 0.14660874252887035, 0.12915863484711254, 0.43215714171100955, 0.31975146025271006, 0.09853645115930587, 0.4968746557861728, 0.23390281264406504, 0.39917811493586935, 0.04690350884276878, 0.4205732788865237, 0.4814980528532554, 0.061683607796224504, 0.029368471562133958, 0.03075645260373816, 0.15936837603025789, 0.057790953639540954, 0.26371077968430334, 0.24606492675619085, 0.35803285015832964, 0.4786872881841778, 0.2633672000138583, 0.031080552661304495, 0.4073140692753873, 0.12616860022541354, 0.09669042112995979, 0.2631088908103404, 0.1206365114399478, 0.3918690525734456, 0.09295580419383315, 0.21439307261989476, 0.2824540461031053, 0.47604201769732846, 0.09377811715638235, 0.31549574410830733, 0.25376500650400613, 0.05210759184125763, 0.30442467113769767, 0.07407670743568712, 0.03674240996636802, 0.33492505301844, 0.13299753890528648, 0.09487385532565845, 0.49729795194582044, 0.14749712565290685, 0.29447408038016004, 0.47940324830243225, 0.10338808879794209, 0.15151915100138286, 0.08188280892860023, 0.24982817200640695, 0.3809592378304483, 0.07818546564626899, 0.3168367727802198, 0.09617561204557745, 0.007031642483530498, 0.026390758480539234, 0.24100636661154118, 0.1593383661562469, 0.15388613839807447, 0.15686486230372965, 0.2640762698155819, 0.05245067406743381, 0.13918374202244793, 0.25660735028148995, 0.30219399361664234, 0.15375213594422538, 0.4394717980903091, 0.15877873878424448, 0.20955932881127076, 0.22441681293103083, 0.46719885760594976, 0.37353574282748025, 0.4182115848830696, 0.10068901929685592, 0.19647662557300843, 0.460909547006357, 0.36900818594488055, 0.4700526620073861, 0.026792091575969623, 0.15861865094974154, 0.22767152762243908, 0.202323250215742, 0.41135989745454804, 0.24735333058314435, 0.1304242416272311, 0.009571971663267231, 0.10984813935349402, 0.21947129766761503, 0.3493627453416931, 0.28611747716107977, 0.1244149737399104, 0.10127210366968409, 0.028711494070567, 0.2660115833206311, 0.23685166953917214, 0.11187240372218082, 0.16201879452691942, 0.48590678768247986, 0.19103606237232218, 0.3090503813684212, 0.05727406600128959, 0.24012665238158248, 0.09851345228341407, 0.22351243781129188, 0.40269984199289655, 0.1889129507740856, 0.42121105081206883, 0.19851756048846525, 0.44491650124338017, 0.3074840585059377, 0.045458635153576565, 0.18897229030644036, 0.2991825743489055, 0.3060189207794891, 0.37359826228672977, 0.01600298378224263, 0.13553754496479092, 0.20921353050072145, 0.2660770960650142, 0.18172407812899677, 0.08712955573529646, 0.024910769048451742, 0.09167695073412546, 0.0887472350830063, 0.12094161520681679, 0.12984951190462318, 0.42261958446022063, 0.43234804030150953, 0.15004231847567195, 0.4467511388747109, 0.1363325915774986, 0.21709320856499253, 0.05921888824571686, 0.48305858232510895, 0.2646002121564958, 0.05698867670178154, 0.35161944239063003, 0.11411290030671783, 0.2672385175839088, 0.2966396071307707, 0.05432699835769367, 0.0491806990951123, 0.23547958892843107, 0.012256373718315228, 0.2909308216293008, 0.15417300694676672, 0.27257184858826683, 0.0704226750278556, 0.3045027141272991, 0.2136852337397201, 0.4320743842385712, 0.4521756090109451, 0.34745770438203966, 0.23480837399637866, 0.2559891313398752, 0.32629546299344186, 0.47192356245579276, 0.04946362842617169, 0.40174192505144357, 0.1794533705877694, 0.47826395050995213, 0.07282219069224477, 0.1360934022804387, 0.141417696101935, 0.10678364566714005, 0.4987190654098726, 0.3584908025082392, 0.3480905017958233, 0.346312819345008, 0.2557647484932334, 0.09624975987538853, 0.21525867415878042, 0.006095140167895974, 0.1252813960773312, 0.13328212561442493, 0.2336099306603125, 0.27282659643650636, 0.3349754335692699, 0.18462804910238895, 0.33158948175521763, 0.32434770982761907, 0.08132157628264058, 0.4642276077846495, 0.13195944320894387, 0.4301143235063727, 0.0665753701706715, 0.38665410369750897, 0.4399902643522986, 0.01805089992807618, 0.07366164117484764, 0.3395886844277452, 0.3317110206581367, 0.20481733076936126, 0.17063055051229176, 0.23265272401277803, 0.26271381298076035, 0.3543995000686727, 0.1556009342358452, 0.11161580358623224, 0.4763540845891127, 0.3419656599194071, 0.10924408277231956, 0.30802911035263314, 0.32118977230923157, 0.33991863027418834, 0.2911544488825147, 0.23611578428060226, 0.4002949163985162, 0.3209473429169308, 0.06440413369416265, 0.2748935070752928, 0.4919103340314976, 0.4472576002809434, 0.49241085538647034, 0.3868882249844612, 0.4629415691285299, 0.15190369669834353, 0.26879660423252655, 0.21206537938254433, 0.07001455910857651, 0.13293720261180614, 0.3011573239851033, 0.4036165377400697, 0.12891669573889897, 0.2100592526866616, 0.10012512825981462, 0.03536237028641365, 0.41604730830475034, 0.23206862707337933, 0.23005421508532903, 0.4881447590563639, 0.48338527141366605, 0.14490549131704872, 0.4804683052341737, 0.23241872917549955, 0.06605035201016696, 0.47467193480748515, 0.1270490587968336, 0.35637585870267463, 0.0459539963443204, 0.027967186529142596, 0.0718912933438412, 0.007304855206944572, 0.338761143872289, 0.4653000800093371, 0.47049856056709904, 0.21209443335353562, 0.38715161575240653, 0.36051340452709324, 0.18936208885225575, 0.07202876481784698, 0.11249074053916297, 0.40354622695602665, 0.209678302903331, 0.4319303766898639, 0.1654152312489423, 0.0393042294434659, 0.45843873219900505, 0.12154108633890631, 0.4984997638416059, 0.39264015950157855, 0.1187017015731337, 0.2041090320706157, 0.16173891637735693, 0.13429035264891404, 0.4669222946627031, 0.22017775244472515, 0.4820211925607668, 0.25419020284951255, 0.12385779728238011, 0.09241173958119475, 0.43756552781603664, 0.08308267936080826, 0.036696390891559294, 0.338065714232264, 0.2012047288881687, 0.02913742606717601, 0.4523255304916582, 0.11703599959724409, 0.49432734890533575, 0.25473105181126277, 0.09799413388853961, 0.06577800915473775, 0.3927555590954236, 0.40624722840656635, 0.3700397624931954, 0.4839061966452981, 0.15171271753721438, 0.14416821521792106, 0.13866056501003943, 0.19279890750888407, 0.4030843108438292, 0.3442104258462181, 0.1738067469837562, 0.10330186681284359, 0.4459131905776521, 0.04366259381233084, 0.37737515000387856, 0.044819018983372705, 0.3875773005501073, 0.30940960548054125, 0.1120782227427567, 0.4894487181633105, 0.2717968689923859, 0.36034775912167183, 0.4708306191464488, 0.3392786167802858, 0.0721500617130506, 0.054540969704960085, 0.42458839786425623, 0.0805697273162077, 0.10141786500166755, 0.3870669749143307, 0.39830255111485574, 0.1838751050832288, 0.2511103847204543, 0.47521823905423927, 0.2741499051344266, 0.15906048702721692, 0.11591650637814327, 0.2605748995938231, 0.4561711061375577, 0.4502056685288549, 0.08549808524336333, 0.1659842153654278, 0.33905357060436886, 0.2108687501055851, 0.46663330495743544, 0.43394922357979115, 0.0033027675366405496, 0.1030760050909385, 0.025961875228042386, 0.14943033693493712, 0.42183711692953096, 0.3412346496742544, 0.16503276711881715, 0.256675811828815, 0.3986840746012871, 0.13918272777778862, 0.4107586771152846, 0.40411275094201865, 0.4477694801528587, 0.13615151538515624, 0.47681528989634864, 0.4060894966442882, 0.2994039580525578, 0.002356832116035157, 0.006134325920461703, 0.015726588632394345, 0.4194446065480084, 0.33158288839157224, 0.22423675081668687, 0.3683079373660894, 0.4709117207121332, 0.21678482537610727, 0.32914468104453337, 0.13490494103899947, 0.4794409107097097, 0.4276932119114954, 0.44903678053353324, 0.3714692993754132, 0.3694854811566156, 0.4491357548776359, 0.3774813411962376, 0.28521573166425107, 0.11445273898687669, 0.4753206263640075, 0.24573642838841964, 0.31800814657221854, 0.15515312148476967, 0.3484685653285696, 0.08903835788297482, 0.3445759026214782, 0.30480916949187215, 0.0333644641645785, 0.11338887974138484, 0.05516314494175106, 0.08987174568361028, 0.20449623465885197, 0.3881310245730331, 0.34176770127728484, 0.13584691566393114, 0.032867170709950155, 0.274352705168108, 0.437751931865791, 0.4338331641244159, 0.09985346707522669, 0.01336082188870702, 0.04315738487774884, 0.044919727297683454, 0.268011321821034, 0.41251355980881366, 0.018298176399369148, 0.29242644693600567, 0.07122562140252653, 0.1893743043589875, 0.3923707464887694, 0.30474353221752404, 0.20884653420098354, 0.4737529122936724, 0.016013677842789675], 
    #     'replicas': [5, 0, 4, 4, 3, 4, 1, 4, 3, 5, 1, 4, 1, 5, 3, 1, 1, 0, 0, 4, 2, 2, 2, 0, 1, 2, 1, 2, 5, 2, 2, 5, 3, 1, 2, 5, 5, 2, 0, 1, 4, 5, 5, 1, 0, 4, 0, 4, 3, 3, 5, 5, 2, 2, 3, 3, 0, 0, 1, 0, 0, 3, 0, 0, 4, 2, 3, 3, 0, 2, 1, 2, 5, 1, 0, 4, 2, 4, 2, 3, 5, 4, 3, 0, 5, 1, 4, 1, 0, 1, 4, 5, 2, 3, 1, 1, 1, 1, 2, 4, 3, 5, 5, 2, 3, 3, 3, 3, 4, 1, 0, 4, 4, 0, 1, 1, 0, 1, 0, 1, 1, 2, 3, 0, 5, 2, 3, 5, 3, 4, 5, 4, 1, 0, 0, 1, 1, 3, 0, 2, 2, 4, 4, 2, 3, 2, 2, 5, 0, 2, 2, 2, 1, 5, 0, 5, 3, 5, 1, 5, 4, 3, 2, 0, 2, 2, 3, 5, 0, 0, 2, 0, 1, 0, 0, 2, 3, 1, 5, 4, 2, 1, 0, 3, 4, 2, 3, 4, 3, 3, 0, 1, 4, 3, 4, 1, 3, 1, 4, 4, 4, 3, 5, 0, 4, 2, 5, 5, 2, 4, 1, 5, 4, 5, 1, 4, 1, 0, 3, 5, 2, 2, 3, 0, 3, 2, 5, 5, 2, 4, 1, 0, 5, 2, 5, 4, 2, 1, 0, 5, 1, 5, 0, 1, 1, 5, 3, 4, 5, 1, 2, 1, 3, 1, 1, 1, 2, 0, 2, 0, 1, 5, 2, 0, 2, 1, 0, 1, 0, 4, 0, 3, 0, 3, 1, 4, 5, 2, 4, 2, 5, 2, 0, 4, 3, 4, 4, 0, 2, 5, 0, 5, 3, 4, 1, 4, 1, 5, 4, 2, 1, 3, 4, 3, 1, 3, 3, 0, 2, 4, 2, 5, 5, 5, 3, 1, 0, 5, 1, 0, 5, 4, 2, 5, 3, 3, 2, 2, 4, 2, 3, 5, 3, 1, 3, 1, 2, 2, 5, 5, 1, 4, 1, 3, 1, 1, 2, 5, 4, 1, 4, 0, 2, 3, 2, 5, 5, 5, 2, 4, 5, 3, 2, 0, 1, 1, 4, 5, 0, 4, 5, 1, 5, 1, 2, 5, 2, 2, 4, 2, 5, 2, 2, 2, 4, 0, 0, 4, 2, 5, 4, 0, 4, 0, 0, 2, 2, 3, 5, 2, 1, 2, 4, 2, 4, 2, 0, 3, 4, 2, 3, 0, 2, 4, 2, 5, 1, 2, 4, 4, 0, 4, 4, 2, 0, 3, 1, 4, 1, 3, 0, 3, 1, 5, 3, 2, 1, 4, 4, 0, 2, 0, 5, 3, 1, 4, 1, 4, 0, 4, 5, 0, 0, 4, 3, 1, 1, 3, 3, 0, 0, 5, 1, 1, 1, 4, 5, 5, 2, 0, 3, 5, 5, 4, 1, 1, 5, 3, 1, 2, 0, 5, 3, 2, 4, 3, 4, 1, 3, 1, 1, 3, 4, 2, 4, 5, 0, 0, 4, 3, 3, 5, 0, 1, 2, 4, 2, 1, 1, 5, 0, 1, 5, 5, 5, 2, 5, 4, 3, 0, 3, 1, 1, 5, 0, 1, 3, 1, 2, 1, 2, 5, 0, 4, 3, 0, 3, 0, 3, 4, 4, 4, 0, 4, 1, 0, 1, 4, 1, 2, 1, 5, 3, 4, 3, 2, 4, 5, 3, 3, 4, 1, 1, 1, 1, 2, 2, 1, 4, 5, 5, 3, 5, 5, 2, 5, 3, 3, 3, 0, 4, 5, 2, 0, 0, 4, 3, 0, 1, 5, 5, 4, 0, 4, 5, 2, 1, 5, 3, 3]
    # }

    # test4 main_init(100, 1.0, 600)
    # init_popu={
    #     'h_m_cost': [[0.4, 1.0, 0.7, 0.8, 0.7, 0.7, 0.7, 0.8, 0.8, 1.0, 0.3, 0.7, 0, 0.8, 1.0, 0, 0, 0, 0, 0.4, 0.8, 0.3, 0.7, 0, 1.0, 0.7, 0.8, 0, 0, 0.5, 1.0, 0, 1.0, 0.7, 1.0, 0.3, 0.3, 0, 0.7, 0.8, 0, 0.5, 1.0, 0.8, 0.5, 0.4, 0, 1.0, 0, 0.7, 1.0, 0.7, 1.0, 0, 1.0, 0.5, 0, 0, 0, 0, 0, 1.0, 0, 1.0, 0, 0.4, 0, 0.5, 0, 0.5, 0, 0.7, 1.0, 0.3, 0, 0.4, 0.5, 0, 1.0, 0.4, 0.7, 1.0, 0.8, 0.8, 0.7, 0, 0.7, 0.8, 0.3, 0, 1.0, 0.4, 0, 0, 0, 1.0, 0.8, 0.8, 0.5, 0]],
    #     'map_v_h': {1: 24, 2: 76, 5: 87, 6: 75, 7: 51, 11: 67, 13: 45, 14: 2, 15: 98, 16: 21, 17: 7, 18: 39, 19: 8, 20: 1, 21: 54, 22: 3, 23: 47, 24: 13, 25: 35, 26: 38, 27: 30, 28: 10, 29: 42, 30: 97, 33: 83, 34: 4, 35: 5, 36: 80, 37: 52, 38: 41, 39: 88, 42: 63, 44: 73, 45: 69, 46: 50, 47: 91, 48: 0, 51: 43, 52: 20, 54: 33, 55: 34, 56: 36, 57: 32, 60: 96, 61: 87, 62: 61, 63: 14, 65: 82, 66: 25, 67: 71, 68: 72, 70: 86, 71: 65, 73: 79, 75: 82, 78: 55, 79: 22, 80: 84, 84: 78, 85: 95, 86: 44, 87: 9, 88: 29, 90: 90, 91: 81, 92: 19, 94: 11, 95: 13, 96: 6, 97: 26, 99: 49},
    #     'c_rp': [0.08842445714323327, 0.24298933012067692, 0.34088013601516315, 0.04097621572126686, 0.018820021352209504, 0.152297198280397, 0.4281096282078699, 0.4295411055902934, 0.11413102264306979, 0.3462746907264091, 0.04713200603823664, 0.003555114858038999, 0.003179312292815095, 0.3217853560154278, 0.39158869907213384, 0.06207193063840444, 0.24438104165348346, 0.426952787019608, 0.49581293601263676, 0.38912383537690204, 0.4834548686764092, 0.051821921601362286, 0.3533709405757324, 0.4542852829293737, 0.13023885038239263, 0.061856663318853256, 0.061782776896783576, 0.2802787248360272, 0.1432137620676452, 0.18023481172288358, 0.41363615539555143, 0.3143605098191813, 0.11022940073553217, 0.43550370008811684, 0.3450924686119305, 0.4435534211470765, 0.25415161200529895, 0.12449226170742933, 0.29760486799664426, 0.24247146510895962, 0.3147434685667298, 0.008163965985240718, 0.09560952342421647, 0.08144879477239925, 0.0786137116851704, 0.44855339237533126, 0.4830157216846543, 0.11374587630573763, 0.339740267676539, 0.30840647258410264, 0.27763741910469003, 0.3352728396328562, 0.22257472690993602, 0.3068698739769306, 0.018409976469132006, 0.33876715014046516, 0.23007825760798528, 0.4780706715210897, 0.12370564875222306, 0.317047815039857, 0.06633742062666975, 0.04012224148112181, 0.26273622784577394, 0.3976765501646962, 0.19911832132510554, 0.24914482929336268, 0.45328189167190713, 0.12768761598780942, 0.07385829489708295, 0.3923456049372886, 0.16023055034240735, 0.20841900628158666, 0.13898888204686266, 0.24308404042023463, 0.023982713739980455, 0.032291703569933716, 0.008956432716607676, 0.3890571493633152, 0.4897360564529616, 0.019082118291013195, 0.1913919868448592, 0.15685539147466748, 0.042419138156640224, 0.4583792966535008, 0.2068803984997724, 0.11703485368302652, 0.4531139318481376, 0.35122219117644765, 0.06236806184255517, 0.1563069576209677, 0.4318679821418131, 0.4614289409299957, 0.26319832524126396, 0.47746032012406714, 0.2811109901997292, 0.20328545709753826, 0.3287924856505744, 0.3020806748122359, 0.0628553676701003, 0.2507387167478661],
    #     'v_m_cost': [[0, 0.5006404426597831, 0.3551390971387739, 0, 0, 0.15763640907189, 0.015585869932769641, 0.6637056105307766, 0, 0, 0, 0.48809544760222556, 0, 0.18946281156325337, 0.5489571628220838, 0.1202268901185698, 0.2833155911623858, 0.37269634901467946, 0.4098084736525661, 0.20508251251291984, 0.8153830028160698, 0.8165974376871264, 0.4270916354559559, 0.317410075689167, 0.2146497528180288, 0.26344821347408653, 0.3357849540722271, 0.9760836922068616, 0.18886802899387495, 0.2662763314224518, 0.3773359315349568, 0, 0, 0.20278952874417888, 0.048243107227829124, 0.39381453305464065, 0.1996712439328018, 0.13653755618084423, 0.22301308973226328, 0.18397307539467353, 0, 0, 0.5954212403654529, 0, 0.06035390311663391, 0.03052698250626773, 0.4490322523012266, 0.25553004075196994, 0.29018790018211743, 0, 0, 0.026434521889260737, 0.3850527912516264, 0, 0.46917009137535215, 0.021084149357563836, 0.1673235919698532, 0.40831569290785263, 0, 0, 0.7767052636303072, 0.38463403909803284, 0.42317297062001236, 0.20690133354788645, 0, 0.38220499902219307, 0.0027182299073384153, 0.5122465251372678, 0.6397595551459636, 0, 0.6311428269960646, 0.31065282080759943, 0, 0.3704653766870326, 0, 0.34123184467401957, 0, 0, 0.3055411933766752, 0.2814575349653164, 0.4497043538845107, 0, 0, 0, 0.26356526910799594, 0.5086009674466165, 0.07972855111638666, 0.93138526915483, 0.23069938818441754, 0, 0.5134558315572426, 0.05968991240287805, 0.27754702859938474, 0, 0.19861463126522833, 0.04088325488706265, 0.6486667338293619, 0.19377698093460013, 0, 0.45460988522668144]],
    #     'v_rm': [0.7, 1.0, 0.5, 0.3, 0.8, 0.4, 0.4, 0.7, 0.8, 0.8, 0.4, 0.5, 0.3, 0.4, 0.7, 0.5, 0.3, 0.8, 0.8, 0.8, 1.0, 1.0, 0.8, 1.0, 0.4, 0.3, 0.7, 1.0, 0.3, 1.0, 0.8, 0.4, 0.5, 0.8, 0.7, 0.7, 0.7, 1.0, 0.5, 0.3, 0.5, 0.8, 1.0, 0.5, 0.3, 0.5, 1.0, 0.4, 0.4, 0.7, 0.7, 0.8, 0.8, 1.0, 0.7, 1.0, 0.3, 1.0, 0.8, 0.8, 0.8, 0.4, 1.0, 1.0, 0.3, 0.4, 0.7, 0.7, 1.0, 1.0, 0.7, 0.4, 0.3, 0.4, 0.8, 0.4, 0.7, 0.7, 0.5, 0.7, 0.7, 0.5, 0.4, 0.8, 1.0, 1.0, 0.5, 1.0, 0.5, 0.7, 1.0, 1.0, 0.4, 0.8, 0.7, 0.4, 0.7, 0.8, 0.3, 0.7],
    #     'h_p_cost': [[0.5, 1.0, 0.8, 1.0, 0.8, 0.8, 0.8, 1.0, 1.0, 1.0, 0.3, 0.8, 0, 1.0, 1.0, 0, 0, 0, 0, 0.5, 1.0, 0.3, 0.8, 0, 1.0, 0.8, 1.0, 0, 0, 0.6, 1.0, 0, 1.0, 0.8, 1.0, 0.3, 0.3, 0, 0.8, 1.0, 0, 0.6, 1.0, 1.0, 0.6, 0.5, 0, 1.0, 0, 0.8, 1.0, 0.8, 1.0, 0, 1.0, 0.6, 0, 0, 0, 0, 0, 1.0, 0, 1.0, 0, 0.5, 0, 0.6, 0, 0.6, 0, 0.8, 1.0, 0.3, 0, 0.5, 0.6, 0, 1.0, 0.5, 0.8, 1.0, 1.0, 1.0, 0.8, 0, 0.8, 1.0, 0.3, 0, 1.0, 0.5, 0, 0, 0, 1.0, 1.0, 1.0, 0.6, 0]],
    #     'c_rm': [0.20278952874417888, 0.04226072756106394, 0.317410075689167, 0.19861463126522833, 0.07118103753337754, 0.09750407448130247, 0.37269634901467946, 0.2814575349653164, 0.13045342206460403, 0.4098084736525661, 0.1913570755032764, 0.2146497528180288, 0.12251467821497239, 0.3055411933766752, 0.3495180965766584, 0.13787486352776715, 0.19377698093460013, 0.48809544760222556, 0.3773359315349568, 0.4761758850931548, 0.46917009137535215, 0.05968991240287805, 0.34123184467401957, 0.41987581418197806, 0.13323525074762174, 0.048243107227829124, 0.13641908562919758, 0.49312317785637555, 0.22083179436571826, 0.21619827696568547, 0.4497043538845107, 0.38463403909803284, 0.07972855111638666, 0.4446217555103647, 0.25046650537823223, 0.25553004075196994, 0.43826209129845445, 0.03578949936541581, 0.30412143378727574, 0.21993974412783446, 0.4490322523012266, 0.13975672187279903, 0.1673235919698532, 0.0148962435559018, 0.24468170166648964, 0.31065282080759943, 0.4149445500303791, 0.06935610581639917, 0.3457250102960999, 0.3551390971387739, 0.26344821347408653, 0.4111981362889423, 0.04088325488706265, 0.4745706532859991, 0.12297020166868017, 0.27754702859938474, 0.1202268901185698, 0.25739544742544307, 0.20690133354788645, 0.44760747775270926, 0.021084149357563836, 0.026434521889260737, 0.3967216235051484, 0.28157329479302806, 0.15763640907189, 0.20508251251291984, 0.45460988522668144, 0.06284983001903924, 0.22301308973226328, 0.42317297062001236, 0.12651960954965275, 0.1597880365047012, 0.03052698250626773, 0.0974641374367958, 0.015585869932769641, 0.21609813277806736, 0.18886802899387495, 0.3357849540722271, 0.3704653766870326, 0.18397307539467353, 0.1996712439328018, 0.0027182299073384153, 0.18946281156325337, 0.40831569290785263, 0.06883407604687788, 0.1858115166810833, 0.3655071273413649, 0.28051023787663065, 0.10074805681542842, 0.023765223278963604, 0.46998579757620385, 0.25777316404829864, 0.339207117722915, 0.35582986036294756, 0.30294172353326193, 0.24286727861148452, 0.3449547349872206, 0.26356526910799594, 0.06035390311663391, 0.31935516900315386], 
    #     'v_rp': [0.8, 1.0, 0.6, 0.3, 1.0, 0.5, 0.5, 0.8, 1.0, 1.0, 0.5, 0.6, 0.3, 0.5, 0.8, 0.6, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.3, 0.8, 1.0, 0.3, 1.0, 1.0, 0.5, 0.6, 1.0, 0.8, 0.8, 0.8, 1.0, 0.6, 0.3, 0.6, 1.0, 1.0, 0.6, 0.3, 0.6, 1.0, 0.5, 0.5, 0.8, 0.8, 1.0, 1.0, 1.0, 0.8, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.3, 0.5, 0.8, 0.8, 1.0, 1.0, 0.8, 0.5, 0.3, 0.5, 1.0, 0.5, 0.8, 0.8, 0.6, 0.8, 0.8, 0.6, 0.5, 1.0, 1.0, 1.0, 0.6, 1.0, 0.6, 0.8, 1.0, 1.0, 0.5, 1.0, 0.8, 0.5, 0.8, 1.0, 0.3, 0.8],
    #     'v_p_cost': [[0, 0.664714398027534, 0.30840647258410264, 0, 0, 0.19911832132510554, 0.023982713739980455, 0.34933951860979073, 0, 0, 0, 0.426952787019608, 0, 0.042419138156640224, 0.5861428604825858, 0.23007825760798528, 0.2693320519634235, 0.4281096282078699, 0.3462746907264091, 0.24914482929336268, 0.652322160618166, 0.7170215107751476, 0.31601484446577627, 0.34088013601516315, 0.003555114858038999, 0.27763741910469003, 0.3890571493633152, 0.9470178892505865, 0.008956432716607676, 0.16839451632764807, 0.49581293601263676, 0, 0, 0.08842445714323327, 0.061856663318853256, 0.5398534484178732, 0.1913919868448592, 0.1868603235499845, 0.07385829489708295, 0.019082118291013195, 0, 0, 0.6738849542625049, 0, 0.0628553676701003, 0.13898888204686266, 0.3147434685667298, 0.4435534211470765, 0.2569596383733828, 0, 0, 0.04012224148112181, 0.06913133968326124, 0, 0.4834548686764092, 0.06633742062666975, 0.09560952342421647, 0.4583792966535008, 0, 0, 0.7883867714809938, 0.3143605098191813, 0.3923456049372886, 0.12370564875222306, 0, 0.3784263327356755, 0.15685539147466748, 0.67485731226249, 0.7141387279967903, 0, 0.6632505334075378, 0.44855339237533126, 0, 0.4897360564529616, 0, 0.3533709405757324, 0, 0, 0.3217853560154278, 0.4295411055902934, 0.41363615539555143, 0, 0, 0, 0.3020806748122359, 0.6209810455348708, 0.11022940073553217, 0.5344303368413261, 0.37332289080262726, 0, 0.6423840985878893, 0.051821921601362286, 0.33876715014046516, 0, 0.04097621572126686, 0.22257472690993602, 0.6208512578762682, 0.24438104165348346, 0, 0.45328189167190713]],
    #     'population': [[[33, 83], [67, 71], [23, 47], [94, 11], [52, 20], [16, 21], [17, 7], [79, 22], [68, 72], [18, 39], [52, 20], [24, 13], [52, 20], [78, 55], [68, 72], [85, 95], [97, 26], [11, 67], [30, 97], [20, 1], [54, 33], [91, 81], [75, 82], [21, 54], [88, 29], [34, 4], [35, 5], [87, 9], [48, 0], [70, 86], [80, 84], [61, 87], [86, 44], [90, 90], [42, 63], [47, 91], [87, 9], [37, 52], [22, 3], [27, 30], [46, 50], [29, 42], [56, 36], [85, 95], [14, 2], [71, 65], [70, 86], [48, 0], [96, 6], [2, 76], [25, 35], [60, 96], [95, 13], [27, 30], [22, 3], [92, 19], [15, 98], [35, 5], [63, 14], [7, 51], [55, 34], [51, 43], [21, 54], [27, 30], [5, 87], [19, 8], [99, 49], [65, 82], [38, 41], [62, 61], [29, 42], [68, 72], [45, 69], [88, 29], [6, 75], [7, 51], [28, 10], [26, 38], [73, 79], [39, 88], [36, 80], [66, 25], [13, 45], [57, 32], [90, 90], [16, 21], [60, 96], [14, 2], [37, 52], [14, 2], [67, 71], [1, 24], [20, 1], [85, 95], [96, 6], [1, 24], [42, 63], [84, 78], [44, 73], [65, 82]]]
    # }
    # addtion0={
    #     'c_rm': [0.4341373163741744, 0.4391874199529058, 0.1815590600710043, 0.07983945311569218, 0.08180604141788272, 0.2714826709716919, 0.4260045322938967, 0.16050242910726992, 0.37302961481837105, 0.39032685749561113, 0.4456608401104697, 0.22763461854567021, 0.1281446187494433, 0.17815741406227806, 0.09340434637257891, 0.47641850347703296, 0.08665686837023673, 0.10087217834148784, 0.049671084931952075, 0.12386481827322246, 0.016187549456153, 0.04806465890914585, 0.235047284365511, 0.0721808923751211, 0.07746058691287211, 0.16647446302367594, 0.37970307715354756, 0.2674371088424349, 0.2005789844226692, 0.3589872944323365, 0.3385048345498892, 0.4856502538996235, 0.4908903347888547, 0.010141874988897098, 0.17240906111833432, 0.35500986495716624, 0.4318150466250418, 0.46715508737728767, 0.03314811187317976, 0.3176359829702486, 0.33238887427168284, 0.21960507771370966, 0.09118396009064086, 0.1374705472425603, 0.04749008619585182, 0.0010886392795413091, 0.4298021863452083, 0.036931008273408034, 0.4363610374092104, 0.4833740253821541, 0.4923705566952111, 0.18384447943168558, 0.015311693102248114, 0.06699083975831069, 0.2602786709486508, 0.4078123519119704, 0.2604316955167323, 0.2065879060747725, 0.06837300480660391, 0.16899359015949253, 0.34910188804056175, 0.1645827431520349, 0.25426902371850835, 0.27100669636124164, 0.338650069889712, 0.23359250637917975, 0.11665369477934195, 0.18909264465188289, 0.45194199139444413, 0.38613460403223676, 0.1805869766652855, 0.01620941504632828, 0.03918127832197568, 0.20827679727781334, 0.12264569335111314, 0.17978708629695248, 0.03625236220587255, 0.3216814015357734, 0.4099673762061271, 0.3411528495497662, 0.281180929627144, 0.12937182855691357, 0.13519558438146556, 0.26190158922982465, 0.031339258083451116, 0.3094129065430831, 0.27315630964090143, 0.13991145051902332, 0.11567792322107776, 0.1027692326016802, 0.3481648219318248, 0.1749636337545894, 0.4461169753432552, 0.15582391802192988, 0.09867527623991149, 0.26382792348018147, 0.4791777930651397, 0.4465506509474274, 0.21191654287039574, 0.3172854037127778, 0.47334204624232135, 0.18165920431995713, 0.257042965662336, 0.2057793868354449, 0.14369885842894026, 0.36856634378039, 0.04542626067610786, 0.4706039873541975, 0.2845861374960259, 0.04438372488454573, 0.44423840718926433, 0.2161332934926368, 0.23108525299794014, 0.4439788302097268, 0.39618837362118464, 0.29546297784261066, 0.0673591383284291, 0.3857482392739995, 0.2420556854170846, 0.22555303787178044, 0.03001539962414676, 0.09957681973742363, 0.23828779459849564, 0.4148545733184974, 0.4452667775718228, 0.4951007204576531, 0.29033489846095994, 0.4820212505566647, 0.004377043383131052, 0.42293882586953135, 0.42731642888940613, 0.3186361477844746, 0.4669731563098549, 0.4659656776601818, 0.041412640998128886, 0.10523415004470868, 0.15634469231598347, 0.4466523128567166, 0.17262344495486764, 0.030963013623434094, 0.13342556650525697, 0.1406785213765496, 0.2020415195241665, 0.32133223139214356, 0.26852909121457547, 0.0035427268416318713, 0.1579416153187106, 0.46225199823960356, 0.2253450913398126, 0.23106888999186515, 0.11866809746050164, 0.0714826607263731, 0.24435158756993036, 0.2542846987700641, 0.1768726623204408, 0.46655537342852516, 0.20523150279042185, 0.32713841367314694, 0.40299442104264155, 0.07213418835035701, 0.33188055842789943, 0.32513296880864817, 0.24120993391071163, 0.28282892839197593, 0.2914948291679289, 0.34002746190792343, 0.18047626860514776, 0.03688511629773544, 0.15998904463062952, 0.16669385186923052, 0.4203779218224919, 0.3731480902812213, 0.028633600602445575, 0.14884214374366048, 0.4663214060828616, 0.4205483132142317, 0.08732984289500684, 0.45051188235097916, 0.17401062272521392, 0.41723204224150906, 0.2585109572553211, 0.15200752560675004, 0.14780594605766176, 0.06979955546358058, 0.23823950950187936, 0.34020687324720716, 0.14632172328179913, 0.18276152613283705, 0.30526662232075175, 0.3970050132133891, 0.13629954654767215, 0.2755635100723379, 0.3756773630549971, 0.24450953837308834, 0.31980969144276766, 0.0013250931863523219, 0.10007458144604359, 0.4448676886933074, 0.10691123009472228, 0.38736362855033724, 0.059193088619210715, 0.3305345540253729, 0.09816703571211863, 0.3902576837969616, 0.49813858980266423, 0.26962603624555104, 0.3139186441140772, 0.04670092589665134, 0.35184206622525627, 0.04832398023162565, 0.1363685850481038, 0.05591216003910321, 0.4795724399332207, 0.09108495230392602, 0.4022524929776097, 0.23226171914885227, 0.4284656537210433, 0.14113433050478885, 0.14985428707615286, 0.461328405969762, 0.03631687576761386, 0.35897683483651066, 0.38458675719447544, 0.19800325261462565, 0.41290011013206035, 0.11064583999017363, 0.1579010138838252, 0.13803163072407212, 0.18440040844574712, 0.007109107788671382, 0.15087526893376427, 0.1053902720941147, 0.22277532122770688, 0.21253900213017177, 0.17175695248332518, 0.1434660529549266, 0.17380714368270211, 0.476031792346014, 0.3511462946564451, 0.2671545385128926, 0.019380416403917772, 0.3771346458135999, 0.29583876958879857, 0.35431586850683466, 0.3033247985173886, 0.26610002818594813, 0.20915183344350857, 0.4847582415158057, 0.3671740143196036, 0.13424488163498763, 0.37548751267919644, 0.13123909758342475, 0.41577769197443, 0.273220776612659, 0.40047658960031873, 0.061769421492425064, 0.48968576087134696, 0.4044176529935346, 0.32437814477994875, 0.16874770962842567, 0.33519573945513625, 0.3400536948836145, 0.28398896111005784, 0.036044713054917105, 0.312766257407902, 0.26644266368750036, 0.2289615453917039, 0.25913860576244674, 0.16917777664034228, 0.47334750726368446, 0.23186255691841914, 0.11151425209813298, 0.010399107317567852, 0.007039197215533088, 0.4656949644617879, 0.24798704145434494, 0.3603783532143241, 0.10086074313608351, 0.48320587791739944, 0.49848762802564694, 0.12659845504813633, 0.39885647972933197, 0.13423066687978666, 0.07578582898452504, 0.4372152647371183, 0.0604740251805401, 0.04592547992511048, 0.26360140302108, 0.08676174455975302, 0.34316617455480364, 0.39198002048655023, 0.019549475968311053, 0.26388812047948346, 0.24285258177233293, 0.13531791878460103, 0.0012994867905184448, 0.4739663133779577, 0.24668346832781618, 0.29622947644195574, 0.38768944819075635, 0.2845627913482597, 0.4730822554855182, 0.240490776242916, 0.013428186932793323, 0.3948438457539039, 0.43489500822115423, 0.15911993156780024, 0.11587028002955685, 0.0499853712991819, 0.12649880194863325, 0.4461215048164529, 0.22390482505035217, 0.2921977994956787, 0.015242361888278239, 0.09094365805613588, 0.047766232864177166, 0.3959611145976696, 0.34947990906152004, 0.17240064721691328, 0.3674318969875229, 0.16044342384874097, 0.3063131625018689, 0.12631035005397892, 0.3826972951007581, 0.23822576237399878, 0.25469733920804116, 0.15699335137971931, 0.17706230244147095, 0.16690747802164732, 0.058156923945404504, 0.08498531822755115, 0.2005310530574805, 0.13640658468916217, 0.038162246888347684, 0.02225270342738861, 0.26409089840752553, 0.21930248889868795, 0.005883782727331782, 0.008909909817539224, 0.2545947881700652, 0.20678869005978498, 0.08036091679506854, 0.19324023620475178, 0.4148270883509957, 0.25452418544412725, 0.25351728090353826, 0.30341839047707064, 0.42279317822374607, 0.10666892695985727, 0.18084064501593017, 0.440339006366697, 0.17190653165443615, 0.21701538378370772, 0.06452675501496521, 0.19226618485279398, 0.161409619169635, 0.10648447243403125, 0.43018043330610745, 0.2269705193788695, 0.4834545937333349, 0.3410280834441704, 0.10924592593165622, 0.21778702822626772, 0.05928788277468197, 0.25723759917649625, 0.19095088297220478, 0.20071555739848626, 0.03274505056949267, 0.48727004994342926, 0.03751832635725377, 0.01599708993417087, 0.27960823930197104, 0.1623108382258174, 0.3531565409170552, 0.4121288861246806, 0.4101591010355388, 0.3107073195244461, 0.07281207607118406, 0.16063608888226602, 0.2847391768644524, 0.42978193406779464, 0.3146802230124033, 0.1054539675664937, 0.34677162832302977, 0.06764100184363978, 0.39706182548183033, 0.14023214313211174, 0.424450030608367, 0.08605976836266674, 0.06296043363213713, 0.41990738035585673, 0.013608268688291042, 0.35965257968759934, 0.17618909226157173, 0.4318056630262379, 0.4469777269138716, 0.3997432480564511, 0.46208682949620383, 0.4724274588869832, 0.23896900413559474, 0.10696028442893049, 0.41856830893368496, 0.3119550314491345, 0.1329213367989931, 0.07938054795793972, 0.03300128745568995, 0.2944469990365327, 0.3387594485848491, 0.49616343634259763, 0.4970623516941335, 0.15526094443248514, 0.3881541585862206, 0.4387624714691105, 0.19954686959765913, 0.41790492075040875, 0.2818260919342991, 0.3820499799531886, 0.4280554658439626, 0.06404204558530557, 0.4922622864784181, 0.02764449853958617, 0.025195193453779074, 0.3437121086118294, 0.2540915873301863, 0.049271238664428535, 0.12237414326996654, 0.3618550894564764, 0.004859941317008648, 0.02287964794177616, 0.18124618395606304, 0.44878037814801797, 0.3365222470802247, 0.20699238089261138, 0.020011689533681903, 0.46005100742446714, 0.3362063736795262, 0.23000204141244732, 0.16596031531229868, 0.4541818424803238, 0.3111785467576673, 0.3810736887665763, 0.3929585144969664, 0.23727656178532522, 0.4124512581319058, 0.2697077293495662, 0.37531377375636643, 0.27643530320344606, 0.31107423099264037, 0.1445016814316304, 0.27809003857731207, 0.44560581540832356, 0.26265085509113306, 0.18725285610068618, 0.2263946361272016, 0.42076696295345895, 0.05687035507548696, 0.3753110238569564, 0.4172461577241904, 0.038019941818814434, 0.2517697115535711, 0.07193336235275036, 0.42795133933445206, 0.11908184150395926, 0.2744671341197829, 0.06479566448314925, 0.2527346154533051, 0.1125371458726408, 0.17485029330610247, 0.46642858183062597, 0.25629686222602055, 0.4341454208898906, 0.4967502349118252, 0.08304365586950752, 0.037281838631813585, 0.34167433200268427, 0.1672468780060215, 0.17422900151097664, 0.384550751298383, 0.30257564425832495, 0.2731950499954519, 0.4285709091678189, 0.2340296835269625, 0.16494351338998914, 0.2869915324322396, 0.23754599951239733, 0.49778026163798783, 0.4120918208111287, 0.25604608204067825, 0.25064353182334137, 0.08354229804904029, 0.22423177933054073, 0.49217869346903065, 0.4770945952862817, 0.49902403054258104, 0.46967653502356443, 0.061806159197027394, 0.021568188172867486, 0.07706202570495677, 0.11191424382272447, 0.16912371740804052, 0.04684840976157553, 0.19377182064340584, 0.16379580167291244, 0.16185946851760238, 0.12667002632472577, 0.4064505918186915, 0.022805344059521226, 0.24126965757500565, 0.35757781050562437, 0.36213608165590416, 0.497559105630491, 0.28201564580252103, 0.01949932374925828, 0.3235316107247993, 0.17858000828151324, 0.011152954323279646, 0.3589136325166349, 0.2177718366749374, 0.01518210444214349, 0.47223653954215994, 0.1051393120459807, 0.4555238598062442, 0.39476395312257834, 0.2870838474963595, 0.24712279929779596, 0.3089476719775908, 0.3508364111387735, 0.3028455864906183, 0.4297040400355442, 0.44964421632636564, 0.3728544942152286, 0.32546171427840964, 0.4620177288846856, 0.03977082987861058, 0.37254688268478575, 0.06618143989711867, 0.12538719826143255, 0.379308175897372, 0.09751202564154432, 0.28854602795176887, 0.1349418864249741, 0.25063639033782903, 0.3899642315524735, 0.4235186507679982, 0.3536441202630288, 0.4783704313365703, 0.030383940371719986, 0.030608578255666874, 0.10605414922954223, 0.1572908294267562, 0.45419047399847784, 0.11899092394643998, 0.024064084943416192, 0.3444132252539513, 0.07073991444889657, 0.4744192625055642, 0.2769929919016765, 0.4260534042716739, 0.19527741781716007, 0.19792999438995512, 0.2185947174322409, 0.017626680817700663, 0.2064243470137658, 0.2642624029522407, 0.3153784260483352, 0.31123019183510553, 0.4594395964095961, 0.06453156503894442, 0.010239053151281347, 0.36531350294916903, 0.01266826485899461, 0.46258334486156955, 0.011101898298647883, 0.34644503034807966, 0.09182968578283299, 0.2846083000849011, 0.4659417421074687, 0.0008051011477996084, 0.28149534507443136, 0.4817916910483454, 0.2284763708451705, 0.2869007344624175, 0.2773299927813995, 0.19405156210601773, 0.4861653124448618, 0.0768809445024799, 0.14576319491372233, 0.08558440515808635, 0.4505108831070689, 0.22966335562061466, 0.3545257060955245, 0.4733658235829372, 0.1599062657370443, 0.4519656993803757, 0.3559863029743281, 0.1931648047759695, 0.3047475582721111, 0.012623436098605806, 0.23560172214093839, 0.46559412895607866], 
    #     'c_rp': [0.4445804915722988, 0.4462616726042802, 0.19050241829660192, 0.09745624118640717, 0.24779440957530907, 0.48416889189014456, 0.30822091044932903, 0.20907758555071376, 0.3189377854216109, 0.4837757298181572, 0.36469596177001556, 0.08841488309187823, 0.12903763998374757, 0.048093456690973646, 0.09408709938791154, 0.4205475629270473, 0.15577375038690983, 0.20977663750270947, 0.06221794254390817, 0.12410839923148864, 0.06442781679404297, 0.11305900113727119, 0.005066384339071306, 0.02423883729006432, 0.2469975380222461, 0.21547432289279955, 0.4064241299448354, 0.4409086326274948, 0.177558842144924, 0.2800178445943123, 0.2976014557634893, 0.41406502692233016, 0.2610142657811617, 0.06552103962005018, 0.22698831962868848, 0.4943416291597215, 0.30667437257586366, 0.2900689354404872, 0.04857818024053534, 0.2637990066771307, 0.4015645767415761, 0.1454413490112172, 0.18393064458167624, 0.22052422703384755, 0.23887569277773735, 0.0013518393257293537, 0.386153303119479, 0.15855492518690306, 0.4375526904427461, 0.4270053904093479, 0.2995928463330386, 0.21271423887431035, 0.2475277099512042, 0.15423174360588537, 0.3077061066677872, 0.38915797155320825, 0.40311784086202435, 0.23345146967490132, 0.04899900569952892, 0.23999044477907217, 0.4051810401329355, 0.12715124671688455, 0.46735728775127333, 0.3169239614404497, 0.4962711259440799, 0.2395423210680916, 0.012698959492209727, 0.0033097346912891457, 0.31383679457321767, 0.26200867828961005, 0.1745724347409901, 0.17747131671337446, 0.08956268883943364, 0.18524392126369255, 0.22700695500138363, 0.13223465525568667, 0.05568505514897443, 0.31036831162888295, 0.3225492167994602, 0.26456231371144234, 0.4509754298536055, 0.20702185425232456, 0.02173878530065365, 0.4808994508631613, 0.14139710037249936, 0.37176976773320153, 0.43878527664986944, 0.15284018969575747, 0.04527605545851576, 0.05657693967388522, 0.3616607065408003, 0.2206033667296658, 0.27295904356199574, 0.14375902693766618, 0.13516111694850036, 0.3695344854602668, 0.30111559616562017, 0.3775158908838023, 0.012123495890990876, 0.4777496924717282, 0.42791170689847186, 0.0973515536509767, 0.2902012985124138, 0.03988785939255057, 0.03701494818089579, 0.4869730956888012, 0.1867945256328129, 0.36470804708547067, 0.4102064417346739, 0.22089599439513413, 0.459615756651926, 0.09320779157314824, 0.20124041287157757, 0.4019024403319752, 0.29731095820263437, 0.3545107743835226, 0.15945331168698856, 0.31363566647664787, 0.05862114359541454, 0.19280511196266142, 0.19218043772882304, 0.23752169027471787, 0.23562868769819362, 0.4797837814204451, 0.2875256048739332, 0.47728820330546323, 0.3638227360843275, 0.480683340228037, 0.10143954703404251, 0.3388677821956998, 0.4797535988365291, 0.2740302861947357, 0.3731389847696313, 0.46887916311058847, 0.12264208344850175, 0.14975621577132459, 0.23199921711891797, 0.4595306348637271, 0.2205407267816753, 0.12479308710630987, 0.007777797641692563, 0.05746236327404469, 0.042652107925625515, 0.46720791250630106, 0.39116493810264824, 0.025120369303446966, 0.04481331629222585, 0.3603354923777105, 0.13155031523026356, 0.2035428791523407, 0.23272771241080548, 0.14766823332801643, 0.23354433728367358, 0.2536850204913688, 0.20664460540770235, 0.3452083116498826, 0.12281684176475882, 0.2788511969305388, 0.43023510652002644, 0.04148797706583529, 0.4732646662483657, 0.26090011678894925, 0.11095147876524514, 0.47251444786864416, 0.3268350085229261, 0.45406617494196183, 0.002649960755467362, 0.23366678740489755, 0.12004487541483505, 0.04589520195701424, 0.43927100662226676, 0.2509111613399078, 0.11256174643630856, 0.023522397341845247, 0.38835269286392526, 0.35895063482293216, 0.027034995345454838, 0.40964885163263787, 0.1610884364077173, 0.3918587013014428, 0.2901626507012722, 0.059529911954777026, 0.21435492341309514, 0.08183360689928354, 0.02025325601048783, 0.276990738422874, 0.22173442667625598, 0.17071130000287088, 0.3141637647273648, 0.26220206312326194, 0.10501598769333342, 0.3255598893497854, 0.42450970050186426, 0.24497817603269295, 0.43495076802724253, 0.07247667116224243, 0.05410284813599342, 0.4064314049301117, 0.13123244664197553, 0.30917963574933016, 0.14245068433544478, 0.28119484461293337, 0.2154237147950414, 0.48629187337488333, 0.27547179078459955, 0.3219473779180879, 0.42762052385765975, 0.2289117754822128, 0.28046990496509155, 0.15205798978245993, 0.027516922694208246, 0.010419186878624753, 0.43265164794892674, 0.09179067818863273, 0.34430425634973155, 0.20243920154395134, 0.32588468212060057, 0.0744037490800572, 0.10968975750501692, 0.3237787877900002, 0.07067945546861104, 0.4623016763408661, 0.2624739033353619, 0.21060818137799747, 0.28789683155997087, 0.1795237050263666, 0.0985246127900033, 0.19776937274209272, 0.07721697545675776, 0.1420318611381659, 0.2068320829930993, 0.1805004585770602, 0.13950647092213897, 0.20500034890791508, 0.04836175834828388, 0.1740408676132053, 0.22865461070861992, 0.28075308719811753, 0.3786657923668193, 0.40182314935624286, 0.019161520743703864, 0.43683891470221387, 0.39825411810318345, 0.4461699166216457, 0.269092953547939, 0.30836039743059573, 0.17839228320581818, 0.4427055098302072, 0.4864908385012144, 0.018524916582457862, 0.3650816552850558, 0.18957032694625076, 0.41319711775009743, 0.32076523094722037, 0.4246886962197217, 0.056086695709552103, 0.3658507396919468, 0.41642507188069755, 0.4565068141981032, 0.20179968754637806, 0.2652410496451089, 0.4941606584341266, 0.2543821815938104, 0.20773326328554986, 0.30546651691099647, 0.3265666876005286, 0.16636007189438395, 0.37706612299275166, 0.24692096736319952, 0.34652329222970285, 0.14108341689833503, 0.1304506121394602, 0.024077015905167365, 0.02527965827821138, 0.37132820645403464, 0.08287611733224665, 0.43877224022558636, 0.2281376632103141, 0.35166724368438257, 0.48137492839809065, 0.17165649782200976, 0.257822197771781, 0.17284381998009457, 0.01000602348243329, 0.264662606390174, 0.04921704541595512, 0.2051007595038053, 0.31202691095248064, 0.15907061826266272, 0.3126657669864065, 0.30823587869148117, 0.12535150671500978, 0.3749836508313608, 0.006911621921718736, 0.04589367573667813, 0.19859137606118388, 0.461620109842123, 0.10930007853665785, 0.2915157543050031, 0.29490765855231205, 0.4832100011898076, 0.2889507838264372, 0.18443863345429629, 0.17644704934711097, 0.4879131872079853, 0.3760551515457729, 0.20942188959667518, 0.06250844250942494, 0.14298958287705038, 0.05059190657487722, 0.41946668639177237, 0.203663924112572, 0.43001793187045845, 0.054956423001797816, 0.0001541225976797178, 0.0899555594321807, 0.32009482659232696, 0.2662398574852972, 0.03363300707119482, 0.347515840501164, 0.2313204912960461, 0.39819219919647497, 0.04737341806733869, 0.3659662063307044, 0.13084285965021225, 0.4732559931942695, 0.04357715411881202, 0.04204385235251412, 0.2038791542875399, 0.1472339574759593, 0.0076727042736063344, 0.17457711244895857, 0.0836567842537217, 0.021648275051117383, 0.14549828567205447, 0.4729888877058225, 0.05197727927379675, 0.24478144489641945, 0.23796887583234927, 0.3627899024053615, 0.19967715286081394, 0.011185417670659892, 0.051736849316049105, 0.49055978005845724, 0.41936258690149697, 0.30325072960419125, 0.4852751047251043, 0.3201496262124387, 0.16979793367133733, 0.14353217330866158, 0.4540412980847779, 0.016879004115369745, 0.1785113238254667, 0.009303719014663092, 0.11313987577383, 0.16970741427334674, 0.09238496170083937, 0.4515319719904878, 0.18524226889747913, 0.4829746085987475, 0.3876281479647058, 0.06508787920143211, 0.21693483113826673, 0.030069214153618185, 0.37792133882995266, 0.12444860658314927, 0.15335290790784156, 0.18559719897564192, 0.30091273120352463, 0.1367038958071854, 0.07070716274755967, 0.45679328927933527, 0.1557403401112265, 0.4286231790383708, 0.43076064254303825, 0.39839603764513565, 0.3424371661621688, 0.03563133853353928, 0.17244362602659896, 0.4617582416907853, 0.4671918629486714, 0.3586704767032542, 0.075376074972195, 0.48783235770326266, 0.03122351429321013, 0.2524247141921243, 0.1638979147935133, 0.4371715463619395, 0.09422893095557172, 0.006126555304025061, 0.310111186157518, 0.03133054548195158, 0.27989889732962214, 0.059281807517561236, 0.46800770597017827, 0.3110482138804133, 0.4450265032626147, 0.35518729695407036, 0.2950216793898989, 0.10692242697528132, 0.07301716593660368, 0.4717861198444882, 0.48498091264922755, 0.07017765322231245, 0.2431295154762007, 0.23606694648274157, 0.3141354675850936, 0.41377955136621036, 0.26713146016671285, 0.30771247411155117, 0.07759191819656008, 0.34196539276346327, 0.47719999598715845, 0.016709564331307103, 0.33782861740972486, 0.45329175118257314, 0.3768257206575404, 0.41214310080930505, 0.1852764341418725, 0.40243149484972923, 0.060192201773071496, 0.014553726731742045, 0.45766365901941386, 0.40734474748177907, 0.2092882171921191, 0.20726335780964644, 0.4712506053751809, 0.2163377275836717, 0.1114498852968907, 0.09225131624264082, 0.3436914144238564, 0.49695012129832894, 0.016337670720049213, 0.11466219333475725, 0.4551463067148169, 0.4692473159900773, 0.08996390343072608, 0.23207515723724637, 0.3516473349633433, 0.3042765505268137, 0.3848003025286473, 0.2718349867936936, 0.05993959550411959, 0.33944251703635003, 0.48578690155511084, 0.37768568382478823, 0.3404785257404597, 0.2541816698325984, 0.17578939791290932, 0.4958701541675175, 0.4380593924885757, 0.46163156332475613, 0.022589223604845943, 0.11822109892357391, 0.3814054559946463, 0.2167907570213709, 0.2954223834932335, 0.3754299162345951, 0.11429011889048712, 0.47083310520420635, 0.03353842383105865, 0.49113053082102653, 0.10022447131874729, 0.2637957559621392, 0.10945956729574075, 0.3600526125738995, 0.10178313250124826, 0.04941855382425531, 0.39232203702604707, 0.2513147462368087, 0.32778758023396415, 0.46912042104412455, 0.11409267550204089, 0.19725959381144947, 0.31154935066710593, 0.17604691139744477, 0.159764142704096, 0.4697458901189976, 0.4595930360715586, 0.3003861316601993, 0.3169343501825193, 0.09306543227793818, 0.22366501929743432, 0.42053356132562275, 0.01578925294287742, 0.3228580724950868, 0.41275990118994077, 0.39370841451430894, 0.44543432774842684, 0.09347638448241624, 0.17697290078372835, 0.3850355571881846, 0.3251751369687742, 0.29317424163097805, 0.4276187137500061, 0.20133721283173478, 0.046070123239960126, 0.00751140302296921, 0.05635578752610049, 0.13487008324901179, 0.05743492402366662, 0.16681017503626694, 0.2344576103914695, 0.03406133905674641, 0.12351904789955598, 0.3567926209719808, 0.1316707178716982, 0.10376765188675885, 0.3403316290379639, 0.30221235554658804, 0.4188488435464364, 0.28103325251246963, 0.11726741884320996, 0.4210981461487183, 0.18450812652204146, 0.017997697970900728, 0.4183849131332458, 0.18326405947056895, 0.013433984192965376, 0.3386381700332291, 0.034710294665696695, 0.2549594803852249, 0.41676986219807177, 0.49398793117162704, 0.03756392685131166, 0.3764733246871041, 0.34202494919756987, 0.44379073763028576, 0.4138253480822243, 0.4200860943155072, 0.30790156540077024, 0.4936939972059647, 0.3666673307881709, 0.12256134023790383, 0.4263304690767565, 0.022478203812742847, 0.06680173974970244, 0.3085148168225225, 0.11593902884515167, 0.44408294278447424, 0.0428705584711061, 0.31434477533619953, 0.35509816628761565, 0.44212750363031256, 0.41312810499508806, 0.2539102765132224, 0.010583448878365986, 0.2242974048371449, 0.17552692239974216, 0.1582318332797254, 0.37155533252506456, 0.018053086187414524, 0.18585718556252273, 0.31008181973864535, 0.03864190268578438, 0.37337736228192986, 0.32874962761152576, 0.3328586031836208, 0.1031398019526098, 0.175439086487518, 0.10047928741613232, 0.02281949052118426, 0.2262184884112735, 0.29143106688291054, 0.4315838566275763, 0.2903077321769709, 0.34627783050072286, 0.07303835807810644, 0.20232517492055835, 0.45296448188546623, 0.19798527755548506, 0.2576697106551272, 0.23269882155040977, 0.46530539667016796, 0.0056302682680052785, 0.48893197583738107, 0.4172998328713857, 0.20211318428847647, 0.4994760088775263, 0.34654111894527817, 0.17739526992746918, 0.3074734174497408, 0.4820816604517556, 0.025568093026363592, 0.26303544788810923, 0.034820147485021824, 0.23203581266435647, 0.009717522398522416, 0.31829519378189575, 0.17667684786847332, 0.49106594273229065, 0.29005644142144954, 0.0883936114216412, 0.3710727347783706, 0.29464515008222936, 0.14030635573287326, 0.39636710416169413, 0.06921943299177458, 0.22442392664665795, 0.3422161606273424], 
    #     'replicas': [2, 1, 2, 2, 0, 3, 5, 5, 2, 0, 1, 2, 5, 3, 1, 2, 5, 1, 1, 2, 3, 5, 0, 5, 2, 4, 3, 3, 3, 2, 0, 0, 3, 4, 5, 5, 5, 3, 3, 3, 1, 0, 2, 3, 2, 0, 1, 5, 2, 4, 5, 2, 0, 0, 4, 4, 5, 3, 1, 3, 1, 3, 4, 5, 3, 2, 0, 5, 4, 5, 0, 0, 1, 5, 5, 1, 5, 0, 1, 3, 3, 2, 4, 2, 4, 3, 4, 4, 4, 1, 1, 0, 0, 0, 0, 3, 1, 3, 4, 4, 5, 0, 0, 1, 3, 1, 2, 4, 2, 0, 0, 3, 1, 2, 5, 5, 1, 2, 0, 4, 1, 1, 1, 1, 0, 1, 4, 3, 4, 1, 2, 1, 4, 3, 3, 1, 4, 5, 0, 5, 2, 4, 5, 5, 0, 4, 0, 1, 5, 3, 0, 4, 3, 1, 3, 3, 5, 1, 1, 2, 0, 2, 0, 4, 5, 1, 1, 2, 1, 3, 0, 0, 5, 3, 5, 2, 0, 4, 2, 3, 5, 2, 0, 3, 4, 3, 4, 5, 4, 2, 5, 4, 1, 3, 4, 1, 2, 5, 2, 2, 3, 5, 4, 4, 0, 2, 3, 3, 1, 0, 2, 1, 4, 1, 3, 5, 5, 1, 2, 5, 1, 5, 5, 4, 5, 1, 5, 3, 3, 2, 4, 3, 4, 1, 2, 3, 0, 5, 5, 1, 0, 4, 4, 5, 0, 1, 3, 2, 0, 2, 1, 0, 1, 3, 3, 5, 1, 5, 3, 0, 2, 1, 4, 2, 2, 4, 5, 3, 0, 0, 3, 3, 3, 1, 1, 0, 3, 0, 1, 0, 2, 0, 5, 2, 3, 0, 3, 1, 2, 5, 5, 0, 4, 5, 0, 2, 2, 3, 1, 1, 2, 2, 1, 4, 2, 5, 3, 4, 3, 0, 2, 5, 3, 5, 3, 3, 3, 2, 5, 5, 4, 2, 4, 2, 3, 1, 1, 4, 2, 2, 5, 0, 3, 4, 2, 4, 2, 0, 5, 4, 5, 1, 5, 3, 2, 1, 5, 1, 0, 0, 2, 1, 3, 2, 1, 5, 4, 3, 2, 2, 3, 3, 2, 0, 5, 2, 1, 1, 4, 4, 3, 4, 2, 0, 1, 0, 3, 4, 5, 0, 1, 1, 2, 4, 5, 4, 2, 2, 3, 2, 5, 4, 2, 0, 2, 1, 1, 4, 3, 2, 3, 2, 1, 0, 2, 2, 2, 1, 5, 4, 1, 4, 4, 5, 1, 4, 2, 0, 3, 4, 5, 2, 3, 1, 2, 2, 4, 5, 2, 3, 4, 1, 1, 2, 4, 2, 2, 4, 3, 4, 0, 3, 0, 1, 5, 2, 5, 5, 0, 0, 1, 4, 1, 0, 2, 3, 2, 1, 3, 5, 5, 0, 1, 1, 4, 2, 0, 0, 1, 4, 4, 3, 0, 0, 1, 1, 1, 5, 1, 1, 1, 2, 4, 4, 3, 3, 3, 0, 5, 5, 2, 2, 3, 5, 1, 0, 4, 2, 3, 3, 4, 5, 2, 4, 0, 2, 1, 5, 2, 2, 5, 4, 0, 0, 0, 3, 2, 4, 5, 5, 1, 4, 0, 5, 2, 4, 3, 3, 5, 4, 1, 5, 5, 4, 5, 3, 2, 1, 4, 5, 0, 3, 1, 3, 2, 0, 4, 2, 3, 3, 2, 0, 2, 4, 2, 5, 0, 2, 4, 1, 2, 2, 5, 0, 4, 1, 1, 5, 4, 3, 0, 4, 1, 2, 0, 2, 1, 4, 2, 0, 5, 2, 5, 4, 5, 0, 0, 5, 3, 3, 1, 3, 3, 5, 5, 0, 2, 2, 4, 3]
    # }


    # 运行10次，取效果最好者
    for gen in xrange(10):
        
        # 1. 用于生成json的数据
        data = {
            'scale':[],
            'simple':[],
            'complex':[],
            'safe_simple':[],
            'safe_complex':[]
        }
        # 2. 产生新初始集群与新增容器的服务数量
        init_popu0 = main_init(400, 1.0)
        cycle = []
        for i in xrange(1, 7):
            a = 10 ** i
            ll = sorted(random.sample(range(1,10), 7))
            for j in ll:
                cycle.append(j*a)

        # 3. 模拟多批量新增场景
        for scale in cycle:
            # 记录初始集群信息并深度拷贝多副本用于算法间对比
            addtion0 = create_addtion(1.0, scale)
            scale_init = len(init_popu0['c_rp']) + sum(addtion0['replicas'])
            cost0 = compute_costs(init_popu0)
            init_popu1 = copy.deepcopy(init_popu0)
            init_popu2 = copy.deepcopy(init_popu1)
            init_popu3 = copy.deepcopy(init_popu2)

            # s0 = 'Start: \ninit_popu = {}  \naddtion = {} \nThe initial cost = {}'.format(init_popu0, addtion0, cost0)
    
            # 初始集群多副本进行不同放置算法对比
            simple, used_time0 = FFDSum_simple(init_popu0, addtion0)
            comple, used_time1 = FFDSum_complex(init_popu1, addtion0)
            # safe_simple, used_time2 = safe_FFDSum_simple(init_popu2, addtion0)
            # safe_comple, used_time3 = safe_FFDSum_complex(init_popu3, addtion0)

            # 各新集群目标模型计算并记录各次迭代集群数据
            cost_simple, cost_complex = compute_costs(simple), compute_costs(comple)
            data = createJSON(data, scale_init, cost_simple, cost_complex, 0, 0)

            # s1 = '\n\n\nEnd:   \nBins_simple = {} \nThe cost_simple of new state = {}'.format(init_popu0, cost_simple)    
            # s2 = '\n\n\nEnd:   \nBins_complex = {} \nThe cost_comlex of new state = {}'.format(init_popu1, cost_complex)    
            # print s0,'\n' ,s1,'\n',s2


        # 4. 记录data用于前端数据可视化
        with open('.//viz//contrast-addtion-{}-demo.json'.format(gen),'w') as f:
            f.flush()
            json.dump(data, f, indent=2)

    # with open('addtion_phase//Result_Contrast.py','a') as f:
    #     f.flush()
    #     f.write(s0)
    #     f.write(s1)
    #     f.write(s2)
