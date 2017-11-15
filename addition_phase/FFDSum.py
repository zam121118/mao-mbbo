#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-15
@Author : Amy
Goal: 定义FFD-based Herustics常见方法FFDSum即通过将多维demand、capacites向量转化为意义明确的标量(volume of the vector)，
      以标量值大小为bins、objects的排序标准，再依据资源约束，循环求解vector bin pack结果。
      weight ：the ratio between the total demand for resource i and the capacity of the host
      FFDSum 以 sum(w_i*v_i) 对所有纬度值乘以weight再求和；
      此次对比中，采用swarm binpack strategy —— scores 作为排序标准，见weighted_node.go
'''


import time
import random
import math
import json
import sys
from copy import deepcopy


def FFDSum(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    '''

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM打分，分最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM打分，分最高者放入

    for i in objects['replicas']:
        object_CPU, object_MEM = objects['c_rp'], objects['c_rm']
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = weightedVMBins(bins, object_CPU, object_MEM) 

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)
                hm_suffix = bins['map_v_h'][vm_suffix]

                # 更改放入VM后的资源变化
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
                # 随机生成一个足以容纳该容器的VM
                vm = create_VM(object_CPU, object_MEM, rp_option, rm_option)

                # 为该VM（object）寻找HM（bin),先计算各HM得分
                weightedHMBins = weightedHMBins(bins, vm['rp'], vm['rm'])
                
                # 获取得分最高的HM编号/新加入的HM编号
                if len(weightedHMBins) > 0:
                    hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
                    vm_suffix = len(bins['v_p_cost'][0])
                else:
                    hm_suffix = len(bins['h_m_cost'][0])
                    vm_suffix = len(bins['v_p_cost'][0])

                # 更新分别放入容器、VM后的资源变化
                bins['c_rp'].append(object_CPU)
                bins['c_rm'].append(object_MEM)
                bins['v_rp'].append(vm['rp'])
                bins['v_rm'].append(vm['rm'])
                bins['v_p_cost'][0][vm_suffix] += object_CPU 
                bins['v_m_cost'][0][vm_suffix] += object_MEM
                bins['h_p_cost'][0][hm_suffix] += vm['rp'] 
                bins['h_m_cost'][0][hm_suffix] += vm['rm']


                # 更新‘population’、‘map_v_h’
                bins['population'][0].append([vm_suffix, hm_suffix])
                bins['map_v_h'][vm_suffix] = hm_suffix

                # 已经解决掉一个object
                i -= 1
                continue

                # 至少有HM能够容纳该新VM时，放入并修改参数
                # if len(weightedHMBins) > 0:
                #     # 获取得分最高HM编号
                #     hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
                #     vm_suffix = len(bins['v_p_cost'][0])

                #     # 更新分别放入容器、VM后的资源变化
                #     bins['c_rp'].append(object_CPU)
                #     bins['c_rm'].append(object_MEM)
                #     bins['v_rp'].append(vm['rp'])
                #     bins['v_rm'].append(vm['rm'])
                #     bins['v_p_cost'][0][vm_suffix] += object_CPU 
                #     bins['v_m_cost'][0][vm_suffix] += object_MEM
                #     bins['h_p_cost'][0][hm_suffix] += vm['rp'] 
                #     bins['h_m_cost'][0][hm_suffix] += vm['rm']


                #     # 更新‘population’、‘map_v_h’
                #     bins['population'][0].append([vm_suffix, hm_suffix])
                #     bins['map_v_h'][vm_suffix] = hm_suffix

                #     # 已经解决掉一个object
                #     i -= 1
                #     continue

                # # 当前所有HM均无法容纳新的VM
                # else:
                #     # 添加新的HM，更新所有资源
                #     hm_suffix = len(bins['h_m_cost'][0])
                #     vm_suffix = len(bins['v_p_cost'][0])

                #     # 更新分别放入容器、VM后的资源变化
                #     bins['c_rp'].append(object_CPU)
                #     bins['c_rm'].append(object_MEM)
                #     bins['v_rp'].append(vm['rp'])
                #     bins['v_rm'].append(vm['rm'])
                #     bins['v_p_cost'][0][vm_suffix] += object_CPU 
                #     bins['v_m_cost'][0][vm_suffix] += object_MEM
                #     bins['h_p_cost'][0][hm_suffix] += vm['rp'] 
                #     bins['h_m_cost'][0][hm_suffix] += vm['rm']

                #     # 更新‘population’、‘map_v_h’
                #     bins['population'][0].append([vm_suffix, hm_suffix])
                #     bins['map_v_h'][vm_suffix] = hm_suffix

                #     # 已经解决掉一个object
                #     i -= 1
                #     continue


    num = set(bins['map_v_h'].values())
    print "used the number of HMs is {}".format(len(num))
    return bins



               


def weightedVMBins(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    weightedVMBins = {}
    for j in xrange(len(bins['v_p_cost'][0])):
        bin_reservedCPU = bins['v_rp'][j] - bins['v_p_cost'][0][j]
        bin_reservedMEM = bins['v_rm'][j] - bins['v_m_cost'][0][j]
        if bin_reservedCPU < object_CPU || bin_reservedMEM < object_MEM:
                continue
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
                cpuScore = (bins['v_p_cost'][0][j] + object_CPU) * 100 / bins['v_rp'][j]
        if object_MEM > 0:
                memScore = (bins['v_m_cost'][0][j] + object_MEM) * 100 / bins['v_rm'][j]
        if cpuScore <= 100 && memoryScore <= 100:
                weightedVMBins.setdefault(j, cpuScore+memScore)
    return weightedVMBins


def weightedHMBins(bins, object_CPU, object_MEM):
    '''
    计算集群bins(HMs)中所有bin的权重，并返回weightedHMBins记录有各个node(HM)得分的weightedHMBins
    '''
    weightedHMBins = {}
    for j in xrange(len(bins['h_p_cost'][0])):
        bin_reservedCPU = 1.0 - bins['h_p_cost'][0][j]
        bin_reservedMEM = 1.0 - bins['h_m_cost'][0][j]
        if bin_reservedCPU < object_CPU || bin_reservedMEM < object_MEM:
                continue
        cpuScore = 100
        memScore = 100
        if object_CPU > 0:
                cpuScore = (bins['h_p_cost'][0][j] + object_CPU) * 100 / 1.0
        if object_MEM > 0:
                memScore = (bins['h_m_cost'][0][j] + object_MEM) * 100 / 1.0
        if cpuScore <= 100 && memoryScore <= 100:
                weightedHMBins.setdefault(j, cpuScore+memScore)
    return weightedHMBins


def create_VM(c_rp, c_rm, rp_option, rm_option):
    '''
    依据实验可选的VM尺寸(rp_option、rm_option)随机生成可以容纳(c_rp、c_rm)的VM
    '''
    vm = {'rp':0, 'rm':0}
    while vm['rp'] == 0:
        rp = random.choice(rp_option)
        rm = random.choice(rm_option)
        if rp >= c_rp and rm >= c_rm:
            vm['rp'],vm['rm'] = rp,rm
    return vm