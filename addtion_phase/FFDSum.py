#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-15
@Author : Amy
Goal : saving host machines
Digest : 定义FFD-based Herustics常见方法FFDSum即通过将多维demand、capacites向量转化为意义明确的标量(volume of the vector)，
      以标量值大小为bins、objects的排序标准，再依据资源约束，循环求解vector bin pack结果。
      weight ：the ratio between the total demand for resource i and the capacity of the host
      FFDSum 以 sum(w_i*v_i) 对所有纬度值乘以weight再求和；
      此次对比中，采用swarm binpack strategy —— scores 作为排序标准，见weighted_node.go
'''


import time
import random
import sys




rp_option = [1.0]                      # vm可选的cpu尺寸
rm_option = [1.0]                      # vm可选的mem尺寸
               

def FFDSum(bins, objects):
    '''
    @param: bins 代表当前系统状态
            objects 代表待放入bin的容器
    @return: 安排好所有objects的集群bins状态
    '''

    print " \n 进入 FFDSum() 方法" 


    time0 = time.time()

    # d-v-h架构下新增阶段希望做到一定节能，即尽可能使用当前已有的VM，尽量不去开启新的HM
    # 情况1： 新增容器以VM作为直接node考虑，为当前所有可容纳running VM打分，分最高者放入
    # 情况2： all running vms均无法放入，init_VM产生新VM，再对所有HM打分，分最高者放入

    for x in xrange(len(objects['c_rp'])):
        object_CPU, object_MEM, i = objects['c_rp'][x], objects['c_rm'][x], objects['replicas'][x]
        
        while i>0:
            # 对该object(容器)计算所有bins（VMs）得分
            weightedVMBins = weightVMBins(bins, object_CPU, object_MEM)

            # 至少有VM可以容纳该Object时，放入并更改参数
            if len(weightedVMBins) > 0:
                # 获取得分最多bins的编号
                vm_suffix = max(weightedVMBins, key=weightedVMBins.get)

                # 且该VM已经在当前集群中有映射HM
                if vm_suffix in bins['map_v_h']:
                    hm_suffix = bins['map_v_h'][vm_suffix]

                # 否则，需要为该VM找寻可以hosted 的HM,并更新资源
                else:
                    hm_suffix = find_HM(bins, bins['v_rp'][vm_suffix], bins['v_rm'][vm_suffix], vm_suffix)

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
                vm = create_VM(object_CPU, object_MEM, rp_option, rm_option)
                vm_suffix = len(bins['v_p_cost'][0])

                # 为该VM找寻HM,并更新HM资源变动及map_v_h
                hm_suffix = find_HM(bins, vm['rp'], vm['rm'], vm_suffix)

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
    print "used time is {} \n used the number of HMs is {}".format(time1-time0, len(num))
    return bins




def find_HM(bins, v_rp, v_rm, vm_suffix):
    '''
    为VM找寻可容纳其的HM标号(系统已有/新增)，并更新所引起的hm资源编号，及map_v_h
    '''
    # 对集群已有的所有HMs进行打分
    weightedHMBins = weightHMBins(bins, v_rp, v_rm)

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



def weightVMBins(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    print "\n 进入weightVMBins() 方法"

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


def weightHMBins(bins, object_CPU, object_MEM):
    '''
    计算集群bins(HMs)中所有bin的权重，并返回weightedHMBins记录有各个node(HM)得分的weightedHMBins
    '''
    print "\n 进入weightHMBins() 方法"


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


def create_VM(c_rp, c_rm, rp_option, rm_option):
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




if __name__ == '__main__':
    '''
    本模块测试算法是否运行正确
    '''
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
    # addition0 = {
    #     'c_rp': [0.2534765051859606, 0.2948935628141042, 0.2224244890668316, 0.18127979201839872, 0.32156802827499703],
    #     'c_rm': [0.3020445793942861, 0.3768727547924075, 0.006082192833673228, 0.15746276310264423, 0.39400382229512343],
    #     'replicas': [4, 0, 4, 3, 0]
    # }
    init_popu = {
        'c_rp': [0.49950862497815096, 0.49566299101104405, 0.19339860376391588, 0.22650079014580787, 0.4985697928665497, 0.23123095298795776, 0.08874821111583076, 0.21338379418561532, 0.19440106465844426,0.08929997048178007],
        'c_rm': [0.3909286789440798, 0.369809808223181, 0.00979746372201648, 0.025755088684076777, 0.33613683282363926, 0.09025060644602326, 0.03690588016174476, 0.1613365031750235, 0.1843056842347392, 0.1654617298885813],
        'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        'v_p_cost': [[0.19339860376391588, 0.4985697928665497, 0.49950862497815096, 0, 0.08929997048178007, 0.3199791641037885, 0.6900640556694884, 0.22650079014580787, 0, 0.21338379418561532]],
        'v_m_cost': [[0.00979746372201648, 0.33613683282363926, 0.3909286789440798, 0, 0.1654617298885813, 0.12715648660776802, 0.5541154924579201, 0.025755088684076777, 0, 0.1613365031750235]],
        'h_p_cost': [[0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]],
        'h_m_cost': [[0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]],
        'population': [[[2, 8], [6, 4], [0, 7], [7, 5], [1, 9], [5, 6], [5, 6], [9, 3], [6, 4], [4, 1]]],
        'map_v_h': {0: 7, 1: 9, 2: 8, 4: 1,5: 6, 6: 4, 7: 5, 9: 3}
        }
    addition0 = {
        'c_rp': [0.11908248759706352, 0.2539499371680547, 0.020365365071704944, 0.3948180323801204, 0.16201211844666025, 0.09712859701028537, 0.31390062270434416, 0.3480375603464177, 0.15014449094820942, 0.04822244066927983, 0.3928791357646204, 0.032534810957771, 0.4651545189795368, 0.0474215706739573, 0.07162125780399875, 0.40903739793374416, 0.0539330604724928, 0.2355628289244136, 0.19700257808129235, 0.373566830122395, 0.17717460262217066, 0.43991572626550735, 0.37451472906275923, 0.3135592929534395,0.015668465353517125, 0.10403211142071572, 0.21390117473577447, 0.4713342566285714, 0.17040421305346137, 0.3260384854338912, 0.2244028315904087, 0.2312332531063797, 0.45247614392078866, 0.20553810157861957, 0.3064820365449853, 0.31058025758787433, 0.1650102907341277, 0.19784436750803397, 0.44271702585692496, 0.1435831818575356, 0.46550750164344235, 0.34333834380364575, 0.027396746345203393, 0.36407514538409447, 0.18766287048391472, 0.1881570123326235, 0.45031175220343606, 0.44156291337181935, 0.3881099941271592, 0.08966540806915951],
        'c_rm': [0.15371760989287112, 0.4727080131827223, 0.1312785397644661, 0.3148741699625581, 0.15490164061562212, 0.2188793775769965, 0.42599638018947206, 0.4296657758683523, 0.04960548585622013, 0.12163920336361042, 0.4155052522150541, 0.22584319726937863, 0.4298025137237217, 0.02073334664757892, 0.0406855119064691, 0.2899188786601343, 0.13482466565478549, 0.1381986097950461, 0.12833142672404127, 0.47013534312111604, 0.15751054415325544, 0.45265496951228257, 0.31177491087859177, 0.4547144122615391, 0.2149583781080965, 0.002010100339807669, 0.23583146593132182, 0.2668389587972696, 0.023147288153819612, 0.49235190501873116, 0.11524643818001151, 0.10224202413249506, 0.39278777898283634, 0.021373650453562182, 0.2750448545115652, 0.49570452049049685, 0.0463055590081595, 0.10080163807146658, 0.3602772552783736, 0.2452958069609209, 0.4291638547046067, 0.4994509837339639, 0.21256047037541928, 0.2802727216555664, 0.24083778776514506, 0.11761680222091694, 0.4740337239408656, 0.292596240387029, 0.37749334161166404, 0.1872898013788786],
        'replicas': [4, 5, 5, 0, 3, 4, 3, 4, 4, 2, 2, 2, 2, 2, 3, 3, 2, 4, 3, 2, 4, 0, 1, 5, 3, 5, 2, 2, 2, 2, 5, 3, 3, 2, 4, 0, 1, 1, 4, 0, 1, 4, 1, 1, 5, 4, 5, 1, 1, 2]
        }

            
    s0 = 'Start: \n init_popu = {} \n addtion = {}'.format(init_popu, addition0)
    bins = FFDSum(init_popu, addition0)
    s1 = '\n\n End:   \n Bins = {}'.format(bins)    

    with open('addtion_phase//check_error.py','a') as f:
        f.flush()
        f.write(s0)
        f.write(s1)