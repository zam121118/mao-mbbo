#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
import random
import math
import copy
import collections
import multiprocessing
import datetime
import Contrast
from init import *


# 其中vm_option以资源降序排列
vm_option = [(1.0, 1.0), (1.0, 0.8), (0.8, 0.7), (0.6, 0.5), (0.5, 0.4), (0.3, 0.3)]



def detect_hm_independce(bins, max_suffix, addtion0):
    '''
    以HM为独立性基础
    @para: bins 经过初步算法安排的放置方案；addtion0该批新增实例服务及其replicas便于独立性检测;
           max_suffix记录上次满足服务容错（独立性的）的最大容器下标，本次检测从该下标之最大下标进行检测
    @func: 从init_server至最大，依据addtion0中各服务容器及其replicas依次检测其在bins['population']对应HM编号，
            当某服务的多个replicas同时放置于一个HM，则至少变换一个replica使其与集群中最大下标HM上某容器交换位置，
            直至检查完所有的service并返回修复独立性之后的bins
    '''
    # 遍历所有容器service
    for x in xrange(len(addtion0['c_rp'])):
        # 各服务所需容器配置及replicas数量
        object_CPU, object_MEM, i = addtion0['c_rp'][x], addtion0['c_rm'][x], addtion0['replicas'][x]
        # 若该服务replica为1，即单节点独立; 若为0说明服务启动失败，没有实际容器放置
        if i == 1 or i == 0:
            continue
        # 该服务所有replicas对应HM下标
        dockers = service2docker(x, max_suffix, bins['population'][0], addtion0)
        try:
            service2hms = [bins['population'][0][j][-1] for j in dockers]
        except IndexError, e:
            print bins['population'][0][dockers[0]]
            print dockers
        # 独立性检测， 若该suffix所有HM值均相同则不满足需要修复，否则满足
        num_hms = len(set(service2hms))
        # 若满足独立性，则进行下一个服务检测
        if num_hms != 1:
            continue

        # 不满足独立性需要进行修复
        flag = False           # 还未修复为False
        # 对该服务的第一个支撑replica从active HMs最大下标者开始依次往前，寻找可与该容器对调换位置的容器
        origin_docker_suffix = dockers[0]
        used_hms = bins['map_v_h'].values()
        used_hms.remove(service2hms[0])
        origin_vm_suffix = bins['population'][0][origin_docker_suffix][0]
        for hm in sorted(used_hms, reverse=True):
            dockers, vms = find_docker_onHM(bins, hm, 0)
            # 依次寻找其他HM上可与该服务第一个replica对掉而满足双方资源约束的解
            for i in xrange(len(dockers)):
                vm_suffix = vms[i]
                docker_suffix = dockers[i]
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
                    bins['population'][0][docker_suffix] = [origin_vm_suffix, service2hms[0]]
                    # map_v_h由于是对掉并不会产生新的拓扑变化，故不用更新
                    flag = True
                    break
            # 若在该hm上对换而修复，则推出本次service修复，进入下一个
            if flag:
                break
            # 否则继续寻找下一个hm
        # 若所有active HMs均无发用于修复独立性,则新建HM与VM
        if not flag:
            vm = Contrast.create_VM_random(object_CPU, object_MEM, vm_option)
            vm_suffix = len(bins['v_p_cost'][0])
            hm_suffix = len(bins['h_m_cost'][0])
            bins['v_p_cost'][0].append(object_CPU)
            bins['v_m_cost'][0].append(object_MEM)
            bins['v_rp'].append(vm['rp'])
            bins['v_rm'].append(vm['rm'])
            bins['h_p_cost'][0].append(vm['rp'])
            bins['h_m_cost'][0].append(vm['rm'])
            bins['map_v_h'][vm_suffix] = hm_suffix
            bins['population'][0][origin_docker_suffix] = [vm_suffix, hm_suffix]
            flag = True
        
    return bins

def detect_vm_independce(bins, max_suffix, addtion0):
    '''
    以VM为独立性基础
    @para: bins 经过初步算法安排的放置方案；addtion0该批新增实例服务及其replicas便于独立性检测;
           max_suffix记录上次满足服务容错（独立性的）的最大容器下标，本次检测从该下标之最大下标进行检测
    @func: 从init_server至最大，依据addtion0中各服务容器及其replicas依次检测其在bins['population']对应VM编号，
            当某服务的多个replicas同时放置于一个VM，则在集群中FFD遍历其他VM,其上可与该容器尺寸者互换位置,
            直至检查完所有的service并返回修复独立性之后的bins
    '''
    # 遍历所有容器service
    for x in xrange(len(addtion0['c_rp'])):
        # 各服务所需容器配置及replicas数量
        object_CPU, object_MEM, i = addtion0['c_rp'][x], addtion0['c_rm'][x], addtion0['replicas'][x]
        # 若该服务replica为1，即单节点独立; 若为0说明服务启动失败，没有实际容器放置
        if i == 1 or i == 0:
            continue
        # 该服务所有replicas对应HM下标
        dockers = service2docker(x, max_suffix, bins['population'][0], addtion0)
        try:
            service2vms = [bins['population'][0][j][0] for j in dockers]
        except IndexError, e:
            print bins['population'][0][dockers[0]]
            print dockers
        # 独立性检测， 若该suffix所有HM值均相同则不满足需要修复，否则满足
        num_hms = len(set(service2vms))
        # 若满足独立性，则进行下一个服务检测
        if num_hms != 1:
            continue

        # 不满足独立性需要进行修复
        flag = False           # 还未修复为False
        # 对该服务的第一个支撑replica从active HMs最大下标者开始依次往前，寻找可与该容器对调换位置的容器
        used_vms = bins['map_v_h'].keys()
        used_vms.remove(service2vms[0])
        origin_docker_suffix = dockers[0]
        origin_vm_suffix = bins['population'][0][origin_docker_suffix][0]
        # 依次寻找其他VM上可与该服务第一个replica对掉而满足双方资源约束的解
        for vm in sorted(used_vms):
            dockers = find_docker_onHM(bins, vm, 1)
            for i in xrange(len(dockers)):
                # 换出原docker换入replica之后的资源
                reversed_cpu1 = bins['v_rp'][vm] - (bins['v_p_cost'][0][vm] - bins['c_rp'][i] + object_CPU)
                reversed_mem1 = bins['v_rm'][vm] - (bins['v_m_cost'][0][vm] - bins['c_rm'][i] + object_MEM)
                # 换入新容器换出replica后的资源
                reversed_cpu0 = bins['v_rp'][origin_vm_suffix] - (bins['v_p_cost'][0][origin_vm_suffix] + bins['c_rp'][i] - object_CPU)
                reversed_mem0 = bins['v_rm'][origin_vm_suffix] - (bins['v_m_cost'][0][origin_vm_suffix] + bins['c_rm'][i] - object_MEM)
                # 若对换后满足资源约束，则更新集群
                if reversed_cpu0 >= 0 and reversed_cpu1 >= 0 and reversed_mem0 >= 0 and reversed_mem1 >=0:
                    bins['v_p_cost'][0][vm] += (object_CPU - bins['c_rp'][i])
                    bins['v_m_cost'][0][vm] += (object_MEM - bins['c_rm'][i])
                    bins['v_p_cost'][0][origin_vm_suffix] += (bins['c_rp'][i] - object_CPU)
                    bins['v_m_cost'][0][origin_vm_suffix] += (bins['c_rm'][i] - object_MEM)
                    bins['population'][0][origin_docker_suffix] = [vm, bins['map_v_h'][vm]]
                    bins['population'][0][i] = [origin_vm_suffix, bins['map_v_h'][origin_vm_suffix]]
                    # map_v_h由于是对掉并不会产生新的拓扑变化，故不用更新
                    flag = True
                    break
            # 若在该hm上对换而修复，则推出本次service修复，进入下一个
            if flag:
                break
            # 否则继续寻找下一个hm
        # 若所有active HMs均无发用于修复独立性,则新建HM与VM
        if not flag:
            vm = Contrast.create_VM_random(object_CPU, object_MEM, vm_option)
            vm_suffix = len(bins['v_p_cost'][0])
            hm_suffix = len(bins['h_m_cost'][0])
            bins['v_p_cost'][0].append(object_CPU)
            bins['v_m_cost'][0].append(object_MEM)
            bins['v_rp'].append(vm['rp'])
            bins['v_rm'].append(vm['rm'])
            bins['h_p_cost'][0].append(vm['rp'])
            bins['h_m_cost'][0].append(vm['rm'])
            bins['map_v_h'][vm_suffix] = hm_suffix
            bins['population'][0][origin_docker_suffix] = [vm_suffix, hm_suffix]
            flag = True
        
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

def docker2service(bins, map_d_s, max_service_suffix, addtion0):
    '''
    map_d_s是已有集群的docker-service，且此时docker最大下标为该list长度
    max_service_suffix是已有集群所有服务的最大下标
    对于一个给定的集群手动维护docker-service映射
    '''
    for i in xrange(len(addtion0['replicas'])):
        x = addtion0['replicas'][i]
        while x > 0:
            map_d_s.append(i + max_service_suffix + 1)
            x -= 1
    return map_d_s

def service2docker(service_suffix, max_suffix, population, addtion0):
    '''
    根据集群中bins['population']与容器增量addtion0，以及集群初始化时已有的容器的最大下标max_suffix
    返回支持第service_suffix号服务的所有容器下标
    '''
    start = sum(addtion0['replicas'][:service_suffix]) + max_suffix + 1
    try:
        end = start + addtion0['replicas'][service_suffix]
        # 若服务对应的副本数量为空，则其dockersf为空列表
        dockers = [i for i in xrange(start, end)]
        return dockers
    except IndexError, e:
        print start, service_suffix
        return False

def deprated_docker2service(docker_suffix, max_suffix, population, addtion0):
    '''
    2017-12-20 由于折半查找时间复杂度高，很耗时 
    根据addtion与population，max_suffix为初始化集群后已有容器的最大下标
    计算给定下标的容器其所属服务编号，以及该服务的所有支持容器副本下标
    '''
    services = []
    # 使用折半查找
    high = len(addtion0['replicas']) - 1
    low = 0
    mid = (low+high+1)/2
    while high>=0:
        dockers = service2docker(mid, max_suffix, population, addtion0)
        if dockers is False:
            print 'docker_suffix={},low={},mild={},high={}'.format(docker_suffix, low, mid, high)
            sys.exit()
        # 列表为空，该服务实际没有运行容器
        if not dockers:
            mid += 1
            continue
        # 刚好找到容器对应的服务, 记录服务与容器对应关系[service_suffix, dockers_list]
        elif docker_suffix in dockers:
            services.append(mid)
            services.append(dockers)
            break
        # 向低端查找
        elif docker_suffix < dockers[0]:
            high = mid - 1
        # 向大端查找
        elif docker_suffix > dockers[-1]:
            low = mid
        mid = (low+high+1)/2
    if services:
        return services
    if not services:
        print "找不到容器对应的服务，有错"
        sys.exit()

def simulate_crash_HM(p_crash, max_suffix, bins, addtion0, map_d_s):
    '''
    2017-12-20 22:00 更新：
        为了保证计算公平性，应使用宕机概率提前选出预备宕机HMs，再进行容错计算
    通过HMs被宕机概率选中来模拟集群HMs宕机现象，并计算因这些机器crash而造成的服务终止问题，使用容错力衡量公式进行计算
    tolerance = a*N_severity+b*N_medium+c*N_mild, a，b, c分别取10,3,1
    '''
    N_severity, N_medium, N_mild = 0, 0, 0
    active_hms = list(set(bins['map_v_h'].values()))
    # 记录宕机引起的嫌疑危机服务，与其对应的处于危机中的容器个数
    crash_hms, crash_services = [], {}
    # 模拟宕机，记录宕机序列
    for h in active_hms:
        # 即该HM被crash
        if random.random() < p_crash:
            print '第 {} hm将被摧毁'.format(h)
            crash_hms.append(h)
            print "开始查找该hm上的容器"
            dockers, vms = find_docker_onHM(bins, h, 0)
            print "结束查找该hm上的容器"
            # 遍历dockers
            for d in dockers:
                # 认为max_suffix及之前的容器服务均满足容错性
                if d <= max_suffix:
                    continue
                print "开始找容器 {} 所属的服务".format(d)
                #services = docker2service(d, max_suffix, bins['population'][0], addtion0) # 容器对应的服务
                services = [map_d_s[d], 0]
                services[-1] = service2docker(services[0], max_suffix, bins['population'][0], addtion0)
                print "结束找容器 {} 所属的服务".format(d)
                hms = [bins['population'][0][i][-1] for i in services[-1]]    # 该服务的支撑容器所分布的HM编号列表
                dangerous_num = 0
                for x in crash_hms:                       # 处于危险状态的容器数量
                    dangerous_num += hms.count(x) 
                safe_num = len(hms) - hms.count(h)
                if safe_num < 1:
                    N_severity += 1
                elif safe_num < 2 and safe_num >= 1:
                    N_medium += 1
                elif safe_num >= 2:
                    N_mild += 1
                crash_services[services[0]] = [dangerous_num, safe_num]
        continue
    # 计算方案容错能力
    tolerance = 10 * N_severity + 3 * N_medium + N_mild
    return tolerance,crash_hms,crash_services

def safe_FFDSum_simple(bins, addtion0):
    '''
    调用Contrast模块FFDSum_simple方法进行初始放置计算；
    再使用本模块detect_vm_indepence方法进行VM Node独立性调整与修复
    '''
    after_bins, used_time = Contrast.FFDSum_simple(bins, addtion0)
    after_bins = detect_vm_independce(after_bins, max_suffix, addtion0)
    return after_bins

def safe_FFDSum_complex(bins, addtion0):
    '''
    调用Contrast模块FFDSum_complex方法进行初始放置计算；
    再使用本模块detect_hm_indepence方法进行HM Node独立性调整与修复
    '''
    after_bins, used_time = Contrast.FFDSum_simple(bins, addtion0)
    after_bins = detect_vm_independce(after_bins, max_suffix, addtion0)
    return after_bins
    return bins

def compute_costs(bins, size=1):
    '''
    优化目标，新增场景提高各节点实际物理资源利用率，即集群中剩余资源利用率最大，减少碎片化资源
    再加容错能力
    '''   

    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'degree_of_concentration': 0.0,
        'power_cost': 0.0,
        'used_hms': 0,
        }
    map_v_h = bins['map_v_h']
    map_h_v = Contrast.map_h2v(bins)
    used_hms = list(set(map_v_h.values()))
    
    # Then, 对bins中前size个方案计算代价值（在新增算法中，size只有0一种值）
    for i in xrange(size):
        utilization = 0
        # 计算总能耗及各running VM/HM负载均衡指数
        tmp1 = len(used_hms)
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

        # 计算VM迁移时间（仅聚合阶段）
        pass
    return cost['degree_of_concentration']

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
    模拟从集群初始化到批量新增,每增加一批新容器的宕机概率
    '''
        # 1. 程序初始设定
    # 多进程初始化
    # p = multiprocessing.Pool()
    manager = multiprocessing.Manager()
    jobs = []
    # main_init(50, 1.0)进行的最初初始化
    p_crash = 0.1
    max_suffix = 49
    # 重复次数(重复几次就用几个并行进程)
    Gen = 2
    # 用于生成记录容错能力的json的数据
    data = {
        'scale':[],
        'simple':[],
        'complex':[],
        'safe_simple':[],
        'safe_complex':[]
    }
    map_d_s = [-1] * (max_suffix + 1)
        

    # 2. 产生新初始集群与新增容器的服务数量,创建多个初始数据集,便于多进程
    init_popu0 = main_init(max_suffix+1, 1.0)
    init_popu1 = copy.deepcopy(init_popu0)
    cycle = []
    for i in xrange(1, 6):
        a = 10 ** i
        ll = sorted(random.sample(range(1,10), 4))
        for j in ll:
            cycle.append(j*a)

    # 3. 模拟多批量新增场景
    for scale in cycle:
        max_service_suffix = -1
        avg_simple = [0, 0, 0]
        avg_complex = [0, 0, 0]
        avg_safe_simple = [0, 0, 0]
        avg_safe_complex = [0, 0, 0]

        # 创建2种新增批量,分别给2个进程独立计算
        addtion0 = create_addtion(1.0, scale)
        addtion1 = create_addtion(1.0, scale)
        avg_scale = 2 * len(init_popu0['c_rp']) + sum(addtion0['replicas']) + sum(addtion1['replicas'])

        # 设置多进程间共享变量
        return_dict = manager.dict()
        # 运行gen个进程进行分别计算求均值
        for gen in xrange(Gen):
            if gen == 0:
                p = multiprocessing.Process(target=main_controller, args=(0, init_popu0, addtion0, safe_FFDSum_simple, p_crash, max_suffix, max_service_suffix, map_d_s, return_dict))
                jobs.append(p)
                p.start()
            elif gen == 1:
                p = multiprocessing.Process(target=main_controller, args=(1, init_popu1, addtion1, safe_FFDSum_complex, p_crash, max_suffix, max_service_suffix, map_d_s, return_dict))
                jobs.append(p)
                p.start()

        for proc in jobs:
            proc.join()

        # print return_dict.values()
        avg_safe_simple[0] += return_dict[0][0]
        avg_safe_simple[1] += return_dict[0][1]
        avg_safe_simple[2] += return_dict[0][2]
        avg_safe_complex[0] += return_dict[1][0]
        avg_safe_complex[1] += return_dict[1][1]
        avg_safe_complex[2] += return_dict[1][2]
        avg_simple = 0
        avg_complex = 0
        
        # 更新最大服务下标\上次检查过容错性的容器最大下标
        max_service_suffix += scale
        # 计算迭代gen代的平均值,并写入文件
        avg_scale /= Gen
        avg_safe_simple[0] /= Gen
        avg_safe_simple[1] /= Gen
        avg_safe_simple[2] /= Gen
        avg_safe_complex[0] /= Gen
        avg_safe_complex[1] /= Gen
        avg_safe_complex[2] /= Gen
        data = createJSON(data, avg_scale, avg_simple, avg_complex, avg_safe_simple, avg_safe_complex)
  
    # # 4. 记录data用于前端数据可视化
    with open('.//viz//contrast-addtion-{}-demo.json'.format(datetime.datetime.now()),'w') as f:
        f.flush()
        json.dump(data, f, indent=2)

































    # # 1. 程序初始设定
    # # 多进程初始化
    # # p = multiprocessing.Pool()
    # manager = multiprocessing.Manager()
    # jobs = []
    # # main_init(50, 1.0)进行的最初初始化
    # p_crash = 0.1
    # max_suffix = 49
    # # 重复次数
    # Gen = 1
    # # 用于生成记录容错能力的json的数据
    # data = {
    #     'scale':[],
    #     'simple':[],
    #     'complex':[],
    #     'safe_simple':[],
    #     'safe_complex':[]
    # }
    # map_d_s = [-1] * (max_suffix + 1)
        

    # # 2. 产生新初始集群与新增容器的服务数量
    # init_popu0 = main_init(max_suffix+1, 1.0)
    # init_popu1 = copy.deepcopy(init_popu0)
    # cycle = []
    # for i in xrange(1, 3):
    #     a = 10 ** i
    #     ll = sorted(random.sample(range(1,10), 4))
    #     for j in ll:
    #         cycle.append(j*a)

    # # 3. 模拟多批量新增场景
    # for scale in cycle:
    #     max_service_suffix = -1
    #     avg_scale = 0
    #     avg_simple = [0, 0, 0]
    #     avg_complex = [0, 0, 0]
    #     avg_safe_simple = [0, 0, 0]
    #     avg_safe_complex = [0, 0, 0]

    #     # 运行10次，取效果最好者
    #     for gen in xrange(Gen):
    #         # 记录初始集群信息并深度拷贝多副本用于算法间对比
    #         addtion0 = create_addtion(1.0, scale)
    #         avg_scale += len(init_popu0['c_rp']) + sum(addtion0['replicas'])

    #         # 对初始集群的多副本进行不同放置决策并计算优化模型结果
    #         #[x.get() for x in [pool.apply_async(pool_test, (x,)) for x in gen_list(l)]]
    #         return_dict = manager.dict()
    #         p = multiprocessing.Process(target=main_controller, args=(0, init_popu0, addtion0, safe_FFDSum_simple, p_crash, max_suffix, max_service_suffix, map_d_s, return_dict))
    #         jobs.append(p)
    #         p.start()
    #         p = multiprocessing.Process(target=main_controller, args=(1, init_popu1, addtion0, safe_FFDSum_complex, p_crash, max_suffix, max_service_suffix, map_d_s, return_dict))
    #         jobs.append(p)
    #         p.start()

    #         # print p.map(main_controller, (init_popu0, init_popu1), (addtion0, addtion0), (FFDSum_simple, FFDSum_complex))

    #         for proc in jobs:
    #             proc.join()
    #         # print return_dict.values()
    #         avg_safe_simple[0] += return_dict[0][0]
    #         avg_safe_simple[1] += return_dict[0][1]
    #         avg_safe_simple[2] += return_dict[0][2]
    #         avg_safe_complex[0] += return_dict[1][0]
    #         avg_safe_complex[1] += return_dict[1][1]
    #         avg_safe_complex[2] += return_dict[1][2]
    #         avg_simple = 0
    #         avg_complex = 0
        
    #         # 更新最大服务下标\上次检查过容错性的容器最大下标
    #         max_service_suffix += scale
    #     # 计算迭代gen代的平均值,并写入文件
    #     avg_scale /= Gen
    #     avg_safe_simple[0] /= Gen
    #     avg_safe_simple[1] /= Gen
    #     avg_safe_simple[2] /= Gen
    #     avg_safe_complex[0] /= Gen
    #     avg_safe_complex[1] /= Gen
    #     avg_safe_complex[2] /= Gen
    #     data = createJSON(data, avg_scale, avg_simple, avg_complex, avg_safe_simple, avg_safe_complex)
  
    # # # 4. 记录data用于前端数据可视化
    # with open('.//viz//contrast-addtion-{}-demo.json'.format(datetime.datetime.now()),'w') as f:
    #     f.flush()
    #     json.dump(data, f, indent=2)
