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
2017-12-22 更新：
      1. 聚合阶段适用于集群在用户增增减减之后，集群到处资源碎片化需要聚合，所以直接使用init.main_init()模拟这种碎片化场景。
      2. 不能直接init.main_init()之后持续增加addtion0是因为这个过程没有用户删除容器，而新增本就以减小碎片化为目标，实际已经是在实时聚合了，故不可在这个基础上跑聚合算法，会异常甚至没有之前效果好。
      3. v-h的聚合与d-v-h的聚合对比，说明加入d-v的聚合效果更好： 
                   （1）直接用init.main_init模拟碎片化集群，
                   （2）再抽取集群中运行态虚拟机的rp,rm,v_p_cost,v_m_cost使得vm_mbbo算法作为集群状态记录；
                    (3) 让vm_mbbo按照其设计的，以VM创建资源量进行各项代价预估给出最终精英解， 但是我们要对精英解按照docker为实际负载，求解集群真正的各项指标。
                    (4) 采用2层的FFDSum_consol进行聚合与3层的FFDSum聚合；2层的vm_mbbo与3层的doc_mbbo聚合；2层的vm_mbbo与3层FFDSum_consol对比。
'''


import time
import random
import math
import copy
import collections
import datetime
import json
import Contrast
import init
import vm_mbbo
import tolerance



# rp_option = [0.5]                      # vm可选的cpu尺寸
# rm_option = [0.5]                      # vm可选的mem尺寸
vm_option = [(0.3, 0.3), (0.5, 0.4), (0.6, 0.5), (0.8, 0.7), (1.0, 0.8), (1.0, 1.0)]
               
def docker2service(scale):
    '''
    return map_d_s, map_s_d
    (此算法为一次性独立的，即每main_init一次就使用一次本算法)
    对在init.main_init()中生成的随机集群中scale数量的容器，随机产生所对应的serive映射，用于独立性检测
    '''
    map_d_s = {}
    suffix = -1  # 记录上次安排完所属服务的容器
    count = 0   # 记录服务下标
    flag = scale
    while flag > 0:
        # 模拟生成需要随机数量replicas支持的服务
        x = random.randint(3, 5)
        for i in xrange(x):
            if len(map_d_s) < scale :
                map_d_s[i+suffix+1] = count
        flag -= x
        count += 1
        if x != 0:
            suffix = len(map_d_s) - 1
    map_s_d = collections.defaultdict(list)
    for key, value in map_d_s.items():
        map_s_d[value].append(key)
    return map_d_s, map_s_d

def FFDSum_3_Consol(bins):
    '''
    @param: bins 代表当前系统状态
    @return: 不考虑容错的 聚合容器后的集群bins状态
    docker-vm聚合会考虑到hm的资源占用，再独立聚合vm-hm
    '''
    # print " \n进入3层 FFDSum_Consol() 聚合方法" 
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
                    break
            # 放置出现意外而需要创建新VM时
            else:
                flag = Contrast.find_HM_complex(bins, object_CPU, object_MEM, vm_option)
                
                # 代表active HMs中有HM可以容纳能够放入该容器的最小VM
                if flag:
                    hm_suffix, min_vm = flag
                    vm_suffix = len(bins['v_p_cost'][0])

                    # 更新放入容器后造成的VM、HM资源变化
                    bins['v_p_cost'][0].append(object_CPU)
                    bins['v_m_cost'][0].append(object_MEM)

                    # 更新‘population’、‘map_v_h’
                    bins['population'][0][x] = [vm_suffix, -1]
                    bins['map_v_h'][vm_suffix] = hm_suffix

                    # 已经解决掉一个object
                    break
    
    # 循环为安排完所有容器的VMs聚合安排HMs
    # 选择所有v_p/m_cost均非0的VMs作为需要重新安排放入的objects（running_vms）
    running_vms = []
    for i in xrange(len(bins['v_p_cost'][0])):
        # 重新统计聚合容器后真正承载容器的VMs
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
            if len(weightedHMBins) > 0:
                # 获取得分最多bins的编号
                hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
                # 记录为该VM选择的HM
                bins['map_v_h'][x] = hm_suffix

                # 更新放入该object（vm）造成的bin（HM）资源变化
                bins['h_p_cost'][0][hm_suffix] += object_CPU
                bins['h_m_cost'][0][hm_suffix] += object_MEM
                break
            else:
                # 创建最大VM          
                hm_suffix = len(bins['h_m_cost'][0])

                # 更新放入容器后造成的VM、HM资源变化
                bins['h_p_cost'][0].append(object_CPU)
                bins['h_m_cost'][0].append(object_MEM)

                # 更新‘population’、‘map_v_h’
                bins['map_v_h'][x] = hm_suffix
                break

    # 整体安排完毕后更新population
    for i in xrange(len(bins['population'][0])):
        v, h = bins['population'][0][i]
        if h == -1:
            bins['population'][0][i] = [v, bins['map_v_h'][v]]

    # 说明性数据统计
    used_hms = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "3层 FFDSum coslidation 聚合used time is {} \n used the number of HMs is {}".format(used_time, len(used_hms))
    return bins

def FFDSum_2_Consol(bins):
    '''
    @param: bins 代表当前系统状态
    @return: 聚合容器后的集群bins状态
    仅进行vm-hm的聚合
    '''
    # print " \n进入2层 FFDSum_Consol() 聚合方法" 
    time0 = time.time()

    # d-v-h架构下的vm-hm两层聚合，会直接忽略掉容器的存在：
    # 1. 直接拿到当前active HMs的分布，并清空这些vm与hm的映射以及造成的资源约束map_v_h与h_p/m_cost;
    # 2. 在当前active的HMs上重新按照进行排序再BFD放入，并更新map_v_h与容器的population；
    #    此处HMs选取的打分设计，可分为2种：仅考虑能耗、能耗+负载指数。

    # 集群所有active vms为需要重新安排放入的objects，清空h_p/m_cost、map_v_h
    running_vms = bins['map_v_h'].keys()
    running_hms = list(set(bins['map_v_h'].values()))
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
            if len(weightedHMBins) > 0:
                # 获取得分最多bins的编号
                hm_suffix = max(weightedHMBins, key=weightedHMBins.get)
                # 记录为该VM选择的HM
                bins['map_v_h'][x] = hm_suffix
                # 更新放入该object（vm）造成的bin（HM）资源变化
                bins['h_p_cost'][0][hm_suffix] += object_CPU
                bins['h_m_cost'][0][hm_suffix] += object_MEM
                break
            else:
                # 创建最大VM          
                hm_suffix = len(bins['h_m_cost'][0])

                # 更新放入容器后造成的VM、HM资源变化
                bins['h_p_cost'][0].append(object_CPU)
                bins['h_m_cost'][0].append(object_MEM)

                # 更新‘population’、‘map_v_h’
                bins['map_v_h'][x] = hm_suffix
                break

    # 整体安排完毕后更新容器的population
    for i in xrange(len(bins['population'][0])):
        v, h = bins['population'][0][i]
        h = bins['map_v_h'][v]
        bins['population'][0][i] = [v, h]

    # 说明性数据统计
    used_hms = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "2层 FFDSum coslidation 聚合 used time is {} \n used the number of HMs is {}".format(used_time, len(used_hms))
    return bins

def safe_FFDSum_3_Consol(bins, map_d_s, map_s_d):
    '''
    @param: bins 代表当前系统状态
    @return: 支持HM级聚合容器后的集群bins状态
    docker-vm聚合会考虑到hm的资源占用，再独立聚合vm-hm
    '''
    # print " \n进入3层HM级容错 FFDSum_Consol() 聚合方法" 
    time0 = time.time()

    # d-v-h架构下支持HM级容错的聚合算法大致如此：
    # 1. 先进行d-v层聚合（以减少active VMs为主，同时尽量使各HM使用率最高）即排序时同时考虑hm、vm使用率；
    # 2. 对于重新统计的active VMs进行v-h的聚合（以降低能耗为目标）；
    # 3. 检测各服务实际replicas的独立性，逐一对各服务replicas进行重新调整，有可能会重新启用本可以关闭的vm、hm。

    # 调用FFDSum_3_Consol()方法进行聚合
    bins = FFDSum_3_Consol(bins)
    
    # 进行独立性检测与修复
    bins = detect_hm_independce(bins, map_d_s, map_s_d)

    # 说明性数据统计
    used_hms = set(bins['map_v_h'].values())
    used_time = time.time() - time0
    print "支持HM级别容错的 3层 FFDSum coslidation 聚合used time is {} \n used the number of HMs is {}".format(used_time, len(used_hms))
    return bins

def detect_hm_independce(bins, map_d_s, map_s_d):
    '''
    对传入的集群状态bins进行以HM为独立性基础的检测与修复
    @para: map_d_s 记录集群中所有docker-service映射；map_s_d 记录集群正在运行的service-docker映射。
    @func: 在bins中通过map_s_d检测各服务所有replicas实际所在HMs，对于all replicas same HM情况，
            则至少变换一个replica使其与集群中最大下标HM上某容器交换位置，直至检查完所有的service并返回修复独立性之后的bins
    '''
    # 遍历所有容器service
    for service, dockers in map_s_d.items():
        # 各服务所需容器配置及replicas数量
        object_CPU, object_MEM, nums = bins['c_rp'][dockers[0]], bins['c_rm'][dockers[0]], len(dockers)
        # 若该服务replica为1，即单节点独立;
        if nums == 1:
            continue
        # 该服务所有replicas对应HM下标,及这些HMs多样性
        d_hms = [bins['population'][0][j][-1] for j in dockers]
        num_hms = len(set(d_hms))
        # 若满足独立性，则进行下一个服务检测（实际在说明的时候是要对所欲replicas都进行独立放置）
        if num_hms != 1:
            continue

        # 对服务的所有容器都进行调整，使得都分布在不同HM上
        while nums > 1:
            # 不满足独立性需要进行修复
            flag = False
            # 对该服务的第一个支撑replica从active HMs最大下标者开始依次往前，寻找可与该容器对调换位置的容器
            origin_docker_suffix = dockers[nums - 1]
            used_hms = list(set(bins['map_v_h'].values()))
            used_hms.remove(d_hms[0])
            origin_vm_suffix = bins['population'][0][origin_docker_suffix][0]
            for hm in sorted(used_hms, reverse=True):
                dockers_onHM, vms = find_docker_onHM(bins, hm, 0)
                # 依次寻找其他HM上可与该服务第一个replica对掉而满足双方资源约束的解
                for i in xrange(len(dockers_onHM)):
                    vm_suffix = vms[i]
                    docker_suffix = dockers_onHM[i]
                    # 换出原docker换入replica之后的资源
                    reversed_cpu1 = bins['v_rp'][vm_suffix] - (bins['v_p_cost'][0][vm_suffix] - bins['c_rp'][docker_suffix] + object_CPU)
                    reversed_mem1 = bins['v_rm'][vm_suffix] - (bins['v_m_cost'][0][vm_suffix] - bins['c_rm'][docker_suffix] + object_MEM)
                    # 换入新容器换出replica后的资源
                    reversed_cpu0 = bins['v_rp'][origin_vm_suffix] - (bins['v_p_cost'][0][origin_vm_suffix] + bins['c_rp'][docker_suffix] - object_CPU)
                    reversed_mem0 = bins['v_rm'][origin_vm_suffix] - (bins['v_m_cost'][0][origin_vm_suffix] + bins['c_rm'][docker_suffix] - object_MEM)
                    # 若对换后满足资源约束，则更新集群
                    if reversed_cpu0 >= 0 and reversed_cpu1 >= 0 and reversed_mem0 >= 0 and reversed_mem1 >=0:
                        bins['v_p_cost'][0][vm_suffix] += (object_CPU - bins['c_rp'][docker_suffix])
                        bins['v_m_cost'][0][vm_suffix] += (object_MEM - bins['c_rm'][docker_suffix])
                        bins['v_p_cost'][0][origin_vm_suffix] += (bins['c_rp'][docker_suffix] - object_CPU)
                        bins['v_m_cost'][0][origin_vm_suffix] += (bins['c_rm'][docker_suffix] - object_MEM)
                        bins['population'][0][origin_docker_suffix] = [vm_suffix, hm]
                        bins['population'][0][docker_suffix] = [origin_vm_suffix, d_hms[nums - 1]]
                        # map_v_h由于是对掉并不会产生新的拓扑变化，故不用更新
                        flag = True
                        nums -= 1
                        break
                    # 或者是否有active VM能够容纳该容器
                    reversed_cpu2 = bins['v_rp'][vm_suffix] - (bins['v_p_cost'][0][vm_suffix] + object_CPU)
                    reversed_mem2 = bins['v_rm'][vm_suffix] - (bins['v_m_cost'][0][vm_suffix] + object_MEM)
                    if reversed_cpu2 >= 0 and reversed_cpu2 >= 0:
                        bins['v_p_cost'][0][vm_suffix] += object_CPU
                        bins['v_m_cost'][0][vm_suffix] += object_MEM
                        bins['v_p_cost'][0][origin_vm_suffix] -= object_CPU
                        bins['v_m_cost'][0][origin_vm_suffix] -= object_MEM
                        bins['population'][0][origin_docker_suffix] = [vm_suffix, hm]
                        flag = True
                        nums -= 1
                        break
                # 若在该hm上对换而修复，则推出本次service修复，进入下一个
                if flag:
                    # 否则继续寻找下一个hm
                    break
            
            # 若所有active HMs均无发用于修复独立性,则新建HM与VM
            if not flag:
                second_flag = Contrast.find_HM_complex(bins, object_CPU, object_MEM, vm_option)
                
                # 代表active HMs中有HM可以容纳能够放入该容器的最小VM
                if second_flag:
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
                    flag = True
                    nums -= 1
                    break

                # 若所有active HMs均不满足，则新建HM并新建VM，（所建VM规格先不加以控制）
                if not second_flag:
                    # 创建最大VM
                    vm = Contrast.create_VM_random(object_CPU, object_MEM,vm_option)
                    vm_suffix = len(bins['v_p_cost'][0])
                    hm_suffix = len(bins['h_m_cost'][0])

                    # 更新放入容器后造成的VM、HM资源变化
                    bins['v_p_cost'][0].append(object_CPU)
                    bins['v_m_cost'][0].append(object_MEM)
                    bins['h_p_cost'][0].append(vm['rp'])
                    bins['h_m_cost'][0].append(vm['rm'])

                    # 追加系统容器、vm数量及资源分布
                    bins['v_rp'].append(vm['rp'])
                    bins['v_rm'].append(vm['rm'])

                    # 更新‘population’、‘map_v_h’
                    bins['population'][0][origin_docker_suffix] = [vm_suffix, hm_suffix]
                    bins['map_v_h'][vm_suffix] = hm_suffix
                    flag = True
                    nums -= 1
                    break
    return bins

def deprated_detect_hm_independce(bins, map_d_s, map_s_d):
    '''
    对传入的集群状态bins进行以HM为独立性基础的检测与修复
    @para: map_d_s 记录集群中所有docker-service映射；map_s_d 记录集群正在运行的service-docker映射。
    @func: 在bins中通过map_s_d检测各服务所有replicas实际所在HMs，对于all replicas same HM情况，
            则至少变换一个replica使其与集群中最大下标HM上某容器交换位置，直至检查完所有的service并返回修复独立性之后的bins
    '''
    # 遍历所有容器service
    for service, dockers in map_s_d.items():
        # 各服务所需容器配置及replicas数量
        object_CPU, object_MEM, i = bins['c_rp'][dockers[0]], bins['c_rm'][dockers[0]], len(dockers)
        # 若该服务replica为1，即单节点独立;
        if i == 1:
            continue
        # 该服务所有replicas对应HM下标,及这些HMs多样性
        d_hms = [bins['population'][0][j][-1] for j in dockers]
        num_hms = len(set(d_hms))
        # 若满足独立性，则进行下一个服务检测（实际在说明的时候是要对所欲replicas都进行独立放置）
        if num_hms != 1:
            continue

        # 不满足独立性需要进行修复
        flag = False
        # 对该服务的第一个支撑replica从active HMs最大下标者开始依次往前，寻找可与该容器对调换位置的容器
        origin_docker_suffix = dockers[0]
        used_hms = list(set(bins['map_v_h'].values()))
        used_hms.remove(d_hms[0])
        origin_vm_suffix = bins['population'][0][origin_docker_suffix][0]
        for hm in sorted(used_hms, reverse=True):
            dockers_onHM, vms = find_docker_onHM(bins, hm, 0)
            # 依次寻找其他HM上可与该服务第一个replica对掉而满足双方资源约束的解
            for i in xrange(len(dockers_onHM)):
                vm_suffix = vms[i]
                docker_suffix = dockers_onHM[i]
                # 换出原docker换入replica之后的资源
                reversed_cpu1 = bins['v_rp'][vm_suffix] - (bins['v_p_cost'][0][vm_suffix] - bins['c_rp'][docker_suffix] + object_CPU)
                reversed_mem1 = bins['v_rm'][vm_suffix] - (bins['v_m_cost'][0][vm_suffix] - bins['c_rm'][docker_suffix] + object_MEM)
                # 换入新容器换出replica后的资源
                reversed_cpu0 = bins['v_rp'][origin_vm_suffix] - (bins['v_p_cost'][0][origin_vm_suffix] + bins['c_rp'][docker_suffix] - object_CPU)
                reversed_mem0 = bins['v_rm'][origin_vm_suffix] - (bins['v_m_cost'][0][origin_vm_suffix] + bins['c_rm'][docker_suffix] - object_MEM)
                # 若对换后满足资源约束，则更新集群
                if reversed_cpu0 >= 0 and reversed_cpu1 >= 0 and reversed_mem0 >= 0 and reversed_mem1 >=0:
                    bins['v_p_cost'][0][vm_suffix] += (object_CPU - bins['c_rp'][docker_suffix])
                    bins['v_m_cost'][0][vm_suffix] += (object_MEM - bins['c_rm'][docker_suffix])
                    bins['v_p_cost'][0][origin_vm_suffix] += (bins['c_rp'][docker_suffix] - object_CPU)
                    bins['v_m_cost'][0][origin_vm_suffix] += (bins['c_rm'][docker_suffix] - object_MEM)
                    bins['population'][0][origin_docker_suffix] = [vm_suffix, hm]
                    bins['population'][0][docker_suffix] = [origin_vm_suffix, d_hms[0]]
                    # map_v_h由于是对掉并不会产生新的拓扑变化，故不用更新
                    flag = True
                    break
                # 或者是否有active VM能够容纳该容器
                reversed_cpu2 = bins['v_rp'][vm_suffix] - (bins['v_p_cost'][0][vm_suffix] + object_CPU)
                reversed_mem2 = bins['v_rm'][vm_suffix] - (bins['v_m_cost'][0][vm_suffix] + object_MEM)
                if reversed_cpu2 >= 0 and reversed_cpu2 >= 0:
                    bins['v_p_cost'][0][vm_suffix] += object_CPU
                    bins['v_m_cost'][0][vm_suffix] += object_MEM
                    bins['v_p_cost'][0][origin_vm_suffix] -= object_CPU
                    bins['v_m_cost'][0][origin_vm_suffix] -= object_MEM
                    bins['population'][0][origin_docker_suffix] = [vm_suffix, hm]
                    flag = True
                    break
            # 若在该hm上对换而修复，则推出本次service修复，进入下一个
            if flag:
                # 否则继续寻找下一个hm
                break
        
        # 若所有active HMs均无发用于修复独立性,则新建HM与VM
        if not flag:
            second_flag = Contrast.find_HM_complex(bins, object_CPU, object_MEM, vm_option)
            
            # 代表active HMs中有HM可以容纳能够放入该容器的最小VM
            if second_flag:
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
                flag = True
                break

            # 若所有active HMs均不满足，则新建HM并新建VM，（所建VM规格先不加以控制）
            if not second_flag:
                # 创建最大VM
                vm = Contrast.create_VM_random(object_CPU, object_MEM,vm_option)
                vm_suffix = len(bins['v_p_cost'][0])
                hm_suffix = len(bins['h_m_cost'][0])

                # 更新放入容器后造成的VM、HM资源变化
                bins['v_p_cost'][0].append(object_CPU)
                bins['v_m_cost'][0].append(object_MEM)
                bins['h_p_cost'][0].append(vm['rp'])
                bins['h_m_cost'][0].append(vm['rm'])

                # 追加系统容器、vm数量及资源分布
                bins['v_rp'].append(vm['rp'])
                bins['v_rm'].append(vm['rm'])

                # 更新‘population’、‘map_v_h’
                bins['population'][0][origin_docker_suffix] = [vm_suffix, hm_suffix]
                bins['map_v_h'][vm_suffix] = hm_suffix
                flag = True
                break
    return bins

def find_docker_onHM(bins, vhm, label):
    '''
    2017-12-21 更新:  通过label表明传入的时hm下标还是vm下标
    即控制label=0,说明查找某hm上所有docker与vm 2个list
      控制label=1, 说明查找某vm上的所有docker
    给定集群以及active HM下标，返回该HM上承载的所有容器下标及vm下标
    '''
    dockers_onHM, vms_onHM, dockers_onVM = [], [], []
    for i in xrange(len(bins['c_rp'])):
        v, h = bins['population'][0][i]
        if label == 0:
            if  h == vhm:
                dockers_onHM.append(i)
                vms_onHM.append(v)
        elif label == 1:
            if v == vhm:
                dockers_onVM.append(i)
    if label == 0:
        return (dockers_onHM, vms_onHM)
    elif label == 1:
        return dockers_onVM

def weightVMBins_FFDSum(bins, running_vms, object_CPU, object_MEM):
    '''
    以最大化使用VM资源为目标，以docker作为实际负载考虑，引入基于打分机制的FFDSum算法，
    对各个VM计算放入object引起的资源占比与hosted HM引起的资源占比之和。
    CPU得分sum(reservedCPU/v_rp*100)
    MEM得分sum(reservedMEM/v_rm*100)
    '''
    # print "\n 进入weightVMBins_FFDSum() 方法"

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
            # FFDSum求权重的打分方式
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

def map_h2v(bins):
    '''
    依据bins中map_v_h，将其转为hm为key，vms list为value的字典
    '''
    # 转换map_v_h为map_h_v
    map_h_v = collections.defaultdict(list)
    for key, value in bins['map_v_h'].items():
        map_h_v[value].append(key)
    return map_h_v

def consolidation_costs(bins, num_crash, map_d_s, map_s_d, size=1):
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

        print "正在进行代价计算"
        # 计算总能耗及各running VM/HM负载均衡指数
        tmp0, tmp1 = len(used_vms), len(used_hms)
        cost['used_hms'] = tmp1
        while tmp1 > 0:
            h = used_hms[tmp1 - 1]   
            # 以docker作为实际负载进行代价计算
            true_load_cpu = sum([bins['v_p_cost'][i][v] for v in map_h_v[h]])
            true_load_mem = sum([bins['v_m_cost'][i][v] for v in map_h_v[h]])
            # 计算集群剩余资源量即各HM节点cpu、mem余量之乘积，所有active HM求和
            utilization += (1.0 - true_load_cpu) * (1.0 - true_load_mem)
            cost['power_cost'] += 446.7 + 5.28*true_load_cpu - 0.04747*true_load_cpu**2 + 0.000334*true_load_cpu**3
            tmp1 -= 1
        cost['degree_of_concentration'] = 100 * cost['used_hms'] - 13 * utilization
        print "资源碎片化程度计算完毕"
        # 计算VM迁移时间（仅聚合阶段）
        pass

        # 模拟宕机计算容错
        cost['tolerance'] = tolerance.simulate_crash_HM(bins, num_crash, map_d_s, map_s_d)
    return cost

def for_vm_mbbo(bins):
    '''
    2017-12-24 本方法同样适用于doc_mbbo中！
    vm_mbbo将容器当作VM中服务，故聚合时不予理会，只需记录各虚拟机实际被容器占用的v_p_cost与v_m_cost用于进行对比
    提取集群当前真正用于承载容器的VM CPU、MEM列表，未占用者设为0.0
    '''
    rp, rm = [], []
    v_p_cost, v_m_cost = [], []
    for x in xrange(len(bins['v_rp'])):
        # 判断该VM是否承载
        if bins['v_p_cost'][0][x] != 0.0 or bins['v_m_cost'][0][x] != 0.0:
            rp.append(bins['v_rp'][x])
            rm.append(bins['v_rm'][x])
            v_p_cost.append(bins['v_p_cost'][0][x])
            v_m_cost.append(bins['v_m_cost'][0][x])
        else:
            rp.append(0.0)
            rm.append(0.0)
            v_p_cost.append(0.0)
            v_m_cost.append(0.0)
    return rp, rm, v_p_cost, v_m_cost

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
    # 对比实验一 (已完成)
    # 用于d-v-h3层聚合与v-h2层聚合 FFDSum 聚合对比， 不考虑容错能力并且在代价中也不计算tolerance
    # p_crash = 0.1
    # data = {
    #     'scale' : [],
    #     'degree_of_concentration_2':[],
    #     'tolerance_2': [],
    #     'power_cost_2': [],
    #     'used_hms_2': [],
    #     'degree_of_concentration_3':[],
    #     'tolerance_3': [],
    #     'power_cost_3': [],
    #     'used_hms_3': []
    # }
    # cycle = [100, 500, 1000, 4000, 5000]
    # for scale in cycle:
    #     init_popu0 = init.main_init(scale, 1.0)
    #     init_popu1 = copy.deepcopy(init_popu0)
    #     # 3层聚合与代价计算(不考虑容错)
    #     init_popu0  = FFDSum_3_Consol(init_popu0)
    #     cost0 = consolidation_costs(init_popu0, p_crash)
    #     # 2层聚合与代价计算（不考虑容错）
    #     init_popu1 = FFDSum_2_Consol(init_popu1)
    #     cost1 = consolidation_costs(init_popu1, p_crash)
    #     s0 = "\n不考虑容错的： 3层聚合  cost0={}\n 2层聚合 cost1={}".format(cost0, cost1)
    #     with open('aaa.py', 'a') as f:
    #         f.write(s0)



    # 对比实验二  （已完成）
    # 用于d-v-h3层支持HM级容错聚合与v-h2层不支持容错聚合对比， 使用FFDSum 方法聚合
    # 由init.main_init()创建随机集群状态后生成map_d_s、map_s_d映射，用于容错计算与独立性修复检测
    # num_crash = 8
    # data = {
    #     'scale' : [],
    #     'degree_of_concentration_2':[],
    #     'tolerance_2': [],
    #     'power_cost_2': [],
    #     'used_hms_2': [],
    #     'degree_of_concentration_3':[],
    #     'tolerance_3': [],
    #     'power_cost_3': [],
    #     'used_hms_3': []
    # }
    # cycle = [100, 200, 300]
    # for scale in cycle:
    #     # 初始准备
    #     init_popu0 = init.main_init(scale, 1.0)
    #     map_d_s, map_s_d = docker2service(scale)
    #     init_popu1 = copy.deepcopy(init_popu0)
    #     cost0 = consolidation_costs(init_popu0, num_crash, map_d_s, map_s_d)
    #     # 3层聚合与代价计算(支持HM级容错)
    #     init_popu0  = safe_FFDSum_3_Consol(init_popu0, map_d_s, map_s_d)
    #     cost1 = consolidation_costs(init_popu0, num_crash, map_d_s, map_s_d)
    #     # 2层聚合与代价计算（不支持容错）
    #     init_popu1 = FFDSum_2_Consol(init_popu1)
    #     cost2 = consolidation_costs(init_popu1, num_crash, map_d_s, map_s_d)
    #     s0 = "\n聚合前集群代价={}\n支持HM级容错的 3层聚合  cost0={}\n 不支持容错的 2层聚合 cost1={}".format(cost0, cost1, cost2)
    #     with open('aaa.py', 'a') as f:
    #         f.write(s0)



    # 用于d-v-h3层聚合与v-h2层聚合对比， 使用mbbo 方法聚合（未完成，明天写）
    num_crash = 8
    data = {
        'scale' : [],
        'degree_of_concentration_2':[],
        'tolerance_2': [],
        'power_cost_2': [],
        'used_hms_2': [],
        'degree_of_concentration_3':[],
        'tolerance_3': [],
        'power_cost_3': [],
        'used_hms_3': []
    }
    cycle = [100, 500, 1000, 4000, 5000]
    for scale in cycle:
        init_popu0 = init.main_init(scale, 1.0)
        init_popu1 = copy.deepcopy(init_popu0)
        # 2层聚合时需要的集群状态信息
        rp, rm, v_p_cost, v_m_cost = for_vm_mbbo(init_popu0)
        cost0 = vm_mbbo.main(100, 5, 100, 1.0, ['power'], rp, rm, v_p_cost, v_m_cost)
        # 3层聚合时需要的集群状态信息
        rp3, rm3, v_p_cost3, v_m_cost3 = for_vm_mbbo(init_popu1)
        init_popu0  = doc_mbbo(init_popu0)   没写完！！！！
        s0 = "\n3层聚合  cost0={}\n 2层聚合 cost1={}".format(cost0, cost1)
        with open('aaa.py', 'a') as f:
            f.write(s0)



    # 用于d-v-h3层架构下,FFDSum与mbbo聚合结果对比（这个不需要画图，可以弄成表格）









    # 希望与新增阶段结合起来的聚合算法（没写完，有问题）
    # 由addtion_phase/init 模块main_init方法生成初始
    # init_popu = init.main_init(100, 1.0)
    # consolidation_popu = 0
    # p_crash = 0.1
    # print "集群初始化完毕"
    # total = len(init_popu['c_rp'])
    # cycle = [100, 300, 500, 700]#, 900, 1300, 1500, 1700, 1900, 2100, 2300]
    # count = 0  # 每增量放置3批，进行一次聚合
    # data0 = {  # 记录新增与vm_bb0
    #     'scale' : [],
    #     'degree_of_concentration':[],
    #     'tolerance': [],
    #     'power_cost': [],
    #     'used_hms': []
    # }
    # data1 = {  # 记录新增与FFDSum_consolidation
    # 'scale' : [],
    # 'degree_of_concentration':[],
    # 'tolerance': [],
    # 'power_cost': [],
    # 'used_hms': []
    # }
    # # 记录初始代价
    # cost0 = consolidation_costs(init_popu, p_crash)
    # data0 = create_JSON(data0, total, cost0['degree_of_concentration'], cost0['power_cost'], cost0['tolerance'], cost0['used_hms'])
    # data1 = create_JSON(data1, total, cost0['degree_of_concentration'], cost0['power_cost'], cost0['tolerance'], cost0['used_hms'])
    # print data0
    # for scale in cycle:
    #     print "正在进行{}批量的增加".format(scale)
    #     count += 1
    #     # 生成增量
    #     addtion0 = init.create_addtion(1.0, scale)

    #     # 首先进行增量批放置
    #     print "将进行初始放置"
    #     init_popu = Contrast.FFDSum_simple(init_popu, addtion0)
    #     total = len(init_popu['c_rp']) + sum(addtion0['replicas'])
    #     cost1 = consolidation_costs(init_popu, p_crash)
    #     data0 = create_JSON(data0, total, cost1['degree_of_concentration'], cost1['power_cost'], cost1['tolerance'], cost1['used_hms'])
    #     data1 = create_JSON(data1, total, cost1['degree_of_concentration'], cost1['power_cost'], cost1['tolerance'], cost1['used_hms'])
    #     # 增量放置3次进行聚合
    #     if count == 3:
    #         count = 0  
    #         print "将进行聚合放置"
    #         consolidation_popu0 = init.main_init(total, 1.0)
    #         consolidation_popu1 = copy.deepcopy(consolidation_popu0)
    #         # 将当前集群状态中真正用到的vm进行提取，作为mbbo算法rp,rm
    #         rp, rm, v_p_cost, v_m_cost = for_vm_mbbo(consolidation_popu0)
    #         # 用于两种聚合算法对比
    #         # vmbbo直接进行聚合放置与代价返回
    #         cost2 = vm_mbbo.main(100, 5, total, 1.0, ['power'], rp, rm, v_p_cost, v_m_cost)
    #         data0 = create_JSON(data0, total, cost2['degree_of_concentration'], cost2['power_cost'], cost2['tolerance'], cost2['used_hms'])
    #         # FFDSum_consolidation
    #         consolidation_popu = FFDSum_Consol(consolidation_popu1)
    #         cost3 = consolidation_costs(consolidation_popu, p_crash)
    #         data1 = create_JSON(data1, total, cost2['degree_of_concentration'], cost2['power_cost'], cost2['tolerance'], cost2['used_hms'])
    # with open('.//viz//consolidation-no-safe-{}-demo.json'.format(datetime.datetime.now()),'a') as f:
    #     f.flush()
    #     json.dump(data0, f, indent=2)
    #     f.write('\n\n')
    #     json.dump(data1, f, indent=2)












    # 用于论文中代码提交
    # # 由addtion_phase/init 模块main_init方法生成初始
    # init_popu = init.main_init(100, 1.0)
    # p_crash = 0.1
    # print "集群初始化完毕"
    # scale = len(init_popu['c_rp'])
    # cycle = [100, 300, 500, 700]#, 900, 1300, 1500, 1700, 1900, 2100, 2300]
    # count = 0  # 每增量放置3批，进行一次聚合
    # data = {
    #     'scale' : [],
    #     'degree_of_concentration':[],
    #     'tolerance': [],
    #     'power_cost': [],
    #     'used_hms': []
    # }
    # # 记录初始代价
    # cost0 = consolidation_costs(init_popu, p_crash)
    # data = create_JSON(data, scale, cost0['degree_of_concentration'], cost0['power_cost'], cost0['tolerance'], cost0['used_hms'])
    # print data
    # for scale in cycle:
    #     print "正在进行{}批量的增加".format(scale)
    #     count += 1
    #     # 生成增量
    #     addtion0 = init.create_addtion(1.0, scale)

    #     # 首先进行增量批放置
    #     print "将进行初始放置"
    #     init_popu = Contrast.FFDSum_simple(init_popu, addtion0)
    #     scale += sum(addtion0['replicas'])
    #     cost1 = consolidation_costs(init_popu, p_crash)
    #     data = create_JSON(data, scale, cost1['degree_of_concentration'], cost1['power_cost'], cost1['tolerance'], cost1['used_hms'])
        
    #     # 增量放置3次进行聚合
    #     if count == 3:
    #         count = 0  
    #         print "将进行聚合放置"
    #         s0 = 'bins={}'.format(init_popu)
    #         with open('aaa.py', 'a') as f:
    #             f.write(s0)
    #         init_popu = FFDSum_Consol(init_popu)
    #         cost2 = consolidation_costs(init_popu, p_crash)
    #         data = create_JSON(data, scale, cost2['degree_of_concentration'], cost2['power_cost'], cost2['tolerance'], cost2['used_hms'])
    # with open('.//viz//consolidation-no-safe-{}-demo.json'.format(datetime.datetime.now()),'w') as f:
    #     f.flush()
    #     json.dump(data, f, indent=2)

