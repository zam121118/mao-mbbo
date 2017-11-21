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
    print "进入能耗、负载方差计算"
    # First, 构造代价变量，计算实际running VMs HMs
    cost = {
        'power_cost': 0.0,
        'v_balance_cost': 0.0,
        'h_balance_cost': 0.0,
        'used_vms': 0,
        'used_hms': 0
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

    print 'cost={}'.format(cost)
    return cost



def weightVMBins_FFDSum(bins, object_CPU, object_MEM):
    '''
    计算集群bins(VMs)中所有bin的权重，并返回weightedVMBins记录有各个node(VM)得分的weightedVMBins
    '''
    print "\n 进入weightVMBins_FFDSum() 方法"

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


def weightHMBins_FFDSum(bins, object_CPU, object_MEM):
    '''
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