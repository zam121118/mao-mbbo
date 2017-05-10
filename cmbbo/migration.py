#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import math
import json
import sys

popu1 = {'elite_migration_time': 975, 'power_cost': [0.0, 0.0, 0.0], 'c_rp': [0.3229852959701244, 0.012917474886494529, 0.23468702638526817, 0.14331364963968823, 0.06976949598305543, 0.0021869563672370362, 0.15860397655309488, 0.3123397367952009, 0.39231479840113537, 0.02984993912219991, 0.052988077271532985, 0.15010615902087054, 0.022014844298087366, 0.21455300258041998, 0.4136554297867728], 'h_balance_cost': [0.0, 0.0, 0.0], 'v_rm': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'elite_h_balance': 14999985.0, 'v_balance_cost': [0.0, 0.0, 0.0], 'elite_power': 14999985.0, 'v_p_cost': [[0.3229852959701244, 0.4136554297867728, 0, 0.39231479840113537, 0.06976949598305543, 0.14331364963968823, 0, 0.15010615902087054, 0, 0, 0.022014844298087366, 0.0021869563672370362, 0.012917474886494529, 0.23468702638526817, 0.3123397367952009], [0.39231479840113537, 0.21455300258041998, 0.052988077271532985, 0.06976949598305543, 0.012917474886494529, 0, 0, 0, 0.02984993912219991, 0.23468702638526817, 0, 0, 0.3123397367952009, 0.3229852959701244, 0], [0, 0.06976949598305543, 0.14331364963968823, 0.15860397655309488, 0.012917474886494529, 0, 0.022014844298087366, 0, 0.39231479840113537, 0.02984993912219991, 0, 0.3229852959701244, 0, 0, 0.3123397367952009]], 'rank': [0, 0, 0], 'h_p_cost': [[1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0], [1.0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 0, 1.0, 0, 0, 0]], 'h_m_cost': [[1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 0, 1.0, 1.0], [1.0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 1.0, 0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0, 0, 1.0, 0, 0, 0]], 'v_m_cost': [[0.3393698761499144, 0.26563421396924014, 0, 0.49236890326589045, 0.19043323606485682, 0.11210690544323604, 0, 0.15886183265243792, 0, 0, 0.08755062728580135, 0.20003600058019932, 0.0252707394805457, 0.22540801200841618, 0.3384360761922669], [0.49236890326589045, 0.22269172595883455, 0.006009297276325987, 0.19043323606485682, 0.0252707394805457, 0, 0, 0, 0.20968700323404896, 0.22540801200841618, 0, 0, 0.3384360761922669, 0.3393698761499144, 0], [0, 0.19043323606485682, 0.11210690544323604, 0.1558738900073305, 0.0252707394805457, 0, 0.08755062728580135, 0, 0.49236890326589045, 0.20968700323404896, 0, 0.3393698761499144, 0, 0, 0.3384360761922669]], 'migration_time': [0.0, 0.0, 0.0], 'c_rm': [0.3393698761499144, 0.0252707394805457, 0.22540801200841618, 0.11210690544323604, 0.19043323606485682, 0.20003600058019932, 0.1558738900073305, 0.3384360761922669, 0.49236890326589045, 0.20968700323404896, 0.006009297276325987, 0.15886183265243792, 0.08755062728580135, 0.22269172595883455, 0.26563421396924014], 'elite_v_balance': 14999985.0, 'v_rp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'init_save': [[[0, 1], [12, 14], [13, 0], [5, 13], [4, 6], [11, 9], [0, 1], [14, 4], [3, 2], [0, 1], [4, 6], [7, 10], [10, 11], [4, 6], [1, 3]], [[13, 8], [4, 14], [9, 0], [13, 8], [3, 12], [4, 14], [13, 8], [12, 10], [0, 9], [8, 6], [2, 5], [2, 5], [2, 5], [1, 7], [0, 9]], [[11, 7], [4, 2], [4, 2], [2, 4], [1, 0], [2, 4], [3, 1], [14, 3], [8, 11], [9, 5], [8, 11], [4, 2], [6, 6], [9, 5], [8, 11]]], 'elite_chrom': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'population': [[[0, 1], [12, 14], [13, 0], [5, 13], [4, 6], [11, 9], [0, 1], [14, 4], [3, 2], [0, 1], [4, 6], [7, 10], [10, 11], [4, 6], [1, 3]], [[13, 8], [4, 14], [9, 0], [13, 8], [3, 12], [4, 14], [13, 8], [12, 10], [0, 9], [8, 6], [2, 5], [2, 5], [2, 5], [1, 7], [0, 9]], [[11, 7], [4, 2], [4, 2], [2, 4], [1, 0], [2, 4], [3, 1], [14, 3], [8, 11], [9, 5], [8, 11], [4, 2], [6, 6], [9, 5], [8, 11]]]}

def checkeffective(popu1,size,num_var):
    '''
    判断候选解的有效性
    '''
    # 先清空各vm,pm的资源使用率
    for i in xrange(size):
        for j in xrange(num_var):
            popu1['v_p_cost'][i][j] = 0
            popu1['v_m_cost'][i][j] = 0
            popu1['h_p_cost'][i][j] = 0
            popu1['h_m_cost'][i][j] = 0
    # 逐一按照候选解，计算实际占用的vm,hm资源
    for i in xrange(size):
        vm_used_id = {}                                # 避免相同vm同时被映射的不同hm的错误
        for j in xrange(num_var):                      # 容器编号
            flag = True
            v_id = popu1['population'][i][j][0]
            h_id = popu1['population'][i][j][1]
            if v_id in vm_used_id:                     # 若vm已经被安排过
                if (h_id == vm_used_id[v_id]):         # 且所在的hm与安排过的hm相同，则跳过该次循环，不需要重新计算资源占用
                    continue
                else:                                  # 若hm不同于安排的hm编号，说明出现同一个vm映射到不同hm的错误，直接返回
                    print "in this chrom %s, a vm has been hosted on different hm, totally wrong!! " %popu1['population'][i]
                    return False
            else:                                                 # 其他情况包括,包括多vm映射到1个hm,按正常情况计算
                popu1['v_p_cost'][i][v_id] += popu1['c_rp'][j]
                popu1['v_m_cost'][i][v_id] += popu1['c_rm'][j]
                popu1['h_p_cost'][i][h_id] += popu1['v_rp'][v_id]
                popu1['h_m_cost'][i][h_id] += popu1['v_rm'][v_id]
                vm_used_id[v_id] = h_id
        for x in xrange(num_var):                                  # 只要超出资源限约束，即报错
            if (popu1['v_p_cost'][i][x] > popu1['v_rp'][x] or popu1['v_m_cost'][i][x] > popu1['v_rm'][x] or popu1['h_p_cost'][i][x] > 1.0 or popu1['h_m_cost'][i][x] > 1.0):
                print popu1['v_p_cost'][i][x], popu1['v_rp'][x]
                print popu1['v_m_cost'][i][x], popu1['v_rm'][x]
                print popu1['h_p_cost'][i][x]
                print popu1['h_m_cost'][i][x]
                print popu1['population'][i],x,vm_used_id       # 出现2个不同vm放于1个hm,超过hm尺寸 ，[(11, 10), (9, 2), (5, 4), (1, 3), (3, 7), (0, 11), (14, 6), (10, 14), (7, 11), (2, 0)]
                return False
    return True

def mbbode_migration(popu1,size,num_var,f,lambdaa):
    '''
    此处迁移算法思想为两种：1. 完全按照lj版本，为每个容器都计算迁移的VM、以及该vm迁移的hm，此种方式需要计算容器迁移造成的vm源，目标机cpu,mem变化，以及新选择的vm与hm引起的源hm，目标hm资源的变化
                        2. 第二种，为每个容器产生的vm，先计算能否容纳该容器，不可以vm编号改变继续，若可以进一步判断该vm是否已经存在安排，若存在则直接以次安排作为容器安排，否则进行新建
    一旦被迁移概率选中：则进行2个层次的迁移——docker所在的vm编号迁移，vm所在的hm编号迁移(只有两层迁移，才可能调整vm-hm分布方式)
    '''
    # lj版mbbo的迁移，突变逻辑不适合现在的逻辑：1,容器直接放置的vm的编号会重复出现 2,vm-hm的关系应该是多对一的，不是多对多 3. 实际VM-hm变化很复杂倒置很难判断实际发生变化的hm编号
    # 因此，应该放弃进行vm,hm同时迁移，突变的想法; 先安排所有容器的vm迁移，整体完成后再进行所有占用的vm到hm的映射
    # for i in xrange(0,size):
    #     for j in xrange(0,num_var):
    #         rand_sum = random.random()
    #         lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
    #         if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
    #             index1 = random.randint(0, size-1)
    #             index2 = random.randint(0, size-1)
    #             while(index1 == index2):
    #                 index2 = random.randint(0, size-1)
    #             #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
    #             tmp_v_id = abs(int(popu1['population'][i][j][0] + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] + 0.5)) % num_var)
    #             tmp_h_id = abs(int(popu1['population'][i][j][1] + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] + 0.5)) % num_var)
    #             while(True):
    #                 cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
    #                 mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
    #                 cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
    #                 mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
    #                 print tmp_v_id,cpu_tmp_v,mem_tmp_v,tmp_h_id,cpu_tmp_h,mem_tmp_h
    #                 if(cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0 and cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):                  # 若该vm重新安排至pm(tmp_position)后，cpu,mem资源使用量不超标，则进行替换;否则继续循环查找可容纳该vm的新pm
    #                     origin_v_id = popu1['population'][i][j][0]
    #                     origin_h_id = popu1['population'][i][j][1]
    #                     popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
    #                     popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
    #                     popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
    #                     popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
    #                     popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
    #                     #
    #                     popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
    #                     popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
    #                     popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
    #                     popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
    #                     print "have migrate successfully!,i=%s,j=%s\n" %(i,j)
    #                     break
    #                 else:
    #                     tmp_v_id = (tmp_v_id + 1) % num_var
    #                     tmp_h_id = (tmp_h_id + 1) % num_var
    
    # 与下面这个几乎一样的
    # for i in xrange(size):
    #     vm_used_id = dict(popu1['population'][i])
    #     for j in xrange(num_var):
    #         rand_sum = random.random()
    #         lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
    #         if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
    #             index1 = random.randint(0, size-1)
    #             index2 = random.randint(0, size-1)
    #             while(index1 == index2):
    #                 index2 = random.randint(0, size-1)
    #             #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
    #             tmp_v_id = abs(int(popu1['population'][i][j][0] + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] + 0.5)) % num_var)
    #             tmp_h_id = abs(int(popu1['population'][i][j][1] + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] + 0.5)) % num_var)
    #             flag = True
    #             while(flag):
    #                 cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
    #                 mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
    #                 if (tmp_v_id not in vm_used_id):                                               # 为容器新产生的vm，直接进行资源约束判断
    #                     cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
    #                     mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
    #                     print tmp_v_id,'not in',tmp_h_id,cpu_tmp_v,mem_tmp_v,cpu_tmp_h,mem_tmp_h,i,j
    #                     if(cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0 and cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):
    #                         origin_v_id = popu1['population'][i][j][0]                                      # 若满足资源限制，则更改vm,hm实际资源占用数据
    #                         origin_h_id = popu1['population'][i][j][1]
    #                         popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
    #                         popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
    #                         popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
    #                         popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
    #                         popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
    #                         #
    #                         popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
    #                         popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
    #                         #popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
    #                         #popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
    #                         vm_used_id[tmp_v_id] = tmp_h_id                                                 # 并添加该组vm-hm映射到字典中
    #                         flag = False                                                                    # 设置跳出while循环标志
    #                         print "have migrate successfully!,i=%s,j=%s\n" %(i,j)
    #                     else:
    #                         tmp_v_id = (tmp_v_id + 1) % num_var                                             # 若不满足，则生成新的vm,hm重新进行while循环
    #                         tmp_h_id = (tmp_h_id + 1) % num_var
    #                 elif (tmp_v_id in vm_used_id):                                        # 若为容器进化的产生的vm，已经存在
    #                     print tmp_v_id,'in',vm_used_id[tmp_v_id],cpu_tmp_v,mem_tmp_v,i,j
    #                     if (cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):        # 并且满足资源约束，则直接将该vm与其对应的hm赋给容器
    #                         origin_v_id = popu1['population'][i][j][0]
    #                         popu1['population'][i][j] = [tmp_v_id,vm_used_id[tmp_v_id]]
    #                         popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
    #                         popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
    #                         popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
    #                         popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
    #                         flag = False                                                              # 并设置while 循环标志为False
    #                         print "just find a serving vm-hm"
    #                     else:                                                                          # 若不满足，则生成新的vm,hm重新进行while循环
    #                         tmp_v_id = (tmp_v_id + 1) % num_var
    #                         tmp_h_id = (tmp_h_id + 1) % num_var

    for i in xrange(size):
        vm_used_id = dict(popu1['population'][i])
        print vm_used_id
        print popu1['h_p_cost'][i]
        for j in xrange(num_var):
            rand_sum = random.random()
            lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
            if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
                index1 = random.randint(0, size-1)
                index2 = random.randint(0, size-1)
                while(index1 == index2):
                    index2 = random.randint(0, size-1)
                #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
                tmp_v_id = abs(int(popu1['population'][i][j][0] + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] + 0.5)) % num_var)
                tmp_h_id = abs(int(popu1['population'][i][j][1] + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] + 0.5)) % num_var)
                cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
                mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
                print tmp_v_id,tmp_h_id,cpu_tmp_v,mem_tmp_v
                if (cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):       # 判断vm层资源约束
                    flag = True
                    while(flag):
                        if (tmp_v_id not in vm_used_id):                                               # 为容器新产生的vm，直接进行资源约束判断
                            cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
                            mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
                            print 'no, not in',cpu_tmp_h,mem_tmp_h
                            if(cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0):                                 # 若满足资源限制，则更改vm,hm实际资源占用数据
                                origin_v_id, origin_h_id = popu1['population'][i][j][0], popu1['population'][i][j][1]
                                popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
                                popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                                popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
                                popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
                                popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
                                #
                                popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
                                popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
                                #popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
                                #popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
                                vm_used_id[tmp_v_id] = tmp_h_id                                                 # 并添加该组vm-hm映射到字典中
                                flag = False                                                                    # 设置跳出while循环标志
                                print "%s,%s have migrate successfully!,vm_used_id = %s, h_p_cost = %s \n" %(i,j,vm_used_id,popu1['h_m_cost'][i])
                            else:
                                tmp_v_id = (tmp_v_id + 1) % num_var                                             # 若不满足，则生成新的vm,hm重新进行while循环
                                tmp_h_id = (tmp_h_id + 1) % num_var
                        elif (tmp_v_id in vm_used_id):                                        # 若为容器进化的产生的vm，已经存在
                            #if (cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):        # 并且满足资源约束，则直接将该vm与其对应的hm赋给容器
                            print 'yes, in', popu1['h_p_cost'][i][vm_used_id[tmp_v_id]]
                            origin_v_id = popu1['population'][i][j][0]
                            popu1['population'][i][j] = [tmp_v_id,vm_used_id[tmp_v_id]]
                            popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
                            popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
                            popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
                            popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
                            flag = False                                                              # 并设置while 循环标志为False
                            print "just find a serving vm-hm"
                else:
                    tmp_v_id = (tmp_v_id + 1) % num_var


    # for i in xrange(size):
    #     vm_used_id = dict(popu1['population'][i])
    #     for j in xrange(num_var):
    #         rand_sum = random.random()
    #         lambda_scale = (lambdaa[i] - lambdaa[0]) / (lambdaa[size-1] - lambdaa[0])   # 标准化迁入率lambda_scale，即该chrom被选为迁入chrom的概率
    #         if(rand_sum < lambda_scale):                                            # 被选为迁入chrom中的第j元素有rand_sum概率被选为迁出chrom随机生成的SIV替换
    #             index1 = random.randint(0, size-1)
    #             index2 = random.randint(0, size-1)
    #             while(index1 == index2):
    #                 index2 = random.randint(0, size-1)
    #             #实现差分迁移，计算被迁入率选中的chrom中，随机选中的SIV将被差分迁移引入的新SIV值（该位置vm将被重新安排的HM标号）
    #             tmp_v_id = abs(int(popu1['population'][i][j][0] + f*(popu1['population'][i][j][0]-popu1['population'][index1][j][0]) + f*(popu1['population'][index1][j][0]-popu1['population'][index2][j][0] + 0.5)) % num_var)
    #             tmp_h_id = abs(int(popu1['population'][i][j][1] + f*(popu1['population'][i][j][1]-popu1['population'][index1][j][1]) + f*(popu1['population'][index1][j][1]-popu1['population'][index2][j][1] + 0.5)) % num_var)
    #             flag = True
    #             while(flag):
    #                 cpu_tmp_v = popu1['v_p_cost'][i][tmp_v_id] + popu1['c_rp'][j]
    #                 mem_tmp_v = popu1['v_m_cost'][i][tmp_v_id] + popu1['c_rm'][j]
    #                 if (tmp_v_id not in vm_used_id):                                               # 为容器新产生的vm，直接进行资源约束判断
    #                     cpu_tmp_h = popu1['h_p_cost'][i][tmp_h_id] + popu1['v_rp'][tmp_v_id]
    #                     mem_tmp_h = popu1['h_m_cost'][i][tmp_h_id] + popu1['v_rm'][tmp_v_id]
    #                     print tmp_v_id,'not in',tmp_h_id,cpu_tmp_v,mem_tmp_v,cpu_tmp_h,mem_tmp_h,i,j
    #                     if(cpu_tmp_h <= 1.0 and mem_tmp_h <= 1.0 and cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):
    #                         origin_v_id = popu1['population'][i][j][0]                                      # 若满足资源限制，则更改vm,hm实际资源占用数据
    #                         origin_h_id = popu1['population'][i][j][1]
    #                         popu1['population'][i][j] = [tmp_v_id,tmp_h_id]
    #                         popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
    #                         popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
    #                         popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
    #                         popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
    #                         #
    #                         popu1['h_p_cost'][i][tmp_h_id] = cpu_tmp_h
    #                         popu1['h_m_cost'][i][tmp_h_id] = mem_tmp_h
    #                         popu1['h_p_cost'][i][origin_h_id] -= popu1['v_rp'][tmp_v_id]
    #                         popu1['h_m_cost'][i][origin_h_id] -= popu1['v_rm'][tmp_v_id]
    #                         vm_used_id[tmp_v_id] = tmp_h_id                                                 # 并添加该组vm-hm映射到字典中
    #                         flag = False                                                                    # 设置跳出while循环标志
    #                         print "have migrate successfully!,i=%s,j=%s\n" %(i,j)
    #                     else:
    #                         tmp_v_id = (tmp_v_id + 1) % num_var                                             # 若不满足，则生成新的vm,hm重新进行while循环
    #                         tmp_h_id = (tmp_h_id + 1) % num_var
    #                 elif (tmp_v_id in vm_used_id):                                        # 若为容器进化的产生的vm，已经存在
    #                     print tmp_v_id,'in',vm_used_id[tmp_v_id],cpu_tmp_v,mem_tmp_v,i,j
    #                     if (cpu_tmp_v <= popu1['v_rp'][tmp_v_id] and mem_tmp_v <= popu1['v_rm'][tmp_v_id]):        # 并且满足资源约束，则直接将该vm与其对应的hm赋给容器
    #                         origin_v_id = popu1['population'][i][j][0]
    #                         popu1['population'][i][j] = [tmp_v_id,vm_used_id[tmp_v_id]]
    #                         popu1['v_p_cost'][i][tmp_v_id] = cpu_tmp_v
    #                         popu1['v_m_cost'][i][tmp_v_id] = mem_tmp_v
    #                         popu1['v_p_cost'][i][origin_v_id] -= popu1['c_rp'][j]
    #                         popu1['v_m_cost'][i][origin_v_id] -= popu1['c_rm'][j]
    #                         flag = False                                                              # 并设置while 循环标志为False
    #                         print "just find a serving vm-hm"
    #                     else:                                                                          # 若不满足，则生成新的vm,hm重新进行while循环
    #                         tmp_v_id = (tmp_v_id + 1) % num_var
    #                         tmp_h_id = (tmp_h_id + 1) % num_var
    # 尽量清零
    for i in xrange(size):
        for j in xrange(num_var):
            if(popu1['v_p_cost'][i][j] < 0.0001):
                popu1['v_p_cost'][i][j] = 0
            elif(popu1['v_m_cost'][i][j] < 0.0001):
                popu1['v_m_cost'][i][j] = 0
            elif(popu1['h_p_cost'][i][j] < 0.0001):
                popu1['h_p_cost'][i][j] = 0
            elif(popu1['h_m_cost'][i][j] < 0.0001):
                popu1['h_m_cost'][i][j] = 0
    # 有效性检测
    if checkeffective(popu1,size,num_var):
        #print "it's effective, population = %s" %popu1['population']
        print 'it is effective'
        return popu1
    else:
        sys.exit("not effective in compute mbbode_migration")

if __name__ == '__main__':
    lambdaa = [0.785887260776948, 0.9449569463147377, 1.0]
    print mbbode_migration(popu1,3,15,0.6,lambdaa)
