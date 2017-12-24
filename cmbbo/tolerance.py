#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
2017-12-24  更新:
    模拟聚合阶段随机宕机某些HMs，统计其上运行的服务实际支持其运行的replicas数量
    代入tolerance中进行计算
'''

import time
import random
import copy
import collections
import Contrast
import FFDSum_Consolidation
import init


# 其中vm_option以资源降序排列
vm_option = [(1.0, 1.0), (1.0, 0.8), (0.8, 0.7), (0.6, 0.5), (0.5, 0.4), (0.3, 0.3)]

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

def simulate_crash_HM(bins, num_crash, map_d_s, map_s_d):
    '''
    2017-12-24 为了聚合阶段新写的。
        对于集群中all active HMs，指定随机挑选num_crash个HM为被摧毁对象。
        查找这些hm运行服务的支持副本数量代入tolerance= a*N_severity+b*N_medium+c*N_mild,
        a，b, c分别取10,3,1进行计算
    '''
    N_severity, N_medium, N_mild = 0, 0, 0
    crash_services = {}
    active_hms = list(set(bins['map_v_h'].values()))
    # 随机挑选被摧毁HMs列表
    hms_crash = random.sample(active_hms, num_crash)
    print "HM {} 将被摧毁".format(hms_crash)
    # 遍历宕机的HM，记录所有宕机造成的嫌疑服务与
    for h in hms_crash:
        print '第 {} hm将被摧毁'.format(h)
        dockers, vms = find_docker_onHM(bins, h, 0)
        print "hm {} 上有容器 {}".format(h, dockers)
        # 遍历dockers
        for d in dockers:
            # 依据该容器查其对应的服务
            service = map_d_s[d]
            print "容器 {} 所属的服务 {} ".format(d, service)
            # 确保所有的服务仅被检查一遍，避免同一服务多个容器多次被纳入tolerance计算
            if service not in crash_services:
                # 确认该服务所有对应的replicas及其所在HM下标
                replicas = map_s_d[service]
                replicas_hms = [bins['population'][0][i][-1] for i in replicas]
                print "服务 {} 的实际运行HM为 {}".format(service, replicas_hms)
                dangerous_num = 0
                # 统计该服务所有replicas实际HMs有多少被hm_crash选中(至少为1,即该h号HM)
                for x in hms_crash:
                    if x in replicas_hms:
                        dangerous_num += replicas_hms.count(x)
                print "服务 {} 有 {} 个容器处于危险中".format(service, dangerous_num)
                safe_num = len(replicas_hms) - dangerous_num
                if safe_num < 1:
                    N_severity += 1
                elif safe_num < 2 and safe_num >= 1:
                    N_medium += 1
                elif safe_num >= 2:
                    N_mild += 1
                crash_services[service] = [dangerous_num, safe_num]
    # 计算方案容错能力
    tolerance = 100 * N_severity + 3 * N_medium + N_mild
    print crash_services
    return tolerance

def main_controller(function_str, bins, addtion0, func_handler, p_crash, max_suffix, max_service_suffix, map_d_s, return_dict):
    '''
    2017-12-20 23:00 使用多进程共享变量与多进程实现2种方式并行计算
    function_str用于标识哪个方法0=safe_FFDSum_simple 1=safe_FFDSum_complex
    使用函数句柄实现不同方法的串行计算逻辑
    '''
    # 初始放置方案的计算
    after_bins = func_handler(bins, addtion0)
    map_d_s = docker2service(bins, map_d_s, max_service_suffix, addtion0)
    # 该方案的目标优化结果
    utilization = compute_costs(after_bins)
    tolerance, crash_hms, crash_services = simulate_crash_HM(p_crash, max_suffix, bins, addtion0, map_d_s)
    return_dict[function_str] = [utilization, tolerance, len(crash_hms)]
    return return_dict


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


if __name__=='__main__':
    '''
    模拟一个给定bins与map_d_s、map_s_d的集群，宕机后出现的问题
    '''
    num_crash = 4
    init_popu0 = init.main_init(50, 1.0)
    map_d_s, map_s_d = FFDSum_Consolidation.docker2service(50)
    tolerance = simulate_crash_HM(init_popu0, num_crash, map_d_s, map_s_d)
    s0 = "\nbins = {}\nmap_d_s = {}\nmap_s_d = {}\nnum_crash = {}\ntolerance = {}\n".format(init_popu0, map_d_s, map_s_d, num_crash, tolerance)
    with open('aaa.py', 'a') as f:
        f.write(s0)












