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
    # print "new Simple used time is {} \n used the number of HMs is {}".format(used_time, len(num))
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
    data['simple'].append(cost1)
    data['complex'].append(cost0)
    data['safe_simple'].append(cost2)
    data['safe_complex'].append(cost3)
    return data

if __name__ == '__main__':
    '''
    对于Docker+VM与Docker+VM+HM架构下，分别不同的排序单位vm，docker进行的FFDSum排序算法，批量对比与画图
    '''

    # 一、 1. 设置可选的虚机尺寸
    vm_option = [(0.3, 0.3), (0.5, 0.4), (0.6, 0.5), (0.8, 0.7), (1.0, 0.8), (1.0, 1.0)]

    # 二、 构造输出json文件
    # 构造并行坐标数据类型
    data = {
        "scale":[],
        "simple":[],
        "complex":[],
        "safe_simple":[],
        "safe_complex":[]
    }



    # 三、 循环计算不同初始集群下，各算法表现出来代价指标
    # cycle = [50]*5 + [100]*5 + [200]*5 + [300]*5 + [500]*5 + [800]*5 + [1000]*5 + [3000]*5 + [5000]*5 + [8000]*5 + [10000]*5
    cycle = [10, 30, 40, 60, 80, 100, 120, 140,160,170, 190, 200, 210, 230, 250, 280,  300, 320, 350, 370, 390, 400, 420, 450, 470, 490, 500, 504, 540, 600]
    for i in cycle:
        # 2. 初始化集群状态及新增序列，计算初始集群的各项指标代价，并深拷贝一份作为其他算法实参
        init_popu0, addtion0 = main_init(100, 1.0, i)
        num_init_docker = len(init_popu0['c_rp'])
        init_popu1, init_popu2, init_popu3 = copy.deepcopy(init_popu0), copy.deepcopy(init_popu0), copy.deepcopy(init_popu0)
        init_cost = compute_costs(init_popu0)
        # s0 = 'Start: \nThe initial Bins = {} \n\n\n The initial cost = {}\n'.format(init_popu0 ,init_cost)
        s0 = '\n\nStart: \nWhen len(addtion0) = {},\nThe initial cost = {}\n'.format(i, init_cost)

        # 3. 分别在两个相同集群状态上执行调度算法，并分别计算最终集群的各项代价
        bins1, used_time1 = new_FFDSum_simple(init_popu1, addtion0)
        bins0, used_time0 = FFDSum_complex(init_popu0, addtion0)
        # bins2, used_time2 = safe_FFDSum_simple(init_popu2, addtion0)
        # bins3, used_time3 = safe_FFDSum_complex(init_popu3, addtion0)
        # cost0, cost1, cost2, cost3 = compute_costs(bins0), compute_costs(bins1), compute_costs(bins2), compute_costs(bins3)
        # cost0['used_time'], cost1['used_time'], cost2['used_time'], cost3['used_time'] = used_time0, used_time1, used_time2, used_time3
        cost0, cost1 = compute_costs(bins0), compute_costs(bins1)
        cost2, cost3 = 0, 0
        
        # 4. 存档记录（s2记录比较详细，用来检验算法运行正确性）
        # s2 = '\n\n\nEnd:\n\n\nThe FFDSum cost of new state = {}\n\nThe FFDSum_Bins = {}  \
        # \n\n\nThe Dot-prod cost of new state = {}\n\nThe Dot-Prod_Bins = {} '.format(cost0, bins0, cost1, bins1)
        # s1 = '\n\n\nEnd: \
        # \n\nThe FFDSum cost of new state = {}   \
        # \n\nThe FFDProd cost of new state = {}  \
        # \n\nThe Dot-prod cost of new state = {} \
        # The func_L2 cost of new state = {}'.format(cost0, cost1, cost2, cost3)      
        # with open('addtion_phase//tmp.py','a') as f:
        #     f.flush()
        #     f.write(s0)
        #     f.write(s1)

        # 5. 写入json文件，用于前端展示算法结果对比
        addtion_scale = num_init_docker + len(addtion0['replicas'])
        data = createJSON(data, addtion_scale, cost0, cost1, cost2, cost3)
    
    # 导出为json文件
    with open('.//viz//contrast-addtion-demo.json', 'w') as f:
        f.flush()
        json.dump(data, f, indent=2)



































# if __name__ == '__main__':
#     '''
#     本模块测试算法是否运行正确
#     '''
#     # test1 init_main(50, 1.0, 100) 使用vm_option以及新的create_VM()
#     # init_popu={
#     #     'h_m_cost': [[0.4, 0.4, 0.3, 0, 0, 1.0, 0.8, 1.0, 0, 0.5, 0.8, 0, 0.8, 1.0, 0, 1.0, 0, 0.4, 1.0, 0.5, 1.0, 1.0, 0.7, 0, 0.4, 0, 0, 1.0, 0.8, 1.0, 0, 0.5, 0, 0.3, 0.4, 0.3, 0.7, 0.5, 0, 1.0, 0, 0.4, 0.5, 0.7, 1.0, 0.7, 0, 0, 0.8, 0.5]],
#     #     'map_v_h': {2: 9, 3: 12, 4: 35, 5: 22, 6: 39, 7: 17, 8: 18, 9: 2, 10: 41, 11: 49, 14: 7, 16: 1, 17: 20, 18: 34, 19: 31, 22: 6, 23: 37, 24: 13, 25: 48, 26: 42, 27: 33, 28: 28, 29: 27, 30: 45, 32: 10, 33: 0, 36: 36, 37: 24, 38: 19, 39: 44, 41: 29, 42: 48, 44: 21, 45: 43, 46: 5, 47: 15},
#     #     'c_rp': [0.39803995189060776, 0.1991658405314019, 0.39768889258222717, 0.3325366354778356, 0.1342777876545161, 0.01656148103282018, 0.05397241445867573, 0.1310434487858827, 0.2704227767280211, 0.008955044055479089, 0.1331721771022163, 0.4241489946289537, 0.3968269044094304, 0.33398198503451765, 0.2495301921879871, 0.08463941599263941, 0.48407314029569853, 0.33486458390354445, 0.14030090211415353, 0.04343243706425565, 0.26124013102124194, 0.3785576996809441, 0.24891073064760638, 0.38282191475385174, 0.21379682570484998, 0.24378931841585733, 0.3002020187123837, 0.1919340274682979, 0.46964883581045436, 0.4714404337487207, 0.06156666961513463, 0.021995671323702337, 0.38869392752558096, 0.12060983793092295, 0.07127347986816346, 0.3838773335994973, 0.37407500041696556, 0.13472434699437258, 0.04449859672699252, 0.36987986212047896, 0.3531740929128703, 0.3366870076071558, 0.16173162442617905, 0.15702730502599677, 0.03809488688757445, 0.08669477009365767, 0.05318386717506646, 0.16398068552521866, 0.2972309296170753, 0.39941631749265183],
#     #     'v_m_cost': [[0, 0, 0.14800148868523197, 0.41801591843087094, 0.18152753484222625, 0.5440159638226236, 0.7458234444061824, 0.2940070530987197, 0.2927490230023475, 0.22850523363734732, 0.24019890890227028, 0.29857914697853616, 0, 0, 0.12279332999634093, 0, 0.2182348067642732, 0.9645704513714561, 0.24100621927613597, 0.42665785344140605, 0, 0, 0.4881140695231102, 0.06452735097775414, 0.371320197853085, 0.011984010378050941, 0.029893211192067864, 0.23579121395624217, 0.37809063210515087, 0.5844804118897265, 0.19750568192006432, 0, 0.7743002345296373, 0.3232851836249956, 0, 0, 0.4683640657503727, 0.3128431944021872, 0.4587901293671526, 0.048552451636542565, 0, 0.8131416406834183, 0.11710179440422402, 0, 0.496905627847963, 0.2300124473863819, 0.32058458723754407, 0.44937996238431505, 0, 0]],
#     #     'v_rm': [1.0, 0.4, 0.5, 0.8, 0.3, 0.7, 1.0, 0.4, 1.0, 0.3, 0.4, 0.5, 0.8, 0.7, 1.0, 0.3, 0.4, 1.0, 0.4, 0.5, 0.5, 0.8, 0.8, 0.5, 1.0, 0.4, 0.5, 0.3, 0.8, 1.0, 0.7, 0.4, 0.8, 0.4, 0.8, 0.8, 0.7, 0.4, 0.5, 1.0, 0.4, 1.0, 0.4, 1.0, 1.0, 0.7, 1.0, 1.0, 0.4, 0.8],
#     #     'h_p_cost': [[0.5, 0.5, 0.3, 0, 0, 1.0, 1.0, 1.0, 0, 0.6, 1.0, 0, 1.0, 1.0, 0, 1.0, 0, 0.5, 1.0, 0.6, 1.0, 1.0, 0.8, 0, 0.5, 0, 0, 1.0, 1.0, 1.0, 0, 0.6, 0, 0.3, 0.5, 0.3, 0.8, 0.6, 0, 1.0, 0, 0.5, 0.6, 0.8, 1.0, 0.8, 0, 0, 1.0, 0.6]],
#     #     'c_rm': [0.37809063210515087, 0.14797875989440723, 0.446136333563489, 0.2846394747802726, 0.09475784196039902, 0.2182348067642732, 0.11710179440422402, 0.11099353151435348, 0.4389301157389788, 0.19750568192006432, 0.16627953082252578, 0.2996871108426934, 0.269498295337843, 0.4896607597493646, 0.14800148868523197, 0.22850523363734732, 0.3232851836249956, 0.4144842213761347, 0.0005388631986207315, 0.048552451636542565, 0.307887938597714, 0.44937996238431505, 0.18901768925024898, 0.3986574193072836, 0.14987527849489743, 0.2300124473863819, 0.42665785344140605, 0.20854072345543492, 0.371320197853085, 0.4346051333948291, 0.23579121395624217, 0.14212366009071636, 0.4881140695231102, 0.09807524881155391, 0.12772752227619394, 0.4308824936720783, 0.2927490230023475, 0.011984010378050941, 0.24100621927613597, 0.259224237003565, 0.2847917268190586, 0.4683640657503727, 0.12279332999634093, 0.06452735097775414, 0.029893211192067864, 0.1043024709467523, 0.18152753484222625, 0.18758561546418268, 0.32058458723754407, 0.4587901293671526],
#     #     'v_rp': [1.0, 0.5, 0.6, 1.0, 0.3, 0.8, 1.0, 0.5, 1.0, 0.3, 0.5, 0.6, 1.0, 0.8, 1.0, 0.3, 0.5, 1.0, 0.5, 0.6, 0.6, 1.0, 1.0, 0.6, 1.0, 0.5, 0.6, 0.3, 1.0, 1.0, 0.8, 0.5, 1.0, 0.5, 1.0, 1.0, 0.8, 0.5, 0.6, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 0.8, 1.0, 1.0, 0.5, 1.0],
#     #     'v_p_cost': [[0, 0, 0.2495301921879871, 0.7362936470549859, 0.05318386717506646, 0.7230539550333492, 0.8218378872111809, 0.20444565697037975, 0.37407500041696556, 0.08463941599263941, 0.14260550925462528, 0.29502413431110136, 0, 0, 0.16173162442617905, 0, 0.01656148103282018, 0.7885778979820345, 0.04449859672699252, 0.3002020187123837, 0, 0, 0.38869392752558096, 0.15702730502599677, 0.46964883581045436, 0.13472434699437258, 0.03809488688757445, 0.06156666961513463, 0.39803995189060776, 0.6852372594535707, 0.008955044055479089, 0, 0.6665186205123532, 0.48407314029569853, 0, 0, 0.3366870076071558, 0.2786287975619556, 0.39941631749265183, 0.04343243706425565, 0, 0.7176864986573962, 0.05397241445867573, 0, 0.5101508616688484, 0.24378931841585733, 0.2972309296170753, 0.3785576996809441, 0, 0]],
#     #     'population': [[[28, 28], [3, 12], [6, 39], [32, 10], [17, 20], [16, 1], [42, 48], [11, 49], [17, 20], [30, 45], [7, 17], [6, 39], [3, 12], [32, 10], [2, 9], [9, 2], [33, 0], [41, 29], [3, 12], [39, 44], [44, 21], [47, 15], [44, 21], [41, 29], [29, 27], [45, 43], [19, 31], [37, 24], [24, 13], [29, 27], [27, 33], [10, 41], [22, 6], [10, 41], [7, 17], [17, 20], [8, 18], [25, 48], [18, 34], [5, 22], [5, 22], [36, 36], [14, 7], [23, 37], [26, 42], [37, 24], [4, 35], [11, 49], [46, 5], [38, 19]]]
#     #     }

#     # addtion0={
#     #     'c_rm': [0.12724923237168873, 0.2302721028812758, 0.02191444219166494, 0.3013645216685813, 0.48897446108798703, 0.0234901968008423, 0.3771913081071047, 0.22209734026425582, 0.41391081355188536, 0.2817032737249423, 0.030146492134660224, 0.4379983116779751, 0.09502065100887658, 0.3950141104427656, 0.19528376497506816, 0.20823149515114106, 0.44323803564487335, 0.0025428982348151274, 0.3249066662838954, 0.205567058133299, 0.21349346691730633, 0.30237438741784994, 0.39374958060505155, 0.05506299602245149, 0.2807617919186476, 0.3749591716213659, 0.15184529493233262, 0.39854966241326806, 0.33523353711422277, 0.4752541716099998, 0.25685674446234824, 0.10903770313561995, 0.4276976868405121, 0.43300638258350416, 0.0456029386292236, 0.46549040282748133, 0.17765338748853168, 0.0934661221926929, 0.3954775768765382, 0.49108265318676436, 0.40884428034542597, 0.364658773381155, 0.31315893636181635, 0.32003608849730597, 0.35205544108622877, 0.421400783872125, 0.340178671088145, 0.3207232886954098, 0.31301399729691504, 0.305957669028904, 0.2587998104719148, 0.14987701490987787, 0.12286710412690202, 0.1643105372162426, 0.2614597593841833, 0.20195967128241013, 0.1961957342865447, 0.20659250240237836, 0.20802818472201912, 0.3641306506288858, 0.18082887838479442, 0.42445094636545905, 0.3566837410007157, 0.3539965799485931, 0.049393884630116874, 0.05843407340139495, 0.4719686138987689, 0.14086556422744853, 0.4262395054831031, 0.0028956928738476106, 0.21830008720508656, 0.28599725253839714, 0.4486971164231134, 0.41541969276935015, 0.09695947985807693, 0.3214933547315539, 0.3319613979970855, 0.25634574843974856, 0.04470711151349721, 0.011807628954853572, 0.12630902545063444, 0.13677898557030524, 0.24399531235619873, 0.052103188808726664, 0.06876660472918, 0.4865100234848053, 0.11770199771313858, 0.466120667899827, 0.4731017893460968, 0.07333858310731534, 0.3419023692313965, 0.12904833952452358, 0.04544969341842153, 0.3718346237745156, 0.2594324249190014, 0.49685562667823757, 0.0629579825744293, 0.021576611683093105, 0.04592072537996808, 0.22864552449513367],
#     #     'c_rp': [0.24287380004718884, 0.11732941819398013, 0.07679450149737188, 0.4825230566268437, 0.4113988337502151, 0.0014786751468847115, 0.33827959700425503, 0.21091676941432547, 0.28336517727156285, 0.3721422626805915, 0.05535705713215172, 0.34628354266195266, 0.043045697389501036, 0.4587298600292345, 0.13961225698695567, 0.12101478456908693, 0.43176140263221313, 0.12784023171147418, 0.3732434110283516, 0.0806503209181822, 0.013288237300968897, 0.3035811630452029, 0.38710621113764826, 0.015388306804734297, 0.45490208939266963, 0.3474555831278905, 0.02170225718712321, 0.3453365551704884, 0.4058359183522699, 0.3827483160405229, 0.35428148465634224, 0.12247784873747031, 0.38216094961196473, 0.4062941136001976, 0.03225462653971345, 0.4512180697552103, 0.2060560790899793, 0.17253856833520514, 0.34304131586777936, 0.3606980997343634, 0.39770875719001614, 0.43150196395382123, 0.39114418695925807, 0.40577932611200157, 0.272376355940989, 0.47765471190476344, 0.2850407683341675, 0.42011021365353524, 0.4625241942015957, 0.36662963367394463, 0.3822584783730816, 0.13558490086347585, 0.22954288793444205, 0.09976022956123104, 0.36911470853878087, 0.013207872580046465, 0.1254307497532945, 0.18631705158743622, 0.0061525930293457876, 0.42752834281498253, 0.2356845138641105, 0.47727463020324185, 0.2572533818555725, 0.48422210840068336, 0.11576165922168186, 0.1621165700552259, 0.33383219895003646, 0.07748829052048806, 0.43093048368701203, 0.10308121995835334, 0.15754324001673548, 0.3156727858609588, 0.2976206050698703, 0.47092888561740953, 0.04361034986052975, 0.47601519610315374, 0.2684921226313891, 0.36251552285823446, 0.08659161909582103, 0.18469917884158704, 0.1749137878158391, 0.09334594162582854, 0.05127291972721165, 0.21029684828330486, 0.1975479200870488, 0.4443544754934908, 0.039315444313542613, 0.39008544255427585, 0.46370478544053134, 0.057304261072659735, 0.49793763032797417, 0.12200490078019233, 0.055275747022489, 0.4460240817791273, 0.2557956942790181, 0.30371824473714826, 0.16026064896100195, 0.04363093290138742, 0.016685483290081016, 0.24168678506346758],
#     #     'replicas': [2, 2, 1, 4, 0, 4, 4, 2, 5, 0, 4, 1, 0, 0, 0, 4, 3, 0, 5, 3, 1, 2, 0, 4, 2, 4, 2, 3, 3, 4, 2, 4, 0, 2, 3, 4, 2, 3, 1, 1, 5, 0, 3, 4, 4, 5, 1, 4, 1, 5, 5, 5, 4, 3, 1, 3, 0, 2, 3, 1, 3, 1, 1, 0, 1, 1, 5, 0, 3, 2, 5, 0, 5, 2, 2, 3, 2, 2, 3, 3, 5, 4, 3, 0, 1, 1, 3, 5, 0, 1, 2, 2, 3, 3, 4, 2, 3, 3, 3, 5]
#     #     }

#     # test2  main_init(50, 1.0, 490)
#     # init_popu={
#     #     'h_m_cost': [[0.8, 0.7, 0.5, 0, 0.4, 0.5, 0, 0.5, 0, 1.0, 0, 0.3, 1.0, 0, 0, 0.5, 0, 0.4, 1.0, 0.5, 1.0, 0.7, 0.8, 1.0, 0, 0.8, 0, 0, 0.7, 0.8, 0, 0, 1.0, 0.7, 0, 0.4, 0.5, 0, 0, 1.0, 0.8, 0, 0.5, 0, 0.8, 0, 0.5, 0.8, 0, 0]],
#     #     'map_v_h': {6: 23, 7: 39, 8: 1, 11: 32, 13: 36, 14: 12, 16: 40, 17: 0, 18: 46, 19: 28, 20: 40, 21: 33, 22: 21, 23: 35, 25: 2, 27: 47, 28: 22, 29: 9, 31: 11, 32: 7, 33: 29, 36: 42, 38: 18, 39: 17, 40: 4, 41: 20, 42: 1, 43: 44, 45: 25, 46: 15, 47: 5, 48: 19},
#     #     'c_rp': [0.10417821771854957, 0.11554185212469442, 0.28864070115634616, 0.2952446314862494, 0.16349966885284212, 0.28161590682938353, 0.1953811194597202, 0.11551302843683342, 0.19839300860994435, 0.1885444656881573, 0.18314436418243707, 0.11636858616654089, 0.13648122051942807, 0.3993348839452889, 0.23376524340028193, 0.13735609226663414, 0.23685589341168256, 0.1416507547241322, 0.3273110778177406, 0.3848017220588272, 0.31517120708475016, 0.35761548582882313, 0.46360785366423557, 0.11792614073558372, 0.2934917096727532, 0.42987498418751874, 0.23185369802499006, 0.13430659009330287, 0.11082866585206402, 0.17591582286113971, 0.46210508826265584, 0.08771152981406893, 0.3246738538707452, 0.0829944805370072, 0.1848468198614463, 0.3886308749315804, 0.3348939642913326, 0.015155781202892071, 0.32462357135300907, 0.11368999343990754, 0.4015506557066194, 0.14412611606541792, 0.16453296438081028, 0.3640345086401249, 0.07988330728334114, 0.10727829402848799, 0.4795484355211322, 0.212719332221196, 0.19712175745405652, 0.12590783091897145],
#     #     'v_m_cost': [[0, 0, 0, 0, 0, 0, 0.5311434407398433, 0.4715366870725802, 0.016789924510398957, 0, 0, 0.8436017734104486, 0, 0.22846384760441985, 0.44004357232794233, 0, 0.07842470829098386, 0.3008901426309918, 0.3815350873949904, 0.18948064620784152, 0.28985727187938554, 0.5914584602883822, 0.3724379289506283, 0.243512937578942, 0, 0.41817599786143256, 0, 0.49474356561391253, 0.29630144558802474, 0.4466829321873842, 0, 0.0590840417635482, 0.4512306180216318, 0.2000259187592355, 0, 0, 0.276238040426233, 0, 0.47915610877162196, 0.20464926842227374, 0.36373812792720916, 0.19857480064517433, 0.1835325263388528, 0.48513227032801676, 0, 0.4614363175422369, 0.15102959297856444, 0.41986545387421786, 0.02978018290553827, 0]], 'v_rm': [1.0, 0.7, 1.0, 0.5, 0.3, 0.8, 1.0, 1.0, 0.3, 0.8, 0.8, 1.0, 1.0, 0.5, 1.0, 1.0, 0.3, 0.8, 0.5, 0.7, 0.5, 0.7, 0.7, 0.4, 1.0, 0.5, 0.5, 0.8, 0.8, 1.0, 0.5, 0.3, 0.5, 0.8, 0.8, 0.4, 0.5, 0.5, 1.0, 0.4, 0.4, 1.0, 0.4, 0.8, 0.3, 0.8, 0.5, 0.5, 0.5, 0.7],
#     #     'h_p_cost': [[1.0, 0.8, 0.6, 0, 0.5, 0.6, 0, 0.6, 0, 1.0, 0, 0.3, 1.0, 0, 0, 0.6, 0, 0.5, 1.0, 0.6, 1.0, 0.8, 1.0, 1.0, 0, 1.0, 0, 0, 0.8, 1.0, 0, 0, 1.0, 0.8, 0, 0.5, 0.6, 0, 0, 1.0, 0.8999999999999999, 0, 0.6, 0, 1.0, 0, 0.6, 1.0, 0, 0]],
#     #     'c_rm': [0.17824705998195625, 0.19857480064517433, 0.48513227032801676, 0.38683117741804673, 0.22846384760441985, 0.3008901426309918, 0.09565191118699568, 0.10275371240488515, 0.1112937320635276, 0.19448370023608777, 0.06439944060358505, 0.05804224213383816, 0.20464926842227374, 0.46248237328931485, 0.10377299264011705, 0.1579987195905237, 0.07842470829098386, 0.0590840417635482, 0.4715366870725802, 0.41817599786143256, 0.4063241747626636, 0.2792788790572614, 0.43518521477705463, 0.016673735482307106, 0.41986545387421786, 0.39097057297379545, 0.0052854663568965565, 0.24171234717600035, 0.02209535513829594, 0.026852986438662907, 0.367959585707387, 0.025515853526722698, 0.26695261730614916, 0.243512937578942, 0.15627324551132757, 0.3815350873949904, 0.44004357232794233, 0.15957573938415423, 0.30569588579337104, 0.19354773318313956, 0.289431093563843, 0.1805861292392373, 0.02978018290553827, 0.28985727187938554, 0.004478343243241312, 0.0887321866957079, 0.26159133927650724, 0.16262765976917862, 0.1289342378402685, 0.016789924510398957],
#     #     'v_rp': [1.0, 0.8, 1.0, 0.6, 0.3, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 0.3, 1.0, 0.6, 0.8, 0.6, 0.8, 0.8, 0.5, 1.0, 0.6, 0.6, 1.0, 1.0, 1.0, 0.6, 0.3, 0.6, 1.0, 1.0, 0.5, 0.6, 0.6, 1.0, 0.5, 0.5, 1.0, 0.5, 1.0, 0.3, 1.0, 0.6, 0.6, 0.6, 0.8],
#     #     'v_p_cost': [[0, 0, 0, 0, 0, 0, 0.5358572457999222, 0.3273110778177406, 0.12590783091897145, 0, 0, 0.8101427851802074, 0, 0.16349966885284212, 0.3348939642913326, 0, 0.23685589341168256, 0.28161590682938353, 0.3886308749315804, 0.3886351550823357, 0.3640345086401249, 0.6484546735256819, 0.541988395545997, 0.0829944805370072, 0, 0.3848017220588272, 0, 0.6636402275878006, 0.22920302187674096, 0.5824157465380932, 0, 0.1416507547241322, 0.4783889956686865, 0.30567130263843234, 0, 0, 0.3395072355251381, 0, 0.5172610246808726, 0.13648122051942807, 0.44099215751954995, 0.11554185212469442, 0.33603191574353963, 0.28864070115634616, 0, 0.5132183195589025, 0.30795042330612055, 0.2934917096727532, 0.16453296438081028, 0]],
#     #     'population': [[[42, 1], [41, 20], [43, 44], [32, 7], [13, 36], [17, 0], [36, 42], [28, 22], [33, 29], [45, 25], [32, 7], [40, 4], [39, 17], [38, 18], [27, 47], [11, 32], [16, 40], [31, 11], [7, 39], [25, 2], [11, 32], [11, 32], [21, 33], [38, 18], [47, 5], [27, 47], [42, 1], [6, 23], [46, 15], [19, 28], [22, 21], [29, 9], [45, 25], [23, 35], [21, 33], [18, 46], [14, 12], [29, 9], [40, 4], [28, 22], [6, 23], [36, 42], [48, 19], [20, 40], [22, 21], [33, 29], [29, 9], [19, 28], [46, 15], [8, 1]]]
#     # }

#     # addtion0={
#     #     'c_rm': [0.4727130783550465, 0.37374710612794537, 0.16565526997755456, 0.20558840534148878, 0.1972368572205715, 0.26572937355401927, 0.07473860995068804, 0.4194501955344404, 0.2964369057954926, 0.38022041597579226, 0.42786691624687656, 0.1647402051596464, 0.2991104289593761, 0.23574057513344118, 0.14948393363473958, 0.33265762970059465, 0.2344523745190794, 0.04300888202054426, 0.17933924683663496, 0.4051092554806042, 0.43351550911117565, 0.07570842663739613, 0.36259623789877427, 0.31484479196308734, 0.4412318747326508, 0.2147598843356489, 0.1129041652160088, 0.3254340899596032, 0.04419874940573551, 0.21973256402193658, 0.13409018200015324, 0.041288616160004954, 0.22441741059345485, 0.39632842228835596, 0.05876173605958293, 0.45966314769779715, 0.14775196977957888, 0.4427985726538468, 0.4101068259600765, 0.4784349173900906, 0.16906071117708268, 0.10727119197757065, 0.3076820672646586, 0.05386433729768425, 0.4048860686539191, 0.07420359408104302, 0.4285867549868213, 0.19019199014774826, 0.42121742106976867, 0.42300500179832545, 0.07662193423163091, 0.03560201076868663, 0.3682532229644999, 0.1899430502845582, 0.4577890520998559, 0.02641183432986241, 0.056798311213508534, 0.49424956475972065, 0.3364198339906105, 0.44888139034669394, 0.0031134394446544478, 0.40281168165166825, 0.004423217063622309, 0.33925582028625784, 0.18665404268583746, 0.22629157189088844, 0.23110554978144918, 0.4822226442546481, 0.44681517973714735, 0.047780433932769956, 0.4200332981511188, 0.28350713897163193, 0.08180039074977372, 0.24608973947521448, 0.4370750666696098, 0.3789650245146556, 0.48660430961291157, 0.3174728662144099, 0.4901082568923586, 0.05383668600318095, 0.32463629644302583, 0.4707920141521622, 0.48072460707793346, 0.35211607516982235, 0.333835989391146, 0.03126700750637096, 0.26728262653401536, 0.10896429047808034, 0.4458936911097152, 0.07963919968086608, 0.2912339719728016, 0.12683100536184458, 0.41693548361300997, 0.24394336959602572, 0.26193991960327934, 0.1906304783280618, 0.18857416092731133, 0.22908088514211128, 0.11196177337523544, 0.428950913923579, 0.2438436719491471, 0.4001377335976143, 0.4414928303268044, 0.4782444550464673, 0.4586973151205578, 0.01225636489474477, 0.2924142994966805, 0.11986742614539608, 0.4301630277127571, 0.0723094019492582, 0.04131771094881512, 0.11264687136088722, 0.4800170489608301, 0.4021757744639264, 0.33798399573652516, 0.41904200377262263, 0.18063998308252202, 0.21225891073788608, 0.1178602627393053, 0.17195860057539333, 0.08935646028818625, 0.35050288930865825, 0.10727693881922701, 0.10274340247078231, 0.15376756631471852, 0.3758617099812055, 0.11924100346465547, 0.00924023133020041, 0.3296149624736389, 0.27650241921269636, 0.0847229937445336, 0.14600631568865546, 0.23844439528540443, 0.195447821575262, 0.3432993318569392, 0.16792234286382088, 0.2524709035326683, 0.48523793101869206, 0.13844882829132318, 0.14863135977213032, 0.39240042772597594, 0.0954079950631703, 0.4348320065488436, 0.027369671162404657, 0.4127972269775579, 0.22773883224715188, 0.37820413078540926, 0.1883164876595437, 0.21050531258336305, 0.03525004216957542, 0.43723789886158704, 0.4193876709262619, 0.12368986469958079, 0.4340111373746544, 0.34291730745239524, 0.3784727969900104, 0.4209223579541708, 0.4667435185735265, 0.4585051377840885, 0.35766664374405605, 0.031386429753420736, 0.43633102600777296, 0.11277877403989162, 0.014509302544503805, 0.32153300246922445, 0.33848729386593973, 0.3868356860095097, 0.06576459931690001, 0.46662534577442727, 0.11244979817075756, 0.33308778112944865, 0.0022537192666249872, 0.02996041641537231, 0.42858189086424303, 0.4063911375254253, 0.3422954506543623, 0.01104962587246694, 0.2777569435196712, 0.0812255766447379, 0.47253801807435886, 0.30487245559709397, 0.04903179580534897, 0.15305877701242346, 0.14106590509641653, 0.2058875711014053, 0.1956769151726179, 0.15948372147415826, 0.39193850074745706, 0.25127349118716497, 0.13255084747740423, 0.11955574817727715, 0.21903658345191326, 0.16749306918359047, 0.20972078905584554, 0.12701287340508186, 0.07080640155183054, 0.007673085408037794, 0.10565880060263075, 0.012557093169630329, 0.4165821685981658, 0.42568390795590405, 0.07966995485892031, 0.41562110162047505, 0.1860604332550529, 0.3199797620635616, 0.27108047713718747, 0.31439057476863796, 0.2434390064248951, 0.3547271524442087, 0.038456149951458574, 0.4434899567199142, 0.29923454179710524, 0.20843042692890995, 0.21158766245415778, 0.07461233262909928, 0.15457381991751543, 0.0034836934245318085, 0.042189080035131, 0.21504519130405025, 0.1574030656210009, 0.010231759346027852, 0.018973917239864913, 0.49935559411606734, 0.399147989445431, 0.4027808601410564, 0.4922516159867946, 0.152412315864649, 0.2932433241373771, 0.1480408006279559, 0.24169788096212955, 0.1802643428875981, 0.4766712091800683, 0.36188068067580625, 0.27228076171240534, 0.39355608401504505, 0.4406043758487075, 0.38061658291630196, 0.46843719554493246, 0.20777903638048714, 0.01979079595344721, 0.21546431610485797, 0.024426818711405562, 0.21516446834526412, 0.3563434220858414, 0.1934857010632295, 0.4746773159593893, 0.17702726909680372, 0.4645952032022316, 0.3938154279439036, 0.4934340377418017, 0.13679895392461341, 0.06402576798730517, 0.36836975104511427, 0.2549398008557931, 0.34807087448813967, 0.09532623940061444, 0.2557394620091119, 0.12451272981544914, 0.2904407948491533, 0.49859128195800806, 0.29677969444968944, 0.11458467228586208, 0.06651971609072058, 0.31388059067520235, 0.13794200142053853, 0.40339510649392796, 0.32914113407482726, 0.18421802745211865, 0.03350202406244662, 0.1577411413149695, 0.3937050419511281, 0.10413292812526659, 0.04934683901315684, 0.0612629135825741, 0.35563759741279405, 0.08236711509115283, 0.021190691182530003, 0.10582999287867012, 0.2116191746357064, 0.3573633312461204, 0.446657518258025, 0.3602723925135416, 0.13426693257870415, 0.3092216745374046, 0.05635795918607828, 0.34703282703376914, 0.07361105666520706, 0.4135185321133587, 0.33995497109612227, 0.11379943910039031, 0.2709138731748952, 0.006322162635428008, 0.32552429328126975, 0.07001629380354749, 0.4374600238863363, 0.3476926966660273, 0.26257175864725507, 0.4845980962243131, 0.36133071705140485, 0.11752101545268345, 0.4213150020736594, 0.30149546276409067, 0.03482212121970146, 0.17651909198450189, 0.2948783010065283, 0.12077602491652684, 0.03048663124448736, 0.17113443053553878, 0.18593694341775596, 0.0928858079553549, 0.1994670803963934, 0.17813981564031267, 0.13858898289405197, 0.20316177596032262, 0.4105340077407903, 0.25311472226327825, 0.07941776261810782, 0.4758449109159065, 0.16357775114498885, 0.372061569570265, 0.2878675276974878, 0.4943527990098858, 0.1968313689185469, 0.1287260744774855, 0.4237377501931887, 0.2575119192180666, 0.41850836699572536, 0.2914280354879667, 0.3268532779087243, 0.1422089307735811, 0.04756160327187073, 0.13847872813337825, 0.14692764344981452, 0.09444526639383205, 0.31915012824562616, 0.1899265127174999, 0.3855052352286808, 0.17643726807856236, 0.12546569059595858, 0.465403485051643, 0.12065920236861613, 0.08989619661112211, 0.1353425890624955, 0.302378806542968, 0.13581862984577245, 0.0687744789130916, 0.43885368386565426, 0.06237302123700575, 0.03738813419466269, 0.4835573375501071, 0.1609047894089181, 0.18306029147200092, 0.10902915529931786, 0.25269422156553256, 0.025279630967617234, 0.15674592426587752, 0.2591932697799023, 0.11159745091874809, 0.422244340724673, 0.4932922979585017, 0.10723039243155977, 0.35964185206994465, 0.35130596189585367, 0.3565752013986988, 0.15903692189347876, 0.37709404302782085, 0.20760731567592977, 0.35753571026452846, 0.31588948858340227, 0.04230082747023603, 0.09377327977736863, 0.35426396638540725, 0.001842693110780419, 0.10935826928885731, 0.23748437410983397, 0.013722021671681711, 0.23550553635614024, 0.2914705350859583, 0.21287509737381535, 0.06970566890800026, 0.3591885267310611, 0.2372173628107813, 0.06313050552991023, 0.1578137628356449, 0.2125204669558666, 0.003500677679032199, 0.1208282003581648, 0.4989231902454276, 0.38900558724764533, 0.3258170359269885, 0.4195360542273958, 0.3863420460823729, 0.43712512786774504, 0.2500627632873561, 0.42934288026055367, 0.04161441641729399, 0.3500400633832698, 0.09003514970714724, 0.0423969794155056, 0.3292430896268047, 0.1897870797590341, 0.002080364610115626, 0.12299057015800072, 0.048854490982413096, 0.4357757664959627, 0.11201424143814598, 0.06632436911582221, 0.1517451514017328, 0.42763375450346686, 0.25736480421634544, 0.38646787528528437, 0.432750641884575, 0.482465426804653, 0.06028817628646216, 0.48347360176702403, 0.4562340348801977, 0.1688847349143317, 0.39492694376691917, 0.17473710703236384, 0.1286630609342996, 0.08474541712371661, 0.4379864506483261, 0.3948489677742818, 0.07170569741150881, 0.3374651516643056, 0.16217701675431095, 0.3163982498973724, 0.3738784676143316, 0.3738653415270715, 0.25855614219742906, 0.16762810775589923, 0.32496299750116187, 0.13070163732740947, 0.09271722245206515, 0.3804104665773519, 0.1635669009151119, 0.031502024272674234, 0.1352128263329362, 0.4562188061840201, 0.08193775695207753, 0.23821873872369947, 0.2277978475762926, 0.28545209754893075, 0.2622501176635511, 0.17873932601521392, 0.26727671763511845, 0.1312821114568234, 0.23413592578814474, 0.2181311673007872, 0.20096189284784743, 0.22381162294974022, 0.008055386802269915, 0.474657457713876, 0.4892731852203757, 0.4400123677148424, 0.2659411765277737, 0.023788885228477052, 0.21537074893987745, 0.07525672783855061, 0.0022676070837934492, 0.44258567250285485, 0.33442321837866995, 0.4548191094955829, 0.4742156401402625, 0.4541200081087184, 0.3341089366295147, 0.3730766544350863, 0.40804049807262927, 0.03250586838312308, 0.4852490862906965, 0.331575859971311, 0.44049812184898435, 0.2518495326340293, 0.13523747797617608, 0.23225046635616467, 0.3013196522049695, 0.46736988725124345, 0.10687088263485156, 0.34195282379185815, 0.11513109393071838, 0.12288298852956722, 0.23848409164880452, 0.07604071519021854, 0.4488405567940096, 0.3707024167029086, 0.16678809120707905, 0.14149458767077494, 0.3607340403450109, 0.13370588668251124, 0.25042415953101005],
#     #     'c_rp': [0.29305109583970174, 0.4530492273111282, 0.018039505271968015, 0.09434744955635427, 0.10819765253425412, 0.33886461013755403, 0.0392000375969328, 0.4185943052388434, 0.49224821016320486, 0.37766346297740067, 0.3580496340984115, 0.22697426854313624, 0.33185943909237503, 0.028651584905286687, 0.06646147330108348, 0.3758414284603254, 0.08583458048216969, 0.168141090715703, 0.14339541102681558, 0.41667172329694374, 0.49533526207542056, 0.2051582309692963, 0.3888796487225458, 0.39966459237796864, 0.25520417455317373, 0.234675718957089, 0.08039980607456565, 0.27785016808788926, 0.2239520501220471, 0.22312548948232802, 0.1400638613407988, 0.112242735510307, 0.08058816490495274, 0.4538332039048552, 0.0031535899599273165, 0.2705637170897369, 0.15360592521093874, 0.32640255306778276, 0.4358492133362926, 0.3307422026351339, 0.10706681752362673, 0.1176025596501023, 0.32898567710201454, 0.09974849754945048, 0.36845466887326056, 0.2390897754598872, 0.3560989342184031, 0.12774115442628148, 0.2827292236355814, 0.3346490952052308, 0.23028249763863085, 0.06611918460967042, 0.36101013350234845, 0.06951565294349171, 0.40403259185691226, 0.12460954570466504, 0.07582146345176022, 0.32056989186025553, 0.3220257763494133, 0.4672958239713628, 0.020395518543301794, 0.28792634940272044, 0.004328483671299677, 0.3294162656684434, 0.13339681423932104, 0.2098940164066903, 0.15965883291689165, 0.35756051454358484, 0.28305142516204224, 0.2080078891796156, 0.3902723720679149, 0.2667627979495921, 0.033940212356825095, 0.11451561651688863, 0.43986866284368004, 0.4766297661647734, 0.3189556897421582, 0.33138827026469797, 0.4586439575320423, 0.02291079686770936, 0.4652949804596518, 0.31546887660502104, 0.33562174128044964, 0.2889051137625315, 0.2644839547571613, 0.2116408290865045, 0.3655108504348802, 0.1344266791810848, 0.33156195784310866, 0.05715820660006998, 0.2591533994793417, 0.06749497339785049, 0.48941797714816054, 0.06196142567895657, 0.4840469220995249, 0.1498690026933226, 0.09760196348648542, 0.045975038420473846, 0.1097910523874146, 0.4158724561515044, 0.09701493373917003, 0.25196064409412866, 0.49549191607067744, 0.43996354067202714, 0.2658804099595618, 0.20353809006109203, 0.4269663242507702, 0.21183366745567767, 0.28149288186575266, 0.13437914837363035, 0.05813381114178828, 0.15973447782080763, 0.3362184077183177, 0.43308694287057536, 0.26603371479954413, 0.43257756859048846, 0.21450199184308244, 0.2187093633200004, 0.1183273036406372, 0.14326617597210745, 0.18962904608491815, 0.4980118784097719, 0.24682047807409113, 0.23186317543110763, 0.03461702431935487, 0.3610969459253352, 0.0822838134311078, 0.18885305662971408, 0.31115896159235457, 0.46894826486106916, 0.11853028004358901, 0.014382924952413056, 0.23264416940912674, 0.062405533169750116, 0.3849564241191391, 0.166328358213429, 0.29644216191095313, 0.38546731576197774, 0.11784889449436209, 0.1254057645650255, 0.32121337901775143, 0.15010476076968782, 0.3638361623379451, 0.08491226798470525, 0.26668447235735376, 0.14505633563484882, 0.26878336263360986, 0.17715554263913974, 0.12351155441698713, 0.1542335211592505, 0.3567567116473269, 0.476773620095601, 0.03521143814945232, 0.2962782401632161, 0.35047379478806, 0.40673907081515465, 0.3716327120198251, 0.2980391634922567, 0.30627917188228, 0.4919608201386479, 0.1352306505222295, 0.326594835251981, 0.06580958988883706, 0.24446935782531803, 0.431287248078709, 0.31157789301690925, 0.303197302047499, 0.22227002766453413, 0.27402931523585494, 0.16093477183825688, 0.39045580329018137, 0.05014129977134413, 0.017072203949424658, 0.34767521197142065, 0.39184874521555796, 0.47838978944071164, 0.21656701492269886, 0.2823501910105685, 0.051172932620985934, 0.4841132767713062, 0.3850454971623754, 0.17103098784824555, 0.007603104765638691, 0.1445640532177584, 0.041207088160401806, 0.08938309276451067, 0.15878123476240663, 0.49462570723178223, 0.40162646284609943, 0.18357061854549833, 0.23425595506622338, 0.14726809173935695, 0.16603922764328127, 0.16982152253041338, 0.140154297349523, 0.2028953283359165, 0.23407932486914385, 0.22071586725458625, 0.10208788743715641, 0.36804434056308444, 0.3215341920731422, 0.1576057666003638, 0.3619692774762814, 0.17145384450112178, 0.44952367862508136, 0.33422120621366497, 0.2742344546322808, 0.04160411476785453, 0.43811613746471606, 0.06173250883901288, 0.3196264803801886, 0.3889582921313644, 0.09504491131138892, 0.17030915275132386, 0.09581518030153735, 0.06725943963205633, 0.03897326684321961, 0.11460372591990403, 0.08468877235164762, 0.032266937678763874, 0.15139860396812876, 0.1973474664298584, 0.35371602150726156, 0.3966494085895933, 0.3876396431579289, 0.37732982047688063, 0.15587531397384313, 0.3560358362113458, 0.14846747206121846, 0.1650009010210985, 0.0770395900344355, 0.4271174896512673, 0.35974671225771604, 0.32449541834123896, 0.39040640735735854, 0.39463722635014303, 0.44962946590501707, 0.3491048894001431, 0.14459323807866642, 0.23798581741092445, 0.04289760621506489, 0.00204566105943893, 0.07396036628738012, 0.31598984258019386, 0.1411588948441953, 0.2728356691582311, 0.11965193850504308, 0.31474102708064283, 0.292665223125272, 0.27391946560093444, 0.19532999162381443, 0.07279257067381106, 0.3502132383881055, 0.48799831564427676, 0.43386420672706916, 0.07578790957944648, 0.38320685586138664, 0.23065622469552427, 0.4779819263275768, 0.3334273397009618, 0.4509982436798631, 0.2083356122659093, 0.08185839994844346, 0.3106564263043143, 0.019447265331200503, 0.358119371423159, 0.29882057411364116, 0.010122341881434627, 0.07830272320021003, 0.21765959694030612, 0.2714984324558488, 0.1247799183491411, 0.024544876691864503, 0.20631058910633804, 0.4225226949674675, 0.22207746614763885, 0.2086235105124184, 0.04297448413977567, 0.11990433945545131, 0.3524490599956247, 0.26028555166956624, 0.39540800480508426, 0.23420506732826968, 0.32202189787009644, 0.23085509248716496, 0.28677007272141286, 0.22451805224355892, 0.2552678618308878, 0.4334964831094621, 0.016651750829678236, 0.3630976031645642, 0.017731781474143837, 0.3661046981193648, 0.23221519164466314, 0.306333000328948, 0.31940530505750964, 0.37359944091575253, 0.28697877404937416, 0.3149819310886091, 0.002660277883232698, 0.38891099975360416, 0.3895783548670114, 0.09290884512083564, 0.11381440322314906, 0.256141203538724, 0.0810735473712278, 0.04592283936011865, 0.21161869052336507, 0.15483912913396264, 0.09214401320473492, 0.07236569739249255, 0.005181227614574513, 0.09981280093757466, 0.14895295988415824, 0.3453429042844626, 0.29334075208634464, 0.03493278826606466, 0.3596245877357025, 0.12394344527400541, 0.3760615465692037, 0.4961674013194515, 0.3294676092303929, 0.05553381542187619, 0.029114885708327987, 0.3089310714010298, 0.48208843553199215, 0.38168923212828626, 0.4073879190979773, 0.4387745744687672, 0.12576170473710713, 0.24552978125516634, 0.2019300557915074, 0.14236599730476074, 0.09743368109317946, 0.28457274217742023, 0.08760861908430106, 0.4407201588685031, 0.11732798490054297, 0.002820352442308549, 0.42097220742030544, 0.14896589682001038, 0.01773460146646022, 0.16650018215984086, 0.35552047771319817, 0.10758509665717736, 0.2350052011102033, 0.2550006701663568, 0.125438581199532, 0.23024682752189346, 0.4087635053357187, 0.10518986301804917, 0.019729634367785687, 0.1499681544779946, 0.3596361262884921, 0.04823516626424462, 0.23395165146739438, 0.2822634845438052, 0.1339818386538983, 0.34837532359848844, 0.35709748968217186, 0.22777366560760792, 0.42385700040984087, 0.4068138061407621, 0.30947615231824943, 0.12404768264509769, 0.47365610086566573, 0.01123866650514277, 0.259555186762302, 0.4449597965850561, 0.08705949586281847, 0.08421940424998786, 0.31139847475877425, 0.22506175838321674, 0.03775377303534827, 0.10447659634139117, 0.2461837102231949, 0.06553598314519588, 0.4331203027752678, 0.14517163038281394, 0.01316341523546749, 0.29664687140004126, 0.24725384091949404, 0.1721598126982724, 0.13765448007030617, 0.07721605641420931, 0.052619140173472745, 0.10788792889883297, 0.41778208035501346, 0.3978570107408519, 0.3931275597860729, 0.46155364957985295, 0.38489338571275733, 0.4440936415600934, 0.27914815090824, 0.29015180746973956, 0.17656496346085043, 0.4565262860406956, 0.12268498514507997, 0.09503608814678183, 0.48006186885181057, 0.1761126002440126, 0.15220003758451084, 0.2060786886214624, 0.205253129354862, 0.49620258949153934, 0.052726973168308267, 0.03542404512180369, 0.07076953721560181, 0.3787018028521418, 0.3615848313181386, 0.4927874061792348, 0.4480782500082847, 0.30786606582331844, 0.22786768486405445, 0.4848634640602126, 0.47633124267043714, 0.007082395331306279, 0.4065706579977465, 0.11875854587312068, 0.1919562678026817, 0.2075959464586722, 0.46307228839836334, 0.30809488064634777, 0.22507552346515752, 0.2962207560155988, 0.04700857713015116, 0.27881480354934113, 0.314384277891236, 0.3667423751189729, 0.2594717193247999, 0.20096903747102596, 0.2570612221158943, 0.12417276215437117, 0.23258932836332735, 0.44454815409340775, 0.10966184539401774, 0.11212948474391499, 0.15288942838067804, 0.3158157388549384, 0.05373295370496611, 0.2479146811713271, 0.22258632719050175, 0.4839493085413665, 0.42457022590078936, 0.0253150341458116, 0.35542724429584116, 0.004353829995428493, 0.21669537657763122, 0.2140989375743712, 0.0672568016203407, 0.017396453296925407, 0.006370537345295246, 0.399208281484869, 0.2540901583028169, 0.38477012709075237, 0.25581651704378366, 0.18767624139186728, 0.17062589607322654, 0.13948316238591313, 0.16726185642946534, 0.3582207780557163, 0.47799026002553824, 0.4656141819650548, 0.4604440626669489, 0.42410513989575255, 0.32816994975059227, 0.2993495762330556, 0.3421948402575753, 0.06326981645293872, 0.48128936260468835, 0.3524475201910982, 0.3883835351700534, 0.27299596376583246, 0.08002345745278272, 0.18035772092087476, 0.34895288163513616, 0.4767364166231759, 0.24514814311552996, 0.2868498605933061, 0.24316193317763207, 0.0036478152990372936, 0.12572515347537444, 0.18046135885135245, 0.26826019996586725, 0.3199298154398646, 0.0743213109160265, 0.24762491170081052, 0.27656812111045315, 0.24192136071361003, 0.36137404094026837],
#     #     'replicas': [2, 0, 3, 3, 0, 4, 4, 3, 5, 3, 1, 5, 2, 2, 3, 1, 0, 5, 1, 4, 4, 3, 3, 4, 1, 3, 1, 0, 5, 5, 3, 2, 5, 0, 2, 0, 2, 1, 3, 2, 1, 3, 2, 4, 3, 1, 0, 0, 1, 3, 3, 3, 2, 5, 0, 5, 0, 3, 2, 2, 4, 3, 0, 2, 3, 4, 3, 0, 3, 0, 2, 1, 4, 4, 1, 2, 4, 2, 5, 2, 1, 2, 0, 1, 4, 2, 5, 0, 5, 4, 5, 0, 4, 5, 1, 5, 3, 2, 4, 5, 0, 0, 5, 0, 2, 5, 5, 3, 4, 2, 0, 1, 2, 4, 5, 1, 3, 2, 4, 0, 3, 5, 3, 4, 0, 4, 2, 0, 3, 1, 0, 2, 3, 1, 1, 2, 5, 5, 2, 5, 5, 0, 5, 1, 2, 1, 0, 1, 3, 3, 2, 3, 1, 0, 4, 1, 1, 5, 2, 0, 2, 2, 0, 2, 4, 2, 0, 1, 3, 0, 4, 3, 2, 3, 0, 3, 1, 0, 4, 0, 2, 2, 1, 3, 5, 1, 5, 2, 0, 3, 1, 5, 3, 1, 1, 2, 0, 3, 0, 5, 3, 2, 3, 3, 4, 2, 5, 2, 3, 4, 3, 5, 2, 2, 4, 4, 5, 2, 4, 2, 5, 5, 1, 4, 4, 1, 2, 2, 4, 2, 1, 3, 4, 3, 0, 4, 2, 4, 2, 2, 1, 4, 0, 1, 3, 5, 1, 0, 5, 1, 2, 1, 0, 0, 4, 3, 0, 5, 0, 4, 3, 4, 3, 0, 5, 4, 0, 1, 4, 2, 4, 2, 0, 1, 4, 3, 1, 2, 2, 1, 4, 3, 3, 2, 2, 4, 5, 4, 3, 0, 5, 2, 1, 5, 0, 3, 0, 5, 5, 1, 0, 0, 3, 4, 4, 2, 5, 4, 2, 3, 2, 1, 3, 2, 3, 0, 2, 0, 5, 3, 5, 1, 5, 5, 1, 5, 5, 3, 2, 0, 4, 4, 1, 1, 5, 2, 2, 1, 1, 0, 4, 1, 1, 2, 0, 1, 3, 5, 1, 0, 1, 5, 4, 0, 1, 3, 0, 0, 1, 5, 2, 5, 1, 5, 0, 1, 2, 5, 1, 5, 0, 1, 0, 2, 1, 1, 3, 0, 5, 0, 5, 3, 0, 5, 0, 1, 3, 3, 5, 3, 0, 3, 1, 1, 1, 4, 3, 0, 4, 1, 2, 5, 4, 4, 2, 2, 5, 0, 2, 5, 3, 3, 1, 1, 0, 4, 3, 2, 0, 3, 5, 0, 0, 3, 4, 2, 5, 5, 3, 5, 2, 4, 1, 0, 4, 4, 0, 1, 0, 3, 1, 1, 1, 0, 3, 4, 3, 5, 3, 2, 0, 4, 5, 5, 4, 3, 2, 5, 0, 4, 3, 0, 4, 5, 0, 3, 1, 5, 3, 2, 4, 4, 0, 2, 2, 5, 1, 1, 3, 5, 2, 2, 5, 1, 4, 2, 2, 2, 0, 0]
#     # }


#     # test3 main_init(50, 1.0, 600)
#     init_popu={
#         'h_m_cost': [[0, 0.7, 0, 0.5, 0.5, 0, 0.7, 0.5, 0.8, 0, 1.0, 0.8, 1.0, 0.8, 1.0, 0, 0, 0.5, 0.5, 1.0, 1.0, 0.3, 0.7, 0, 0, 0.4, 0.4, 1.0, 0, 0.3, 0, 0.8, 0.8, 0.4, 0.8, 0.3, 0, 0, 0.8, 0, 0.7, 0, 0.7, 0.4, 0, 1.0, 1.0, 0.5, 0, 0]],
#         'map_v_h': {0: 3, 1: 32, 2: 20, 3: 12, 6: 27, 7: 19, 8: 7, 9: 11, 11: 13, 12: 8, 13: 46, 14: 14, 15: 13, 16: 26, 17: 40, 18: 10, 20: 34, 23: 31, 24: 4, 25: 45, 27: 1, 28: 17, 30: 34, 33: 47, 35: 21, 36: 33, 37: 22, 38: 42, 39: 25, 42: 38, 43: 35, 44: 18, 46: 29, 47: 43, 48: 6},
#         'c_rp': [0.46753713484069664, 0.04636662319671786, 0.36371410421672207, 0.4397808694328428, 0.4520105196828375, 0.31461687878874167, 0.3084256333815727, 0.4742530600854063, 0.017754557750803313, 0.2312214598223868, 0.24854485264716403, 0.12117745138186053, 0.08411418388687258, 0.4813761608575876, 0.4584421878210625, 0.4311042102652728, 0.06030912629059282, 0.3546110038595228, 0.2436129220414398, 0.4395827964180183, 0.026328558782577338, 0.26766806339929994, 0.006353103024922424, 0.09959422261955131, 0.22130101987189532, 0.016946830056633833, 0.35476164307933156, 0.4841656305638405, 0.23428761143518467, 0.08205125986030393, 0.3092315521768564, 0.1274451485902971, 0.23279820556475678, 0.14945648131649303, 0.2312650054751273, 0.054880766329289676, 0.4995655577264974, 0.48778459417937425, 0.36418955523344476, 0.1499584651749215, 0.0008667751566664439, 0.36070225961836067, 0.3915062248864705, 0.23398259755537487, 0.3868337465598162, 0.44604448020561355, 0.09225837623573824, 0.04888351328699364, 0.1507781185704513, 0.08993184619937827],
#         'v_m_cost': [[0.40206563669168577, 0.395672014084409, 0.7278715738116328, 0.5764138102472568, 0, 0, 0.5774414606596321, 0.959555131472364, 0.2809412119846755, 0.317306724557739, 0, 0.20008118367666572, 0.40450467583570693, 0.32939835167536746, 0.05152646699594893, 0.164431857780547, 0.21894466415527922, 0.3178541924587413, 0.9146710859406961, 0, 0.0837220241419647, 0, 0, 0.4071688603133601, 0.41646356801546236, 0.5859872501820467, 0, 0.09383084325781946, 0.43286443648377915, 0, 0.21425453828369292, 0, 0, 0.4497682224419286, 0, 0.03036755720668652, 0.17571875757737992, 0.5262524190389926, 0.3738339515362714, 0.11207395576043322, 0, 0, 0.2159899214861732, 0.04549673532072929, 0.315909771808345, 0, 0.24647529340792082, 0.39649545740251935, 0.1315936360904222, 0]], 
#         'v_rm': [0.5, 0.8, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.8, 1.0, 0.4, 0.8, 1.0, 1.0, 0.4, 0.4, 0.7, 1.0, 0.7, 0.4, 0.5, 0.4, 0.8, 0.5, 1.0, 0.7, 0.7, 0.5, 1.0, 0.4, 0.3, 0.3, 0.5, 0.3, 0.3, 0.4, 0.7, 0.7, 0.4, 0.5, 0.5, 0.8, 0.3, 0.5, 0.8, 0.3, 0.4, 0.7, 0.5], 
#         'h_p_cost': [[0, 0.8, 0, 0.6, 0.6, 0, 0.8, 0.6, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 0.6, 0.6, 1.0, 1.0, 0.3, 0.8, 0, 0, 0.5, 0.5, 1.0, 0, 0.3, 0, 1.0, 1.0, 0.5, 1.0, 0.3, 0, 0, 1.0, 0, 0.8, 0, 0.8, 0.5, 0, 1.0, 1.0, 0.6, 0, 0]],
#         'c_rm': [0.41646356801546236, 0.24739699398976775, 0.3889996083957719, 0.3790975481868236, 0.45990303310677655, 0.3178541924587413, 0.4497682224419286, 0.30685818984825136, 0.010189429553198737, 0.21425453828369292, 0.14865947314328073, 0.20008118367666572, 0.14827502009464125, 0.315909771808345, 0.27058327081138067, 0.3102296672940231, 0.03987486975677568, 0.40206563669168577, 0.21894466415527922, 0.43763989050828445, 0.11207395576043322, 0.3785383593803085, 0.03079564948473476, 0.17571875757737992, 0.03036755720668652, 0.06360428424224832, 0.47703119543241174, 0.4296681049814891, 0.24647529340792082, 0.04549673532072929, 0.32939835167536746, 0.164431857780547, 0.14612971564735883, 0.1935476963719354, 0.028630500933051584, 0.1315936360904222, 0.2865110750730042, 0.40450467583570693, 0.39649545740251935, 0.02226911158125605, 0.1874142018514849, 0.3775929458957118, 0.34877402562480914, 0.09383084325781946, 0.4105953249025231, 0.49965209836558755, 0.08739351561274009, 0.05152646699594893, 0.04384715438518902, 0.2159899214861732],
#         'v_rp': [0.6, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 0.8, 1.0, 0.8, 0.5, 0.6, 0.5, 1.0, 0.6, 1.0, 0.8, 0.8, 0.6, 1.0, 0.5, 0.3, 0.3, 0.6, 0.3, 0.3, 0.5, 0.8, 0.8, 0.5, 0.6, 0.6, 1.0, 0.3, 0.6, 1.0, 0.3, 0.5, 0.8, 0.6], 
#         'v_p_cost': [[0.3546110038595228, 0.13048080708359044, 0.8312870943193134, 0.3645808793733885, 0, 0, 0.9326952479064687, 0.898054999888451, 0.24171485755223127, 0.5059186607514199, 0, 0.12117745138186053, 0.48778459417937425, 0.3092315521768564, 0.04888351328699364, 0.1274451485902971, 0.2436129220414398, 0.31461687878874167, 0.7943444394973498, 0, 0.21108724486104413, 0, 0, 0.49893306887442723, 0.46753713484069664, 0.7347183938794006, 0, 0.23398259755537487, 0.5367922117347377, 0, 0.2312214598223868, 0, 0, 0.3084256333815727, 0, 0.22130101987189532, 0.09959422261955131, 0.6092471122655247, 0.4480510403219066, 0.026328558782577338, 0, 0, 0.08993184619937827, 0.08205125986030393, 0.4813761608575876, 0, 0.23428761143518467, 0.36418955523344476, 0.054880766329289676, 0]],
#         'population': [[[24, 4], [1, 32], [3, 12], [2, 20], [7, 19], [17, 40], [33, 47], [6, 27], [25, 45], [30, 34], [37, 22], [11, 13], [1, 32], [44, 18], [6, 27], [38, 42], [20, 34], [0, 3], [16, 26], [18, 10], [39, 25], [23, 31], [9, 11], [36, 33], [35, 21], [38, 42], [18, 10], [25, 45], [46, 29], [43, 35], [13, 46], [15, 13], [25, 45], [8, 7], [23, 31], [48, 6], [9, 11], [12, 8], [47, 43], [28, 17], [3, 12], [37, 22], [2, 20], [27, 1], [28, 17], [7, 19], [8, 7], [14, 14], [20, 34], [42, 38]]]
#     }

#     addtion0={
#         'c_rm': [0.37186574350901574, 0.4165091557639013, 0.47480830960171416, 0.44651334770861395, 0.2961709326780183, 0.4297780657277471, 0.37096497523868377, 0.4340253092995384, 0.3000643746249745, 0.45176905716932925, 0.025905679526446013, 0.27686828332273994, 0.0435487512082216, 0.4896802932035266, 0.08157194232401355, 0.03257871119238895, 0.22295847154296772, 0.0697779377433553, 0.18447013561042763, 0.1381592942888916, 0.25057003431525593, 0.12356390820844909, 0.14982515842577013, 0.42912813605218053, 0.19823435610518597, 0.36266387601831784, 0.3243716072219618, 0.239389814330686, 0.3183561553611596, 0.49569395092501645, 0.28485795236586714, 0.3261090120570394, 0.23261764216552847, 0.30579709458937443, 0.03658643112222809, 0.04361156799134794, 0.15859137940569373, 0.27805453039043915, 0.15974932749697107, 0.03685759001541139, 0.42667914363366233, 0.24162512231542962, 0.1724622541347531, 0.41768513380349015, 0.4649275481692375, 0.10367898563876324, 0.29652686397176575, 0.40746837467530705, 0.43491596451989967, 0.10862551619973373, 0.4881166896209102, 0.36810032130968673, 0.3250848448428578, 0.279694489960741, 0.18162203789563455, 0.12133127907137131, 0.13936967386749968, 0.32631595574818545, 0.04390947952066396, 0.11443945697006658, 0.2491779456995943, 0.036518303945034386, 0.033171519106168446, 0.2912708427571312, 0.2598735903089284, 0.10866976349731791, 0.3647790571410142, 0.15941353990031543, 0.06985524274350224, 0.17735499944777658, 0.017360963104863236, 0.46385673953529727, 0.23067437288193596, 0.06119155069163246, 0.18700290760971133, 0.45723279539129924, 0.22459301719204583, 0.4560313253829514, 0.19108111144123352, 0.13216610627885278, 0.1526790276078844, 0.18915053627432094, 0.4424268507057554, 0.050907842823829624, 0.12948896048958394, 0.09681853608485219, 0.24020313975126292, 0.222932275909643, 0.0630251050531897, 0.19159246468154587, 0.19779068621643014, 0.016607488521059532, 0.4225734355404382, 0.31956679316022574, 0.13335817951350684, 0.36294344902314524, 0.21390052409101604, 0.020069858832430315, 0.031563134177735486, 0.31733283983136273, 0.2612616261043156, 0.4901978646392669, 0.1822585550742889, 0.10189485167015286, 0.15836179311747747, 0.1735337517128837, 0.2509999993876843, 0.33073558041309553, 0.392027350699464, 0.18448940786953394, 0.14641150576010656, 0.039393361477761984, 0.4284376821383463, 0.31795373405370475, 0.1286786887615868, 0.027050445955327712, 0.2908346101666075, 0.10560789302275789, 0.2151424501339909, 0.009610747937471964, 0.025911456850036735, 0.0991105089886587, 0.44958281018399715, 0.06221273108932082, 0.4788710482015005, 0.3370311728784082, 0.08033137219602118, 0.4922703043947412, 0.4958064769176814, 0.30431918827794835, 0.23426801262512686, 0.47725710702208696, 0.2692053102869282, 0.07666703355591453, 0.1366822237546619, 0.096212681437128, 0.28305692323240333, 0.31257738562354265, 0.4812849939149194, 0.29361176599844696, 0.40775828109456447, 0.4462774904699932, 0.20205601493252076, 0.22262164697683082, 0.26358180196412534, 0.3243089269096472, 0.4898838601082382, 0.39606990793331814, 0.3101509307737651, 0.1365646701695994, 0.4423696941623717, 0.08705449326928322, 0.3954136205595406, 0.07072671636873429, 0.48667391139525773, 0.13861872892374597, 0.041586017170815476, 0.4247183812770222, 0.009394012472246666, 0.3111627719006852, 0.19837069427244008, 0.22365552959794546, 0.3655716024132649, 0.24475676872130395, 0.07653348263317095, 0.27562310323492833, 0.35513981883814705, 0.4331941994881573, 0.27728204699158254, 0.39718129786737527, 0.3788937650563507, 0.35540780317508036, 0.24158704684652607, 0.06700472674178223, 0.15469546387977248, 0.09532356126070013, 0.18936582221529227, 0.181206803964337, 0.28657837894968335, 0.08083289845975883, 0.48500571276418625, 0.3693952149610521, 0.31324680035247454, 0.4319819905179228, 0.4497314237599393, 0.3221293032806861, 0.3953161327980943, 0.03152454291115683, 0.38933498787366505, 0.037851259101837315, 0.2730788204290633, 0.050773487398160205, 0.20646964478025262, 0.04433674647532662, 0.4404281270961163, 0.01569481647424284, 0.3468000858476531, 0.17783409469996872, 0.08085683952140346, 0.11222808315162983, 0.14646014585648381, 0.287280148771895, 0.3100959046940429, 0.044476846845800944, 0.4589218218519512, 0.23764142646618006, 0.2979786403303784, 0.15400359764853316, 0.28252613553064854, 0.44163384637376, 0.1232422330924926, 0.05005564947797844, 0.1575060763917627, 0.176743466614971, 0.1211956396213037, 0.4462489880636383, 0.23077885756321778, 0.4314907484331479, 0.33963992522556546, 0.4969046026253558, 0.21265415020491918, 0.35792666204481594, 0.1350212912492205, 0.15459043102387138, 0.4586550980752039, 0.12804381108580018, 0.4636767488264291, 0.027118957811320538, 0.24379818225520913, 0.35931195338488364, 0.3941696658801176, 0.2409017797525234, 0.31170499251315287, 0.46024883207099565, 0.09879252993785434, 0.3071250296216007, 0.13380842114820402, 0.1953058607220961, 0.4486226966457955, 0.23907333364658317, 0.010485555368688781, 0.41249487283650443, 0.1676902777380918, 0.3466473354000649, 0.43273385758230337, 0.02929359715258517, 0.18654046722986478, 0.05607298796927923, 0.12081350951536698, 0.4266126891192913, 0.14750399004251058, 0.32711944893627765, 0.23880371027348096, 0.1944415132692643, 0.029923664931516297, 0.1870962972129366, 0.08212230274068924, 0.06005524356336528, 0.24965375424785438, 0.3832880240195119, 0.06523531692833828, 0.0953520010845113, 0.3041737475145774, 0.39543425770177376, 0.24461529699559012, 0.43052568691491244, 0.20539900543745382, 0.06077528060593365, 0.04300107348972845, 0.4586741409742616, 0.4798468056135088, 0.31543483422547364, 0.03193725807845421, 0.1730126131569832, 0.27911855465169644, 0.31400218625616727, 0.3635667467429542, 0.1265195194633813, 0.22326151207974854, 0.1315692603120025, 0.0037961477415163203, 0.44907417155141105, 0.1373395611998061, 0.08220735228631032, 0.13733598230941882, 0.0537032106335853, 0.10739281735490658, 0.27351453490285227, 0.43783301662026197, 0.16001013750639803, 0.18765544600997516, 0.06517163060803241, 0.4128776260935768, 0.11149155223140489, 0.026619823430797107, 0.03459413123454022, 0.34760296017647496, 0.2302268348659491, 0.45448137300501706, 0.20642738865701776, 0.03823834203629786, 0.0007753729953149657, 0.22174570508374195, 0.39618115870065607, 0.07833924392571062, 0.49369201616328817, 0.24754217467448425, 0.4220036027957617, 0.2568851442329897, 0.03740702905705262, 0.016940333430792986, 0.38296448121948634, 0.35345491984603405, 0.3718791533257564, 0.052238852337570474, 0.1664898601406886, 0.14704531829880388, 0.3572905541501804, 0.06379097366979444, 0.008729369156874833, 0.20885151424848644, 0.22384378718358655, 0.0383085370173428, 0.06978290173308863, 0.20114311617553302, 0.48416505833489687, 0.47003363094011485, 0.0729377105753945, 0.320288828178974, 0.05656814088671072, 0.20125899759873206, 0.15734930935949226, 0.4360444720861231, 0.27134951839330557, 0.16624945102124714, 0.31534818535607106, 0.03958639668243347, 0.38526245580192364, 0.2845275028561286, 0.2072631621954612, 0.23279141155406655, 0.14322808519584734, 0.047662138349305105, 0.3983392223462474, 0.13454292141576873, 0.29005838883568913, 0.08604498153308626, 0.44874457600692164, 0.16128113923613605, 0.4651869310247969, 0.2917064840972865, 0.3819560474450556, 0.10598616846789563, 0.3423797995156745, 0.37917151242503144, 0.4776715249409881, 0.033816566246092084, 0.42849599472664074, 0.061954453882369476, 0.33671468622441214, 0.05811894071420892, 0.16719067503560917, 0.037928358716759064, 0.16897357004587826, 0.3562465529710728, 0.34775432890860514, 0.4997444161563169, 0.4975384774576561, 0.421349520139142, 0.12051406340349563, 0.19284903567540507, 0.16143321140704864, 0.16811622952410754, 0.1857940804366549, 0.035240214647034, 0.35859534256061154, 0.25200886505645514, 0.003875881071891324, 0.452778274003573, 0.26618504176514346, 0.04712194082067947, 0.29319761530808075, 0.2498009275682448, 0.40348967138546843, 0.2275540657687761, 0.485494731102874, 0.2698467202758207, 0.181644609750766, 0.14932766726891436, 0.33622199270068504, 0.4414763241706361, 0.05981915955464334, 0.24330823638686974, 0.23678657139260875, 0.4447594561848196, 0.4668675667929868, 0.0641139652666346, 0.08323841959322523, 0.4580895236938832, 0.47003140071109817, 0.1638295899226412, 0.29127744908976905, 0.3757803809040036, 0.49011617460172174, 0.2997970408645596, 0.12067014174607496, 0.4031457478090167, 0.3662179367986232, 0.1722479854875871, 0.4226463245463712, 0.3609609847658265, 0.3508917912184096, 0.35935791567844416, 0.40778860095906877, 0.32151668059031996, 0.08092134956198554, 0.4298224127949589, 0.11753311384619822, 0.18498527288036826, 0.2231019368667597, 0.4138908688888082, 0.3424760855863912, 0.21921216762340498, 0.1405978427178143, 0.24187459847222356, 0.00738960871901187, 0.463917796204644, 0.2049753091080488, 0.15204302986039178, 0.40833424712026883, 0.47085666959755035, 0.21682933212913377, 0.34443363063434296, 0.08509035838606238, 0.12386327420025905, 0.40077475690419373, 0.20985957984040435, 0.2861252125328251, 0.12085365210580096, 0.08506759970168787, 0.2473044818924713, 0.1966374511685269, 0.37698607184554, 0.3980093212420181, 0.3449196637076407, 0.1761329888418641, 0.27856444882544096, 0.46800227585186455, 0.1331240275725011, 0.04516082204838248, 0.19837766828744471, 0.2537247709910397, 0.09708878058815085, 0.4942435363318268, 0.11799283353467332, 0.08031891547743522, 0.4406721431575652, 0.20363129636914423, 0.44016718449154646, 0.4871137315358923, 0.03965678878295387, 0.21236270365307017, 0.21902313170305138, 0.22926298065542383, 0.42916592444470303, 0.23850759994866577, 0.29866000688050776, 0.2783530226808073, 0.09797818957140672, 0.018112751378431824, 0.4897421629609034, 0.24250897669958196, 0.061461428496457055, 0.3190689658650796, 0.044672489131371035, 0.14721708816132947, 0.43382938394563075, 0.24923545045208928, 0.2652884973171458, 0.40372194082045, 0.11019275797749123, 0.2381058467487387, 0.49128903999612245, 0.3488018522410332, 0.46882500290696105, 0.35532646819738667, 0.15679375454851402, 0.129308827740912, 0.04977202395369887, 0.09697446743831672, 0.39255626062351623, 0.30794079202635705, 0.09475701505718803, 0.07562327596379168, 0.3013442872746356, 0.0036421213974237865, 0.45874281452975646, 0.1462327245744063, 0.2610152465632267, 0.2745243144372929, 0.08019076832792274, 0.47180906516916693, 0.2507683636498813, 0.2556127564389057, 0.48127018625839335, 0.41941059392957536, 0.026555503599668295, 0.039325276548780874, 0.2587928734364193, 0.02354441367232374, 0.23330058780134766, 0.33723475489604116, 0.37399243390928966, 0.1372220111739931, 0.41051365834633247, 0.3373721672910944, 0.3001049569423673, 0.2269369442190587, 0.21644263672541167, 0.3112689238076273, 0.3054894831292154, 0.3200393760868323, 0.012790244816163199, 0.025386078421429342, 0.31846203198567025, 0.02558232489034243, 0.26396585067592815, 0.26434542179153164, 0.1301694169282346, 0.10626004299750075, 0.09115506894042677, 0.13591571037179592, 0.3074198007914759, 0.34275522350577925, 0.24109847455355907, 0.36740526588451433, 0.42693832210408544, 0.03009443466014372, 0.4865875846162281, 0.4534753329894743, 0.43669096419851283, 0.13035959169587608, 0.3917758461803158, 0.4673898122717218, 0.25158834233116045, 0.17968307757833654, 0.12420553739464357, 0.05919276680915944, 0.28048003267300314, 0.479629240389001, 0.22102431323394084, 0.35552223456150467, 0.41619168826924907, 0.15197637296798716, 0.33002553220175274, 0.01172981486525801, 0.40863165810673174, 0.43281493150621886, 0.4941458849082052, 0.3402771006545873, 0.29932142924735167, 0.33571396818956395, 0.40088289329073057, 0.31931030209475036, 0.07226107914400157, 0.27584447041649784, 0.22390443885921485, 0.44137200869606297, 0.05679954764408987, 0.3538787195742129, 0.08231716786716486, 0.3306093310558673, 0.4088761590298735, 0.005701646102374641, 0.0079407978636018, 0.02513534323015776, 0.020462690993900162, 0.20925325681889204, 0.48299629051078335, 0.2526271459405319, 0.1067456538729373, 0.05609332872864581, 0.3648953775146927, 0.4906739596634956, 0.4939894409098967, 0.02727515767778632, 0.18592186052538587, 0.0003212801587708647, 0.14053566758979222, 0.30506616683919585, 0.4289836931749391, 0.117926263652746, 0.47303925843095906, 0.19695734163665013, 0.15584274082317026, 0.3281175084414856, 0.25483461082253395, 0.013327699845649826, 0.4348668920523323, 0.011000457039012146],
#         'c_rp': [0.4833697458455798, 0.3755515869455199, 0.46990091217999114, 0.3763602746575489, 0.4543654546324348, 0.41269482311966044, 0.4981683607872964, 0.4707832480778932, 0.46997736886096486, 0.40651442819922656, 0.00929025530282207, 0.35042851986314905, 0.08367938113515766, 0.36552992962433906, 0.2248022739255227, 0.028477990432169475, 0.001020694745996642, 0.10934342376943229, 0.2487739014331941, 0.118373850391221, 0.483472563552339, 0.16985751014944755, 0.15238846001222855, 0.40317198082696776, 0.22925858242971525, 0.31673916594587764, 0.4132790520402505, 0.13259729967690825, 0.3887650139448799, 0.3606897008148494, 0.314380873107692, 0.3435948552881879, 0.24594622589392562, 0.32914763147163484, 0.23538308282673093, 0.14234804004905782, 0.01857201938582481, 0.2635115707298967, 0.1358019701091046, 0.04803323257386638, 0.361463410797461, 0.023968689782179253, 0.12096437409341965, 0.2844173555155676, 0.3057142872085872, 0.16785121397863523, 0.3688047788373409, 0.28272830767490487, 0.46378389781776813, 0.01170419764533237, 0.4670271645105812, 0.48382636260590545, 0.42703235824430946, 0.3751666736026679, 0.15374978572411796, 0.23541381268880163, 0.0824301575017023, 0.46279642126989357, 0.14325036177336187, 0.0407024335206837, 0.18857019851086465, 0.036466293546731754, 0.23477776706837777, 0.3324291062779458, 0.4327077080103193, 0.06141884653239249, 0.4454217684774466, 0.07101371109704513, 0.06928177047711098, 0.08087750341475597, 0.15836905892384973, 0.31870819428922387, 0.1727741187413801, 0.030208660527103304, 0.06017188331698531, 0.2739635712091708, 0.18918630176668882, 0.42123039681848967, 0.08561007215633637, 0.21198441603181556, 0.048172422179332264, 0.16153427697723016, 0.41070458359140555, 0.0731217825371066, 0.2171931650368621, 0.13219303317089287, 0.19475293150877454, 0.2013428055284378, 0.23687248257788418, 0.09121267304646502, 0.04678819592561867, 0.14672847164193803, 0.3435769264844819, 0.49242020406542814, 0.0409664112790068, 0.36475451227284755, 0.09570676041581277, 0.23890168963808106, 0.20628741644572857, 0.3313512882014375, 0.31582134951414337, 0.2962823493533754, 0.08598334833891602, 0.23681344186737224, 0.17285152387566016, 0.1400732292764877, 0.3236515467581221, 0.4716695133760555, 0.3128417664544814, 0.0850787948504742, 0.1912452786529571, 0.06936794464238927, 0.4204325161542431, 0.35960584872287715, 0.04165655867165108, 0.0486168987725793, 0.26277840449400136, 0.17671586553475233, 0.02751113233356739, 0.1659247697143757, 0.03813989356453079, 0.1974726282923468, 0.49917538295861336, 0.001743278408789517, 0.4729034825381834, 0.31885141054237154, 0.13681615153658466, 0.3973065661402, 0.31507068157757223, 0.41931334880676135, 0.23574979345915775, 0.41995818309220595, 0.44247891104105, 0.24412185388208085, 0.1506196222369861, 0.21215793135643574, 0.4564678389238802, 0.4222802740691941, 0.31482318977858476, 0.33988911336464955, 0.4628959703378222, 0.42966674522435666, 0.21983785344487988, 0.04322069202059753, 0.3643487385988137, 0.4352866691777107, 0.32950162718438475, 0.26424374549907176, 0.25294223217515416, 0.10395002293304423, 0.35108991615448953, 0.002702517971561069, 0.43869003062429457, 0.22986526882049957, 0.4856332192065889, 0.1874860466780231, 0.0026644800125128487, 0.3956899891989233, 0.03199395165380953, 0.4634981593877173, 0.21583224769306647, 0.1792158670640383, 0.4658888700926561, 0.008036984101598421, 0.08553612760670787, 0.2507776880258077, 0.4176733505143218, 0.37322020468723205, 0.2576207240284359, 0.48420929791959083, 0.25505146654247923, 0.3171203114863912, 0.16384530602054342, 0.024495883094568627, 0.05948913785217075, 0.22163276917498625, 0.09175151912267321, 0.018101201827941504, 0.33915977991102236, 0.13416238470279468, 0.3715654909215476, 0.4973797212065931, 0.4547734321466362, 0.2879410944399666, 0.3816661254905886, 0.40499255010778734, 0.29177324232590746, 0.05311443975256813, 0.4153729592894382, 0.09742481867849556, 0.3459547831507878, 0.006594329541183552, 0.08674250460013083, 0.043157734322362584, 0.34466340792092987, 0.08271111420735056, 0.32799913454332125, 0.16650674805300303, 0.10704526491089444, 0.14660874252887035, 0.12915863484711254, 0.43215714171100955, 0.31975146025271006, 0.09853645115930587, 0.4968746557861728, 0.23390281264406504, 0.39917811493586935, 0.04690350884276878, 0.4205732788865237, 0.4814980528532554, 0.061683607796224504, 0.029368471562133958, 0.03075645260373816, 0.15936837603025789, 0.057790953639540954, 0.26371077968430334, 0.24606492675619085, 0.35803285015832964, 0.4786872881841778, 0.2633672000138583, 0.031080552661304495, 0.4073140692753873, 0.12616860022541354, 0.09669042112995979, 0.2631088908103404, 0.1206365114399478, 0.3918690525734456, 0.09295580419383315, 0.21439307261989476, 0.2824540461031053, 0.47604201769732846, 0.09377811715638235, 0.31549574410830733, 0.25376500650400613, 0.05210759184125763, 0.30442467113769767, 0.07407670743568712, 0.03674240996636802, 0.33492505301844, 0.13299753890528648, 0.09487385532565845, 0.49729795194582044, 0.14749712565290685, 0.29447408038016004, 0.47940324830243225, 0.10338808879794209, 0.15151915100138286, 0.08188280892860023, 0.24982817200640695, 0.3809592378304483, 0.07818546564626899, 0.3168367727802198, 0.09617561204557745, 0.007031642483530498, 0.026390758480539234, 0.24100636661154118, 0.1593383661562469, 0.15388613839807447, 0.15686486230372965, 0.2640762698155819, 0.05245067406743381, 0.13918374202244793, 0.25660735028148995, 0.30219399361664234, 0.15375213594422538, 0.4394717980903091, 0.15877873878424448, 0.20955932881127076, 0.22441681293103083, 0.46719885760594976, 0.37353574282748025, 0.4182115848830696, 0.10068901929685592, 0.19647662557300843, 0.460909547006357, 0.36900818594488055, 0.4700526620073861, 0.026792091575969623, 0.15861865094974154, 0.22767152762243908, 0.202323250215742, 0.41135989745454804, 0.24735333058314435, 0.1304242416272311, 0.009571971663267231, 0.10984813935349402, 0.21947129766761503, 0.3493627453416931, 0.28611747716107977, 0.1244149737399104, 0.10127210366968409, 0.028711494070567, 0.2660115833206311, 0.23685166953917214, 0.11187240372218082, 0.16201879452691942, 0.48590678768247986, 0.19103606237232218, 0.3090503813684212, 0.05727406600128959, 0.24012665238158248, 0.09851345228341407, 0.22351243781129188, 0.40269984199289655, 0.1889129507740856, 0.42121105081206883, 0.19851756048846525, 0.44491650124338017, 0.3074840585059377, 0.045458635153576565, 0.18897229030644036, 0.2991825743489055, 0.3060189207794891, 0.37359826228672977, 0.01600298378224263, 0.13553754496479092, 0.20921353050072145, 0.2660770960650142, 0.18172407812899677, 0.08712955573529646, 0.024910769048451742, 0.09167695073412546, 0.0887472350830063, 0.12094161520681679, 0.12984951190462318, 0.42261958446022063, 0.43234804030150953, 0.15004231847567195, 0.4467511388747109, 0.1363325915774986, 0.21709320856499253, 0.05921888824571686, 0.48305858232510895, 0.2646002121564958, 0.05698867670178154, 0.35161944239063003, 0.11411290030671783, 0.2672385175839088, 0.2966396071307707, 0.05432699835769367, 0.0491806990951123, 0.23547958892843107, 0.012256373718315228, 0.2909308216293008, 0.15417300694676672, 0.27257184858826683, 0.0704226750278556, 0.3045027141272991, 0.2136852337397201, 0.4320743842385712, 0.4521756090109451, 0.34745770438203966, 0.23480837399637866, 0.2559891313398752, 0.32629546299344186, 0.47192356245579276, 0.04946362842617169, 0.40174192505144357, 0.1794533705877694, 0.47826395050995213, 0.07282219069224477, 0.1360934022804387, 0.141417696101935, 0.10678364566714005, 0.4987190654098726, 0.3584908025082392, 0.3480905017958233, 0.346312819345008, 0.2557647484932334, 0.09624975987538853, 0.21525867415878042, 0.006095140167895974, 0.1252813960773312, 0.13328212561442493, 0.2336099306603125, 0.27282659643650636, 0.3349754335692699, 0.18462804910238895, 0.33158948175521763, 0.32434770982761907, 0.08132157628264058, 0.4642276077846495, 0.13195944320894387, 0.4301143235063727, 0.0665753701706715, 0.38665410369750897, 0.4399902643522986, 0.01805089992807618, 0.07366164117484764, 0.3395886844277452, 0.3317110206581367, 0.20481733076936126, 0.17063055051229176, 0.23265272401277803, 0.26271381298076035, 0.3543995000686727, 0.1556009342358452, 0.11161580358623224, 0.4763540845891127, 0.3419656599194071, 0.10924408277231956, 0.30802911035263314, 0.32118977230923157, 0.33991863027418834, 0.2911544488825147, 0.23611578428060226, 0.4002949163985162, 0.3209473429169308, 0.06440413369416265, 0.2748935070752928, 0.4919103340314976, 0.4472576002809434, 0.49241085538647034, 0.3868882249844612, 0.4629415691285299, 0.15190369669834353, 0.26879660423252655, 0.21206537938254433, 0.07001455910857651, 0.13293720261180614, 0.3011573239851033, 0.4036165377400697, 0.12891669573889897, 0.2100592526866616, 0.10012512825981462, 0.03536237028641365, 0.41604730830475034, 0.23206862707337933, 0.23005421508532903, 0.4881447590563639, 0.48338527141366605, 0.14490549131704872, 0.4804683052341737, 0.23241872917549955, 0.06605035201016696, 0.47467193480748515, 0.1270490587968336, 0.35637585870267463, 0.0459539963443204, 0.027967186529142596, 0.0718912933438412, 0.007304855206944572, 0.338761143872289, 0.4653000800093371, 0.47049856056709904, 0.21209443335353562, 0.38715161575240653, 0.36051340452709324, 0.18936208885225575, 0.07202876481784698, 0.11249074053916297, 0.40354622695602665, 0.209678302903331, 0.4319303766898639, 0.1654152312489423, 0.0393042294434659, 0.45843873219900505, 0.12154108633890631, 0.4984997638416059, 0.39264015950157855, 0.1187017015731337, 0.2041090320706157, 0.16173891637735693, 0.13429035264891404, 0.4669222946627031, 0.22017775244472515, 0.4820211925607668, 0.25419020284951255, 0.12385779728238011, 0.09241173958119475, 0.43756552781603664, 0.08308267936080826, 0.036696390891559294, 0.338065714232264, 0.2012047288881687, 0.02913742606717601, 0.4523255304916582, 0.11703599959724409, 0.49432734890533575, 0.25473105181126277, 0.09799413388853961, 0.06577800915473775, 0.3927555590954236, 0.40624722840656635, 0.3700397624931954, 0.4839061966452981, 0.15171271753721438, 0.14416821521792106, 0.13866056501003943, 0.19279890750888407, 0.4030843108438292, 0.3442104258462181, 0.1738067469837562, 0.10330186681284359, 0.4459131905776521, 0.04366259381233084, 0.37737515000387856, 0.044819018983372705, 0.3875773005501073, 0.30940960548054125, 0.1120782227427567, 0.4894487181633105, 0.2717968689923859, 0.36034775912167183, 0.4708306191464488, 0.3392786167802858, 0.0721500617130506, 0.054540969704960085, 0.42458839786425623, 0.0805697273162077, 0.10141786500166755, 0.3870669749143307, 0.39830255111485574, 0.1838751050832288, 0.2511103847204543, 0.47521823905423927, 0.2741499051344266, 0.15906048702721692, 0.11591650637814327, 0.2605748995938231, 0.4561711061375577, 0.4502056685288549, 0.08549808524336333, 0.1659842153654278, 0.33905357060436886, 0.2108687501055851, 0.46663330495743544, 0.43394922357979115, 0.0033027675366405496, 0.1030760050909385, 0.025961875228042386, 0.14943033693493712, 0.42183711692953096, 0.3412346496742544, 0.16503276711881715, 0.256675811828815, 0.3986840746012871, 0.13918272777778862, 0.4107586771152846, 0.40411275094201865, 0.4477694801528587, 0.13615151538515624, 0.47681528989634864, 0.4060894966442882, 0.2994039580525578, 0.002356832116035157, 0.006134325920461703, 0.015726588632394345, 0.4194446065480084, 0.33158288839157224, 0.22423675081668687, 0.3683079373660894, 0.4709117207121332, 0.21678482537610727, 0.32914468104453337, 0.13490494103899947, 0.4794409107097097, 0.4276932119114954, 0.44903678053353324, 0.3714692993754132, 0.3694854811566156, 0.4491357548776359, 0.3774813411962376, 0.28521573166425107, 0.11445273898687669, 0.4753206263640075, 0.24573642838841964, 0.31800814657221854, 0.15515312148476967, 0.3484685653285696, 0.08903835788297482, 0.3445759026214782, 0.30480916949187215, 0.0333644641645785, 0.11338887974138484, 0.05516314494175106, 0.08987174568361028, 0.20449623465885197, 0.3881310245730331, 0.34176770127728484, 0.13584691566393114, 0.032867170709950155, 0.274352705168108, 0.437751931865791, 0.4338331641244159, 0.09985346707522669, 0.01336082188870702, 0.04315738487774884, 0.044919727297683454, 0.268011321821034, 0.41251355980881366, 0.018298176399369148, 0.29242644693600567, 0.07122562140252653, 0.1893743043589875, 0.3923707464887694, 0.30474353221752404, 0.20884653420098354, 0.4737529122936724, 0.016013677842789675], 
#         'replicas': [5, 0, 4, 4, 3, 4, 1, 4, 3, 5, 1, 4, 1, 5, 3, 1, 1, 0, 0, 4, 2, 2, 2, 0, 1, 2, 1, 2, 5, 2, 2, 5, 3, 1, 2, 5, 5, 2, 0, 1, 4, 5, 5, 1, 0, 4, 0, 4, 3, 3, 5, 5, 2, 2, 3, 3, 0, 0, 1, 0, 0, 3, 0, 0, 4, 2, 3, 3, 0, 2, 1, 2, 5, 1, 0, 4, 2, 4, 2, 3, 5, 4, 3, 0, 5, 1, 4, 1, 0, 1, 4, 5, 2, 3, 1, 1, 1, 1, 2, 4, 3, 5, 5, 2, 3, 3, 3, 3, 4, 1, 0, 4, 4, 0, 1, 1, 0, 1, 0, 1, 1, 2, 3, 0, 5, 2, 3, 5, 3, 4, 5, 4, 1, 0, 0, 1, 1, 3, 0, 2, 2, 4, 4, 2, 3, 2, 2, 5, 0, 2, 2, 2, 1, 5, 0, 5, 3, 5, 1, 5, 4, 3, 2, 0, 2, 2, 3, 5, 0, 0, 2, 0, 1, 0, 0, 2, 3, 1, 5, 4, 2, 1, 0, 3, 4, 2, 3, 4, 3, 3, 0, 1, 4, 3, 4, 1, 3, 1, 4, 4, 4, 3, 5, 0, 4, 2, 5, 5, 2, 4, 1, 5, 4, 5, 1, 4, 1, 0, 3, 5, 2, 2, 3, 0, 3, 2, 5, 5, 2, 4, 1, 0, 5, 2, 5, 4, 2, 1, 0, 5, 1, 5, 0, 1, 1, 5, 3, 4, 5, 1, 2, 1, 3, 1, 1, 1, 2, 0, 2, 0, 1, 5, 2, 0, 2, 1, 0, 1, 0, 4, 0, 3, 0, 3, 1, 4, 5, 2, 4, 2, 5, 2, 0, 4, 3, 4, 4, 0, 2, 5, 0, 5, 3, 4, 1, 4, 1, 5, 4, 2, 1, 3, 4, 3, 1, 3, 3, 0, 2, 4, 2, 5, 5, 5, 3, 1, 0, 5, 1, 0, 5, 4, 2, 5, 3, 3, 2, 2, 4, 2, 3, 5, 3, 1, 3, 1, 2, 2, 5, 5, 1, 4, 1, 3, 1, 1, 2, 5, 4, 1, 4, 0, 2, 3, 2, 5, 5, 5, 2, 4, 5, 3, 2, 0, 1, 1, 4, 5, 0, 4, 5, 1, 5, 1, 2, 5, 2, 2, 4, 2, 5, 2, 2, 2, 4, 0, 0, 4, 2, 5, 4, 0, 4, 0, 0, 2, 2, 3, 5, 2, 1, 2, 4, 2, 4, 2, 0, 3, 4, 2, 3, 0, 2, 4, 2, 5, 1, 2, 4, 4, 0, 4, 4, 2, 0, 3, 1, 4, 1, 3, 0, 3, 1, 5, 3, 2, 1, 4, 4, 0, 2, 0, 5, 3, 1, 4, 1, 4, 0, 4, 5, 0, 0, 4, 3, 1, 1, 3, 3, 0, 0, 5, 1, 1, 1, 4, 5, 5, 2, 0, 3, 5, 5, 4, 1, 1, 5, 3, 1, 2, 0, 5, 3, 2, 4, 3, 4, 1, 3, 1, 1, 3, 4, 2, 4, 5, 0, 0, 4, 3, 3, 5, 0, 1, 2, 4, 2, 1, 1, 5, 0, 1, 5, 5, 5, 2, 5, 4, 3, 0, 3, 1, 1, 5, 0, 1, 3, 1, 2, 1, 2, 5, 0, 4, 3, 0, 3, 0, 3, 4, 4, 4, 0, 4, 1, 0, 1, 4, 1, 2, 1, 5, 3, 4, 3, 2, 4, 5, 3, 3, 4, 1, 1, 1, 1, 2, 2, 1, 4, 5, 5, 3, 5, 5, 2, 5, 3, 3, 3, 0, 4, 5, 2, 0, 0, 4, 3, 0, 1, 5, 5, 4, 0, 4, 5, 2, 1, 5, 3, 3]
#     }

#     cost0 = compute_costs(init_popu)
#     init_popu1 = copy.deepcopy(init_popu)
#     s0 = 'Start: \ninit_popu = {}  \naddtion = {} \nThe initial cost = {}'.format(init_popu, addtion0, cost0)
   
#     simple, used_time0 = new_FFDSum_simple(init_popu, addtion0)
#     comple, used_time1 = FFDSum_complex(init_popu1, addtion0)
#     cost_simple = compute_costs(simple)
#     cost_complex = compute_costs(comple)

#     s1 = '\n\n\nEnd:   \nBins_simple = {} \nThe cost_simple of new state = {}'.format(init_popu, cost_simple)    
#     s2 = '\n\n\nEnd:   \nBins_complex = {} \nThe cost_comlex of new state = {}'.format(init_popu1, cost_complex)    
#     # print s0,'\n' ,s1,'\n',s2

#     with open('addtion_phase//Result_Contrast.py','a') as f:
#         f.flush()
#         f.write(s0)
#         f.write(s1)
#         f.write(s2)

