#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-12-17
@Author : Amy
Goal : 分别以docker/VM，docker/HM作为资源利用率排序准则，对比同时使用FFDSum时的最终结果，并存于Result_Contrast.py
Digest : 分别定义2种FFDSum算法：
      一种在新容器到来时，模拟openstack向swarm提供当前VMs尺寸，由swarm自行选择放入，若无新的VM，则由openstack新建，并返回（v,h）给容器层；
      另一种则由swarm进行全局资源的管控，以docker作为真正的负载，首先针对各个HM打分再以其上各个VM打分，若要新建VM则以打分放入；
2017-12-20 更新: 使用多线程multiprocessing中多进行与共享变量的方式Gen次重复实验取均值
'''


import time
import random
import math
import copy
import collections
import datetime
import multiprocessing
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
    # print "Complex used time is {} \n used the number of HMs is {}".format(used_time, len(num))
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
    # print "Simple used time is {} \n used the number of HMs is {}".format(used_time, len(num))
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
        cost['degree_of_concentration'] = 100 * cost['used_hms'] - 13 * utilization

        # 计算VM迁移时间（仅聚合阶段）
        pass

    # # print 'true cost={}'.format(cost)
    # return cost
    return cost['used_hms'], cost['degree_of_concentration']

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

def main_controller(function_str, bins, addtion0, func_handler, return_dict):
    '''
    2017-12-20 23:00 使用多进程共享变量与多进程实现4种方式并行计算
    function_str用于标识哪个方法,0=FFDSum_simple 1=FFDSum_complex 2=safe_FFDSum_simple 3=safe_FFDSum_complex
    使用函数句柄实现不同方法的串行计算逻辑
    '''
    # 初始放置方案的计算
    after_bins, used_time = func_handler(bins, addtion0)
    # 该方案的目标优化结果
    used_hm, utilization = compute_costs(after_bins)
    return_dict[function_str] = [used_hm, utilization]
    return return_dict


if __name__ == '__main__':
    '''
    对于Docker+VM与Docker+VM+HM架构下，不同排序策略的BFD下，重复Gen次取各项指标均值的对比
    '''
    # 多进程初始化
    # p = multiprocessing.Pool()
    manager = multiprocessing.Manager()
    jobs = []

    # 重复次数
    Gen = 3
       
    # 1. 用于生成json的数据
    data = {
        'scale':[],
        'simple':[],
        'complex':[],
        'safe_simple':[],
        'safe_complex':[]
    }

    # 2. 产生新初始集群与新增容器的服务数量
    init_popu0 = main_init(50, 1.0)
    init_popu1 = copy.deepcopy(init_popu0)
    init_popu2 = copy.deepcopy(init_popu1)
    init_popu3 = copy.deepcopy(init_popu2)

    cycle = []
    for i in xrange(1, 3):
        a = 10 ** i
        ll = sorted(random.sample(range(1,10), 4))
        for j in ll:
            cycle.append(j*a)

    # 3. 模拟多批量新增场景
    for scale in cycle:
        avg_scale = 0
        avg_simple = [0, 0]
        avg_complex = [0, 0]
        avg_safe_simple = [0, 0]
        avg_safe_complex = [0, 0]

        # 运行10次，取效果最好者
        for gen in xrange(Gen):
            # 记录初始集群信息并深度拷贝多副本用于算法间对比
            addtion0 = create_addtion(1.0, scale)
            avg_scale += len(init_popu0['c_rp']) + sum(addtion0['replicas'])
            cost0 = compute_costs(init_popu0)

            # 对初始集群的多副本进行不同放置决策并计算优化模型结果
            #[x.get() for x in [pool.apply_async(pool_test, (x,)) for x in gen_list(l)]]
            return_dict = manager.dict()
            p = multiprocessing.Process(target=main_controller, args=(0, init_popu0, addtion0, FFDSum_simple, return_dict))
            jobs.append(p)
            p.start()
            p = multiprocessing.Process(target=main_controller, args=(1, init_popu1, addtion0, FFDSum_complex, return_dict))
            jobs.append(p)
            p.start()

            # print p.map(main_controller, (init_popu0, init_popu1), (addtion0, addtion0), (FFDSum_simple, FFDSum_complex))

            for proc in jobs:
                proc.join()
            # print return_dict.values()
            avg_simple[0] += return_dict[0][0]
            avg_simple[1] += return_dict[0][1]
            avg_complex[0] += return_dict[1][0]
            avg_complex[1] += return_dict[1][1]
            avg_safe_simple = 0
            avg_safe_complex = 0
        # 计算迭代gen代的平均值,并写入文件
        avg_scale /= Gen
        avg_simple[0] /= Gen
        avg_complex[0] /= Gen
        avg_simple[1] /= Gen
        avg_complex[1] /= Gen
        data = createJSON(data, avg_scale, avg_simple, avg_complex, avg_safe_simple, avg_safe_complex)
    # # 4. 记录data用于前端数据可视化
    with open('.//viz//contrast-addtion-{}-demo.json'.format(datetime.datetime.now()),'w') as f:
        f.flush()
        json.dump(data, f, indent=2)
