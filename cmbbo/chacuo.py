进入 init_Docker
[0.46143501062511305, 0.3837410591302293, 0.10314288390788534, 0.05750704968243808, 0.10050669240419341, 0.4169841326992089, 0.0841912744860075, 0.3783048050457624, 0.3530010163231708, 0.28083475163929, 0.07813743841557197, 0.3191346305961524, 0.49762283386706635, 0.18347841234413953, 0.4779282801585459, 0.14976181247470638, 0.49733983068279586, 0.44445098346968015, 0.3682670875556045, 0.39568249969754066, 0.39139119807664685, 0.4302271394685114, 0.331264766543538, 0.46084074149400794, 0.46091812595580206, 0.1724490894151136, 0.2103723478269961, 0.014328184571816116, 0.18669714652898228, 0.0945056409857396, 0.14298549812204014, 0.39723642829925004, 0.12273407364251371, 0.2973929654838172, 0.32887410159010216, 0.0937522368415254, 0.06569421500321859, 0.31117439541854236, 0.28172909967794324, 0.19230189887968135, 0.021895284572048035, 0.42096957846723954, 0.20463934797364502, 0.3172212210207901, 0.1161201418283952, 0.08717991883537013, 0.3956235065396091, 0.48097643034503584, 0.3396808233050438, 0.12173239112990047] [0.3055695577392985, 0.3197790196045699, 0.18771698493570818, 0.001279596534413091, 0.10259716692652684, 0.49993739508456836, 0.21565294159951864, 0.2746944862135556, 0.3587570369682309, 0.48433055764414157, 0.134962246234688, 0.28877433720032986, 0.32364331936410207, 0.19997557353368386, 0.43686245364253334, 0.2133021003254714, 0.31626214848990264, 0.3244069535712246, 0.273384297823132, 0.3790144536328914, 0.44109919184775015, 0.2807228248597049, 0.27628068306793196, 0.4738620484615105, 0.30602464448640077, 0.06676058922011127, 0.22357276864072687, 0.034911330866568085, 0.041081983725013815, 0.09287824369819131, 0.19530955684973317, 0.44254155895909403, 0.23845216358743854, 0.3085251195674721, 0.32695416813079026, 0.1358775001751132, 0.05809947654802919, 0.45056675598813456, 0.31999059862808676, 0.15109346307752872, 0.013038046268100068, 0.3101784481486248, 0.025879026144808748, 0.28319745342953645, 0.08362130497712456, 0.02137271466287402, 0.349259229065907, 0.48712840088391596, 0.36366719551206056, 0.14563466021170235]
进入init_VM
[0.5, 0.7, 1.0, 0.3, 0.3, 0.5, 0.7, 1.0, 0.5, 1.0, 0.5, 0.7, 0.5, 0.3, 0.7, 0.3, 0.5, 0.7, 0.7, 1.0, 0.5, 0.5, 0.7, 0.7, 1.0, 0.5, 0.5, 0.7, 1.0, 0.5, 0.7, 0.5, 1.0, 0.5, 0.7, 1.0, 0.7, 0.5, 1.0, 0.7, 0.3, 0.7, 0.5, 1.0, 0.7, 0.5, 0.7, 0.5, 1.0, 1.0] [0.5, 1.0, 1.0, 0.7, 1.0, 0.7, 0.7, 0.7, 0.7, 0.5, 0.5, 0.5, 0.7, 0.3, 0.7, 0.5, 1.0, 0.7, 0.3, 1.0, 0.7, 0.3, 1.0, 0.5, 0.5, 0.7, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.7, 0.5, 1.0, 0.5, 0.7, 0.7, 0.3, 0.5, 0.5, 0.5, 0.7, 0.5, 1.0, 0.7, 1.0, 0.7, 0.5]
开始主流程
进入make_population
进入initialize_population
进入check_effective
Initailization population is effective
进入mbbode_cost
进入check_effective
进入mbbode_rank
[1, 6, 10, 12, 11] 0
上代结果： 49999950.0 49999950.0 49999950.0 3250
本代结果替代后： 15760.8829213 0.778228993752 783583.280416 0.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[5, 42], [34, 12], [33, 13], [42, 3], [25, 18], [26, 46], [12, 27], [27, 45], [47, 19], [23, 33], [43, 38], [28, 49], [36, 5], [32, 4], [32, 4], [6, 6], [9, 23], [46, 47], [17, 17], [25, 18], [8, 39], [2, 40], [37, 2], [6, 6], [14, 24], [17, 17], [14, 24], [4, 32], [43, 38], [35, 15], [28, 49], [22, 35], [48, 34], [2, 40], [0, 37], [40, 20], [35, 15], [42, 3], [34, 27], [16, 25], [33, 13], [48, 34], [20, 16], [38, 30], [7, 26], [37, 2], [42, 14], [44, 43], [33, 13], [31, 0]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 34, v_p_cost = 0.665470158808, v_rp = 0.7, v_m_cost = 0.639769618233, v_rm = 0.5
取出38前有这些容器： [1, 38]
取出38后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 0.764304951641, v_rp = 0.5, v_m_cost = 0.801105581588, v_rm = 0.5
取出3前有这些容器： [3, 37, 46]
取出3后有： [37, 46] v_p_cost=0.706797901958, v_rp = 0.5, v_m_cost = 0.799825985054, v_rm = 0.5
取出37前有这些容器： [37, 46]
取出37后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.5
修改hm过载  h_id = 32, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 49]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.546636447352, v_rp = 0.5, v_m_cost = 0.535669479645, v_rm = 0.5
取出2前有这些容器： [2, 32, 42, 44]
取出2后有： [32, 42, 44] v_p_cost=0.443493563445, v_rp = 0.5, v_m_cost = 0.347952494709, v_rm = 0.5
修改vm超载的情况 v_id = 9, v_p_cost = 0.646095322611, v_rp = 1.0, v_m_cost = 0.61015162156, v_rm = 0.5
取出43前有这些容器： [34, 43]
取出43后有： [34] v_p_cost=0.32887410159, v_rp = 1.0, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 10, v_p_cost = 0.857058517165, v_rp = 0.5, v_m_cost = 0.654828786805, v_rm = 0.5
取出46前有这些容器： [0, 46]
取出46后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.691342817645, v_rp = 0.3, v_m_cost = 0.844367191147, v_rm = 0.5
取出3前有这些容器： [3, 8, 9]
取出3后有： [8, 9] v_p_cost=0.633835767962, v_rp = 0.3, v_m_cost = 0.843087594612, v_rm = 0.5
取出9前有这些容器： [8, 9]
取出9后有： [8] v_p_cost=0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.828604597226, v_rp = 0.7, v_m_cost = 0.592542831558, v_rm = 0.5
取出22前有这些容器： [16, 22]
取出22后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.792150825764, v_rp = 1.0, v_m_cost = 0.937695156872, v_rm = 0.7
取出37前有这些容器： [37, 47]
取出37后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 6, h_p_cost = 1.7, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [5, 8, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[0.7, 0.7, 0.5]
5
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 17, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 38]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
11
修改hm过载  h_id = 28, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 14]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
14
修改hm过载  h_id = 33, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [31, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
31
修改hm过载  h_id = 43, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 25]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 45, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 48]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
7
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 1.06993742722, v_rp = 0.3, v_m_cost = 1.37175976727, v_rm = 0.7
取出9前有这些容器： [9, 14, 37]
取出9后有： [14, 37] v_p_cost=0.789102675577, v_rp = 0.3, v_m_cost = 0.887429209631, v_rm = 0.7
取出37前有这些容器： [14, 37]
取出37后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.7
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 0.919669775248, v_rp = 1.0, v_m_cost = 0.857692120697, v_rm = 0.7
取出15前有这些容器： [15, 21, 48]
取出15后有： [21, 48] v_p_cost=0.769907962774, v_rp = 1.0, v_m_cost = 0.644390020372, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.679608611288, v_rp = 0.7, v_m_cost = 0.651831969526, v_rm = 0.5
取出4前有这些容器： [4, 13, 46]
取出4后有： [13, 46] v_p_cost=0.579101918884, v_rp = 0.7, v_m_cost = 0.5492348026, v_rm = 0.5
取出13前有这些容器： [13, 46]
取出13后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.812718071025, v_rp = 0.7, v_m_cost = 0.597791251394, v_rm = 0.3
取出18前有这些容器： [17, 18]
取出18后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 32, v_p_cost = 0.941894556301, v_rp = 1.0, v_m_cost = 0.79315304537, v_rm = 0.7
取出24前有这些容器： [24, 47]
取出24后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 6, h_p_cost = 2.5, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [28, 37, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0],mem尺寸[0.5, 0.7, 0.7]
37
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
28
修改hm过载  h_id = 10, h_p_cost = 1.4, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [1, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.3]
1
修改hm过载  h_id = 12, h_p_cost = 1.4, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 17]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.7]
14
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 30, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 34, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 39, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 7]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 1.0]
0
修改hm过载  h_id = 44, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 49, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
30
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.873316588506, v_rp = 0.3, v_m_cost = 0.927271333322, v_rm = 0.7
取出3前有这些容器： [3, 19, 32, 33]
取出3后有： [19, 32, 33] v_p_cost=0.815809538824, v_rp = 0.3, v_m_cost = 0.925991736788, v_rm = 0.7
取出32前有这些容器： [19, 32, 33]
取出32后有： [19, 33] v_p_cost=0.693075465181, v_rp = 0.3, v_m_cost = 0.6875395732, v_rm = 0.7
取出33前有这些容器： [19, 33]
取出33后有： [19] v_p_cost=0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.7
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.598129526271, v_rp = 0.3, v_m_cost = 0.426240486291, v_rm = 1.0
取出4前有这些容器： [4, 12]
取出4后有： [12] v_p_cost=0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 1.0
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.583693096956, v_rp = 0.5, v_m_cost = 0.592192654925, v_rm = 0.7
取出39前有这些容器： [20, 39]
取出39后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.281729099678, v_rp = 0.3, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 17, v_p_cost = 0.822494233833, v_rp = 0.7, v_m_cost = 0.682729886267, v_rm = 0.7
取出40前有这些容器： [24, 40, 48]
取出40后有： [24, 48] v_p_cost=0.800598949261, v_rp = 0.7, v_m_cost = 0.669691839998, v_rm = 0.7
取出48前有这些容器： [24, 48]
取出48后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 0.813968198599, v_rp = 1.0, v_m_cost = 0.600501844464, v_rm = 0.5
取出1前有这些容器： [1, 21]
取出1后有： [21] v_p_cost=0.430227139469, v_rp = 1.0, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.460206719143, v_rp = 0.7, v_m_cost = 0.478507010279, v_rm = 0.3
取出30前有这些容器： [30, 43]
取出30后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.3
修改vm超载的情况 v_id = 30, v_p_cost = 0.901946008812, v_rp = 0.7, v_m_cost = 0.797306849033, v_rm = 0.7
取出41前有这些容器： [41, 47]
取出41后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 33, v_p_cost = 0.678071179939, v_rp = 0.5, v_m_cost = 0.926872116603, v_rm = 0.7
取出9前有这些容器： [9, 31]
取出9后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 36, v_p_cost = 0.986885116363, v_rp = 0.7, v_m_cost = 0.731087183928, v_rm = 0.5
取出25前有这些容器： [0, 8, 25]
取出25后有： [0, 8] v_p_cost=0.814436026948, v_rp = 0.7, v_m_cost = 0.664326594708, v_rm = 0.5
取出8前有这些容器： [0, 8]
取出8后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.55534638248, v_rp = 0.5, v_m_cost = 0.56674029216, v_rm = 1.0
取出29前有这些容器： [23, 29]
取出29后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 1.0
修改vm超载的情况 v_id = 47, v_p_cost = 1.54547209338, v_rp = 0.5, v_m_cost = 1.18168848087, v_rm = 1.0
取出28前有这些容器： [5, 16, 17, 28]
取出28后有： [5, 16, 17] v_p_cost=1.35877494685, v_rp = 0.5, v_m_cost = 1.14060649715, v_rm = 1.0
取出5前有这些容器： [5, 16, 17]
取出5后有： [16, 17] v_p_cost=0.941790814152, v_rp = 0.5, v_m_cost = 0.640669102061, v_rm = 1.0
取出17前有这些容器： [16, 17]
取出17后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 1.0
修改hm过载  h_id = 10, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 10]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.5]
10
修改hm过载  h_id = 11, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
33
修改hm过载  h_id = 13, h_p_cost = 1.3, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 21, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [31, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
31
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 39, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 41, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 4]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 43, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 44, h_p_cost = 1.4, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [22, 27]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.3]
22
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [41, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 47, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 49, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.38374105913, v_rp = 0.3, v_m_cost = 0.319779019605, v_rm = 1.0
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 13, v_p_cost = 0.331264766544, v_rp = 0.3, v_m_cost = 0.276280683068, v_rm = 0.3
取出22前有这些容器： [22]
取出22后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 1.08446666326, v_rp = 0.3, v_m_cost = 1.12863876505, v_rm = 0.5
取出33前有这些容器： [19, 20, 33]
取出33后有： [19, 20] v_p_cost=0.787073697774, v_rp = 0.3, v_m_cost = 0.820113645481, v_rm = 0.5
取出20前有这些容器： [19, 20]
取出20后有： [19] v_p_cost=0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.5
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.3
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 1.18899017127, v_rp = 0.7, v_m_cost = 1.20191583615, v_rm = 1.0
取出9前有这些容器： [9, 14, 21]
取出9后有： [14, 21] v_p_cost=0.908155419627, v_rp = 0.7, v_m_cost = 0.717585278502, v_rm = 1.0
取出21前有这些容器： [14, 21]
取出21后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 1.0
修改vm超载的情况 v_id = 27, v_p_cost = 0.32887410159, v_rp = 0.7, v_m_cost = 0.326954168131, v_rm = 0.3
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 1.43941364802, v_rp = 0.5, v_m_cost = 0.964312421425, v_rm = 0.5
取出17前有这些容器： [12, 16, 17]
取出17后有： [12, 16] v_p_cost=0.99496266455, v_rp = 0.5, v_m_cost = 0.639905467854, v_rm = 0.5
取出16前有这些容器： [12, 16]
取出16后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.71284472756, v_rp = 0.7, v_m_cost = 0.632456682495, v_rm = 0.3
取出43前有这些容器： [43, 46]
取出43后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.3
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.634727567407, v_rp = 0.5, v_m_cost = 0.730729359507, v_rm = 1.0
取出29前有这些容器： [29, 30, 31]
取出29后有： [30, 31] v_p_cost=0.540221926421, v_rp = 0.5, v_m_cost = 0.637851115809, v_rm = 1.0
取出30前有这些容器： [30, 31]
取出30后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 1.0
修改hm过载  h_id = 9, h_p_cost = 1.4, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [36, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.3]
36
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [10, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.3]
10
修改hm过载  h_id = 14, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [35, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 16, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 32]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
2
修改hm过载  h_id = 25, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 31, 44]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.7],mem尺寸[0.5, 0.5, 0.5]
15
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 28, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 34, h_p_cost = 0.6, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 4]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 39, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 5]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 44, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
22
进入mbbode_rank
[7, 5, 10, 9, 9] 1
上代结果： 15760.8829213 0.778228993752 783583.280416 0.0
执行全局精英解替换： 15760.8829213 0.778228993752 783583.280416 0.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[5, 42], [34, 12], [33, 13], [42, 3], [25, 18], [26, 46], [12, 27], [27, 45], [47, 19], [23, 33], [43, 38], [28, 49], [36, 5], [32, 4], [32, 4], [6, 6], [9, 23], [46, 47], [17, 17], [25, 18], [8, 39], [2, 40], [37, 2], [6, 6], [22, 38], [17, 17], [14, 24], [4, 32], [43, 38], [35, 15], [28, 49], [22, 35], [48, 34], [2, 40], [0, 37], [40, 20], [35, 15], [42, 3], [35, 15], [16, 25], [33, 13], [48, 34], [20, 16], [38, 30], [7, 26], [37, 2], [49, 29], [44, 43], [33, 13], [31, 0]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 22, v_p_cost = 0.858154554255, v_rp = 0.7, v_m_cost = 0.748566203445, v_rm = 1.0
取出31前有这些容器： [24, 31]
取出31后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 1.0
修改hm过载  h_id = 32, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 19]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 38, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.7]
22
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.941365105392, v_rp = 0.5, v_m_cost = 0.839601234423, v_rm = 0.5
取出44前有这些容器： [28, 32, 37, 42, 44]
取出44后有： [28, 32, 37, 42] v_p_cost=0.825244963564, v_rp = 0.5, v_m_cost = 0.755979929445, v_rm = 0.5
取出32前有这些容器： [28, 32, 37, 42]
取出32后有： [28, 37, 42] v_p_cost=0.702510889921, v_rp = 0.5, v_m_cost = 0.517527765858, v_rm = 0.5
取出28前有这些容器： [28, 37, 42]
取出28后有： [37, 42] v_p_cost=0.515813743392, v_rp = 0.5, v_m_cost = 0.476445782133, v_rm = 0.5
取出42前有这些容器： [37, 42]
取出42后有： [37] v_p_cost=0.311174395419, v_rp = 0.5, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 11, v_p_cost = 0.893305333565, v_rp = 0.7, v_m_cost = 0.702657772997, v_rm = 0.5
取出19前有这些容器： [12, 19]
取出19后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.331264766544, v_rp = 0.3, v_m_cost = 0.276280683068, v_rm = 0.3
取出22前有这些容器： [22]
取出22后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.5
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 0.485896839062, v_rp = 1.0, v_m_cost = 0.533977435546, v_rm = 0.5
取出29前有这些容器： [20, 29]
取出29后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.280834751639, v_rp = 0.7, v_m_cost = 0.484330557644, v_rm = 0.3
取出9前有这些容器： [9]
取出9后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 34, v_p_cost = 0.789236666023, v_rp = 0.7, v_m_cost = 0.583562745972, v_rm = 0.5
取出18前有这些容器： [18, 41]
取出18后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.3
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 44, v_p_cost = 0.744903230704, v_rp = 0.7, v_m_cost = 0.608597384947, v_rm = 0.5
取出4前有这些容器： [4, 13, 24]
取出4后有： [13, 24] v_p_cost=0.6443965383, v_rp = 0.7, v_m_cost = 0.50600021802, v_rm = 0.5
取出13前有这些容器： [13, 24]
取出13后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改hm过载  h_id = 7, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 12, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 27]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
20
修改hm过载  h_id = 42, h_p_cost = 2.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [19, 35]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 1.0]
19
修改hm过载  h_id = 43, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [25, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
25
修改hm过载  h_id = 46, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.935168390621, v_rp = 0.3, v_m_cost = 0.777614884404, v_rm = 0.7
取出30前有这些容器： [22, 24, 30]
取出30后有： [22, 24] v_p_cost=0.792182892499, v_rp = 0.3, v_m_cost = 0.582305327554, v_rm = 0.7
取出22前有这些容器： [22, 24]
取出22后有： [24] v_p_cost=0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 0.7
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.405636343702, v_rp = 0.7, v_m_cost = 0.332817065873, v_rm = 0.3
取出40前有这些容器： [1, 40]
取出40后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.3
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.761811181984, v_rp = 0.5, v_m_cost = 0.971458958528, v_rm = 0.7
取出9前有这些容器： [9, 47]
取出9后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 36, v_p_cost = 1.14504426976, v_rp = 0.7, v_m_cost = 0.948511615693, v_rm = 0.5
取出11前有这些容器： [11, 19, 21]
取出11后有： [19, 21] v_p_cost=0.825909639166, v_rp = 0.7, v_m_cost = 0.659737278493, v_rm = 0.5
取出19前有这些容器： [19, 21]
取出19后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 38, v_p_cost = 1.13895520682, v_rp = 1.0, v_m_cost = 0.948540129874, v_rm = 0.7
取出48前有这些容器： [7, 41, 48]
取出48后有： [7, 41] v_p_cost=0.799274383513, v_rp = 1.0, v_m_cost = 0.584872934362, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.984169189811, v_rp = 0.3, v_m_cost = 1.06279651224, v_rm = 0.5
取出32前有这些容器： [5, 17, 32]
取出32后有： [5, 17] v_p_cost=0.861435116169, v_rp = 0.3, v_m_cost = 0.824344348656, v_rm = 0.5
取出5前有这些容器： [5, 17]
取出5后有： [17] v_p_cost=0.44445098347, v_rp = 0.3, v_m_cost = 0.324406953571, v_rm = 0.5
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -1.11022302463e-16, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.966460988834, v_rp = 1.0, v_m_cost = 0.758640490435, v_rm = 0.7
取出44前有这些容器： [8, 16, 44]
取出44后有： [8, 16] v_p_cost=0.850340847006, v_rp = 1.0, v_m_cost = 0.675019185458, v_rm = 0.7
修改hm过载  h_id = 1, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [24, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
24
修改hm过载  h_id = 2, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
18
修改hm过载  h_id = 4, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 8, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 28, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 34, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
12
修改hm过载  h_id = 38, h_p_cost = 1.3, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 38]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 40, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 15]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 0.5]
15
修改hm过载  h_id = 44, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 8]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
8
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.934054776475, v_rp = 0.7, v_m_cost = 0.941448665208, v_rm = 1.0
取出39前有这些容器： [9, 24, 39]
取出39后有： [9, 24] v_p_cost=0.741752877595, v_rp = 0.7, v_m_cost = 0.790355202131, v_rm = 1.0
取出9前有这些容器： [9, 24]
取出9后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 1.0
修改vm超载的情况 v_id = 3, v_p_cost = 0.478571116912, v_rp = 0.3, v_m_cost = 0.462471906511, v_rm = 0.7
取出45前有这些容器： [20, 45]
取出45后有： [20] v_p_cost=0.391391198077, v_rp = 0.3, v_m_cost = 0.441099191848, v_rm = 0.7
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.461435010625, v_rp = 0.3, v_m_cost = 0.305569557739, v_rm = 1.0
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 10, v_p_cost = 1.03682201245, v_rp = 0.5, v_m_cost = 0.964005661466, v_rm = 0.5
取出34前有这些容器： [18, 34, 48]
取出34后有： [18, 48] v_p_cost=0.707947910861, v_rp = 0.5, v_m_cost = 0.637051493335, v_rm = 0.5
取出48前有这些容器： [18, 48]
取出48后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.297392965484, v_rp = 0.3, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 0.778061962515, v_rp = 0.7, v_m_cost = 0.757059501891, v_rm = 1.0
取出43前有这些容器： [23, 43]
取出43后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 1.0
修改vm超载的情况 v_id = 23, v_p_cost = 0.874678122938, v_rp = 0.7, v_m_cost = 0.605129778431, v_rm = 0.5
取出21前有这些容器： [17, 21]
取出21后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 26, v_p_cost = 0.974624496996, v_rp = 0.5, v_m_cost = 0.884573458198, v_rm = 0.7
取出42前有这些容器： [5, 8, 42]
取出42后有： [5, 8] v_p_cost=0.769985149022, v_rp = 0.5, v_m_cost = 0.858694432053, v_rm = 0.7
取出8前有这些容器： [5, 8]
取出8后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.3
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.594113406957, v_rp = 0.5, v_m_cost = 0.543351788245, v_rm = 0.5
取出26前有这些容器： [1, 26]
取出26后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 43, v_p_cost = 0.821393914069, v_rp = 1.0, v_m_cost = 0.718418155832, v_rm = 0.7
取出29前有这些容器： [22, 29, 46]
取出29后有： [22, 46] v_p_cost=0.726888273083, v_rp = 1.0, v_m_cost = 0.625539912134, v_rm = 0.7
修改hm过载  h_id = 4, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [39, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
39
修改hm过载  h_id = 6, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [21, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.3, 1.0]
21
修改hm过载  h_id = 16, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 17, h_p_cost = 1.7, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [5, 6, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.5],mem尺寸[0.7, 0.7, 0.5]
5
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 20, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 23, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 26, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [24, 33]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.7]
33
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 48, h_p_cost = 3.0, h_m_cost = 2.5
该物理机上放置的虚拟机为：  [4, 18, 43, 49]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 1.0, 1.0],mem尺寸[1.0, 0.3, 0.7, 0.5]
4
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 1.0],mem尺寸[0.3, 0.7, 0.5]
18
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
43
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.877824874193, v_rp = 0.5, v_m_cost = 0.973799443546, v_rm = 0.5
取出5前有这些容器： [5, 23]
取出5后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.732690728523, v_rp = 0.3, v_m_cost = 0.653614898583, v_rm = 0.7
取出27前有这些容器： [27, 33, 41]
取出27后有： [33, 41] v_p_cost=0.718362543951, v_rp = 0.3, v_m_cost = 0.618703567716, v_rm = 0.7
取出33前有这些容器： [33, 41]
取出33后有： [41] v_p_cost=0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.7
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.500037196176, v_rp = 0.5, v_m_cost = 0.420329146425, v_rm = 0.7
取出49前有这些容器： [7, 49]
取出49后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.91737999207, v_rp = 0.3, v_m_cost = 0.765697599916, v_rm = 0.5
取出40前有这些容器： [1, 40, 44, 46]
取出40后有： [1, 44, 46] v_p_cost=0.895484707498, v_rp = 0.3, v_m_cost = 0.752659553648, v_rm = 0.5
取出44前有这些容器： [1, 44, 46]
取出44后有： [1, 46] v_p_cost=0.77936456567, v_rp = 0.3, v_m_cost = 0.66903824867, v_rm = 0.5
取出1前有这些容器： [1, 46]
取出1后有： [46] v_p_cost=0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.5
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 22, v_p_cost = 0.975551114026, v_rp = 0.7, v_m_cost = 0.760505773007, v_rm = 1.0
取出14前有这些容器： [12, 14]
取出14后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 1.0
修改vm超载的情况 v_id = 23, v_p_cost = 0.780569641221, v_rp = 0.7, v_m_cost = 0.59434389494, v_rm = 0.5
取出11前有这些容器： [0, 11]
取出11后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.706856895116, v_rp = 0.7, v_m_cost = 0.829581209621, v_rm = 0.3
取出37前有这些容器： [19, 37]
取出37后有： [19] v_p_cost=0.395682499698, v_rp = 0.7, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 32, v_p_cost = 1.16044998005, v_rp = 1.0, v_m_cost = 0.855689625377, v_rm = 0.7
取出22前有这些容器： [18, 22, 24]
取出22后有： [18, 24] v_p_cost=0.829185213511, v_rp = 1.0, v_m_cost = 0.57940894231, v_rm = 0.7
修改vm超载的情况 v_id = 37, v_p_cost = 0.600482714591, v_rp = 0.5, v_m_cost = 0.503979133426, v_rm = 0.7
取出2前有这些容器： [2, 16]
取出2后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 44, v_p_cost = 0.99406742696, v_rp = 0.7, v_m_cost = 0.788582605928, v_rm = 0.5
取出25前有这些容器： [20, 21, 25]
取出25后有： [20, 21] v_p_cost=0.821618337545, v_rp = 0.7, v_m_cost = 0.721822016707, v_rm = 0.5
取出20前有这些容器： [20, 21]
取出20后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.610603201268, v_rp = 0.5, v_m_cost = 0.646944766759, v_rm = 1.0
取出38前有这些容器： [34, 38]
取出38后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 4, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [16, 19]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 9, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 22]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 1.0]
6
修改hm过载  h_id = 12, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 16, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 25]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 26, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 36]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 28, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
17
修改hm过载  h_id = 34, h_p_cost = 1.4, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [11, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.3]
11
修改hm过载  h_id = 37, h_p_cost = 2.2, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [23, 38, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.5],mem尺寸[0.5, 0.7, 1.0]
45
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
23
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
38
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [26, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
26
修改hm过载  h_id = 47, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 34]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.5]
3
进入mbbode_rank
[8, 4, 11, 4, 13] 1
上代结果： 15760.8829213 0.778228993752 783583.280416 0.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[10, 20], [17, 23], [18, 40], [10, 26], [14, 30], [14, 49], [4, 14], [35, 42], [37, 46], [6, 3], [20, 5], [42, 25], [11, 27], [22, 49], [40, 20], [14, 30], [7, 19], [33, 34], [40, 32], [40, 0], [24, 7], [13, 29], [8, 0], [2, 47], [20, 6], [46, 11], [4, 16], [9, 11], [45, 29], [2, 31], [24, 19], [39, 49], [22, 49], [31, 32], [9, 28], [9, 4], [32, 15], [0, 44], [30, 26], [6, 13], [19, 39], [25, 25], [18, 40], [28, 6], [19, 39], [44, 37], [20, 5], [4, 19], [40, 41], [4, 3]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.897272443788, v_rp = 0.3, v_m_cost = 1.07198877134, v_rm = 1.0
取出6前有这些容器： [6, 26, 47, 49]
取出6后有： [26, 47, 49] v_p_cost=0.813081169302, v_rp = 0.3, v_m_cost = 0.856335829736, v_rm = 1.0
取出49前有这些容器： [26, 47, 49]
取出49后有： [26, 47] v_p_cost=0.691348778172, v_rp = 0.3, v_m_cost = 0.710701169525, v_rm = 1.0
取出26前有这些容器： [26, 47]
取出26后有： [47] v_p_cost=0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 1.0
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=-1.66533453694e-16, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 10, v_p_cost = 0.518942060308, v_rp = 0.5, v_m_cost = 0.306849154274, v_rm = 0.5
取出3前有这些容器： [0, 3]
取出3后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 0.3
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 14, v_p_cost = 0.667252637578, v_rp = 0.7, v_m_cost = 0.815836662337, v_rm = 0.7
取出4前有这些容器： [4, 5, 15]
取出4后有： [5, 15] v_p_cost=0.566745945174, v_rp = 0.7, v_m_cost = 0.71323949541, v_rm = 0.7
取出15前有这些容器： [5, 15]
取出15后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.934679070911, v_rp = 0.5, v_m_cost = 0.790246119787, v_rm = 0.7
取出10前有这些容器： [10, 24, 46]
取出10后有： [24, 46] v_p_cost=0.856541632495, v_rp = 0.5, v_m_cost = 0.655283873552, v_rm = 0.7
取出46前有这些容器： [24, 46]
取出46后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 0.534376696199, v_rp = 1.0, v_m_cost = 0.636408748697, v_rm = 0.5
取出30前有这些容器： [20, 30]
取出30后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 1.58155869072, v_rp = 0.3, v_m_cost = 1.45292840061, v_rm = 0.5
取出48前有这些容器： [14, 18, 19, 48]
取出48后有： [14, 18, 19] v_p_cost=1.24187786741, v_rp = 0.3, v_m_cost = 1.0892612051, v_rm = 0.5
取出18前有这些容器： [14, 18, 19]
取出18后有： [14, 19] v_p_cost=0.873610779856, v_rp = 0.3, v_m_cost = 0.815876907275, v_rm = 0.5
取出19前有这些容器： [14, 19]
取出19后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 1.11022302463e-16, v_rm = 0.5
修改hm过载  h_id = 11, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
46
修改hm过载  h_id = 14, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 25, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
25
修改hm过载  h_id = 29, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 32, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [31, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 34, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [33, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 44, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [37, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
37
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.396941246853, v_rp = 0.3, v_m_cost = 0.176972489222, v_rm = 0.7
取出39前有这些容器： [39, 42]
取出39后有： [42] v_p_cost=0.204639347974, v_rp = 0.3, v_m_cost = 0.0258790261448, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.727620104952, v_rp = 0.7, v_m_cost = 0.589247944427, v_rm = 0.7
取出33前有这些容器： [21, 33]
取出33后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.461435010625, v_rp = 0.3, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.925427413815, v_rp = 0.5, v_m_cost = 0.811535354455, v_rm = 0.7
取出17前有这些容器： [17, 47]
取出17后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.72265596462, v_rp = 0.7, v_m_cost = 0.717379874916, v_rm = 0.3
取出22前有这些容器： [20, 22]
取出22后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.799274383513, v_rp = 0.3, v_m_cost = 0.584872934362, v_rm = 0.5
取出7前有这些容器： [7, 41]
取出7后有： [41] v_p_cost=0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.5
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 1.0002263365, v_rp = 1.0, v_m_cost = 0.948771603606, v_rm = 0.7
取出36前有这些容器： [6, 8, 16, 36]
取出36后有： [6, 8, 16] v_p_cost=0.934532121492, v_rp = 1.0, v_m_cost = 0.890672127058, v_rm = 0.7
取出6前有这些容器： [6, 8, 16]
取出6后有： [8, 16] v_p_cost=0.850340847006, v_rp = 1.0, v_m_cost = 0.675019185458, v_rm = 0.7
修改vm超载的情况 v_id = 49, v_p_cost = 0.758763031798, v_rp = 1.0, v_m_cost = 0.921193011287, v_rm = 0.5
取出9前有这些容器： [9, 14]
取出9后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.5
修改hm过载  h_id = 9, h_p_cost = 2.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [18, 47, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 1.0],mem尺寸[0.3, 1.0, 0.7]
47
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
18
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
48
修改hm过载  h_id = 14, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [42, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 23, h_p_cost = 2.2, h_m_cost = 2.6
该物理机上放置的虚拟机为：  [3, 14, 20, 23]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 0.5, 0.7],mem尺寸[0.7, 0.7, 0.7, 0.5]
3
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.7],mem尺寸[0.7, 0.7, 0.5]
20
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
14
修改hm过载  h_id = 35, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[1.0, 0.5]
40
修改hm过载  h_id = 44, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 25]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 47, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.05433850572, v_rp = 0.5, v_m_cost = 1.07612691236, v_rm = 0.5
取出38前有这些容器： [0, 37, 38]
取出38后有： [0, 37] v_p_cost=0.772609406044, v_rp = 0.5, v_m_cost = 0.756136313727, v_rm = 0.5
取出37前有这些容器： [0, 37]
取出37后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 0.7
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 1.0
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 15, v_p_cost = 0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.5
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.935658082936, v_rp = 0.5, v_m_cost = 1.03231027986, v_rm = 0.3
取出26前有这些容器： [9, 17, 26]
取出26后有： [9, 17] v_p_cost=0.725285735109, v_rp = 0.5, v_m_cost = 0.808737511215, v_rm = 0.3
取出9前有这些容器： [9, 17]
取出9后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.3
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.877824874193, v_rp = 0.5, v_m_cost = 0.973799443546, v_rm = 0.5
取出5前有这些容器： [5, 23]
取出5后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.565001951575, v_rp = 0.5, v_m_cost = 0.315776469939, v_rm = 0.7
取出28前有这些容器： [7, 28]
取出28后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.563601095369, v_rp = 0.7, v_m_cost = 0.672861160999, v_rm = 0.5
取出49前有这些容器： [11, 32, 49]
取出49后有： [11, 32] v_p_cost=0.441868704239, v_rp = 0.7, v_m_cost = 0.527226500788, v_rm = 0.5
取出32前有这些容器： [11, 32]
取出32后有： [11] v_p_cost=0.319134630596, v_rp = 0.7, v_m_cost = 0.2887743372, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.780977487429, v_rp = 0.7, v_m_cost = 0.762320578564, v_rm = 0.3
取出1前有这些容器： [1, 31]
取出1后有： [31] v_p_cost=0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改hm过载  h_id = 2, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [1, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.3]
21
修改hm过载  h_id = 11, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 14, h_p_cost = 2.3, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [3, 7, 28]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0, 1.0],mem尺寸[0.7, 0.7, 0.5]
3
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
7
修改hm过载  h_id = 15, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [47, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 0.7]
47
修改hm过载  h_id = 18, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [33, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 19, h_p_cost = 1.7, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [5, 16, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[0.7, 1.0, 0.7]
5
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 22, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [37, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
37
修改hm过载  h_id = 34, h_p_cost = 1.4, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [18, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.3]
18
修改hm过载  h_id = 36, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[0.5, 0.5]
40
修改hm过载  h_id = 40, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 4]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 1.0]
4
修改hm过载  h_id = 41, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [19, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.5]
34
修改hm过载  h_id = 43, h_p_cost = 2.5, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [2, 25, 35]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0],mem尺寸[1.0, 0.7, 1.0]
25
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 1.0]
2
修改hm过载  h_id = 44, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.789102675577, v_rp = 0.3, v_m_cost = 0.887429209631, v_rm = 0.7
取出37前有这些容器： [14, 37]
取出37后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.7
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.837210294801, v_rp = 1.0, v_m_cost = 1.00930322167, v_rm = 0.5
取出27前有这些容器： [15, 20, 27, 38]
取出27后有： [15, 20, 38] v_p_cost=0.822882110229, v_rp = 1.0, v_m_cost = 0.974391890801, v_rm = 0.5
取出15前有这些容器： [15, 20, 38]
取出15后有： [20, 38] v_p_cost=0.673120297755, v_rp = 1.0, v_m_cost = 0.761089790476, v_rm = 0.5
取出38前有这些容器： [20, 38]
取出38后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 11, v_p_cost = 0.559969630821, v_rp = 0.7, v_m_cost = 0.695246951934, v_rm = 0.5
取出30前有这些容器： [5, 30]
取出30后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.762045864176, v_rp = 0.5, v_m_cost = 0.594473505818, v_rm = 0.7
取出7前有这些容器： [1, 7]
取出7后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.409402204959, v_rp = 0.7, v_m_cost = 0.411242929303, v_rm = 0.3
取出10前有这些容器： [10, 22]
取出10后有： [22] v_p_cost=0.331264766544, v_rp = 0.7, v_m_cost = 0.276280683068, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.681101246211, v_rp = 0.5, v_m_cost = 0.523618892898, v_rm = 0.7
取出13前有这些容器： [12, 13]
取出13后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 29, v_p_cost = 0.780052756552, v_rp = 0.5, v_m_cost = 0.594798981687, v_rm = 0.3
取出11前有这些容器： [11, 24]
取出11后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.3
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 36, v_p_cost = 0.618991856745, v_rp = 0.7, v_m_cost = 0.583787752129, v_rm = 0.5
取出40前有这些容器： [40, 44, 47]
取出40后有： [44, 47] v_p_cost=0.597096572173, v_rp = 0.7, v_m_cost = 0.570749705861, v_rm = 0.5
取出44前有这些容器： [44, 47]
取出44后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.609708853229, v_rp = 0.5, v_m_cost = 0.811284725775, v_rm = 1.0
取出9前有这些容器： [9, 34]
取出9后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 1.0
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [14, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.3]
29
修改hm过载  h_id = 3, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [18, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.3]
21
修改hm过载  h_id = 5, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 10, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
20
修改hm过载  h_id = 32, h_p_cost = 0.8, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 16]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 33, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 37, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 12]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
26
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 41, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 23]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 43, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 44, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 31]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.5]
31
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [30, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
33
进入mbbode_rank
[5, 7, 7, 10, 11] 0
上代结果： 15760.8829213 0.778228993752 783583.280416 0.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[5, 42], [34, 12], [33, 13], [42, 3], [25, 18], [26, 46], [12, 27], [27, 45], [47, 19], [23, 33], [43, 38], [28, 49], [36, 5], [32, 4], [32, 4], [6, 6], [9, 23], [46, 47], [17, 17], [25, 18], [1, 49], [2, 40], [37, 2], [6, 6], [14, 24], [17, 17], [14, 24], [4, 32], [43, 38], [35, 15], [28, 49], [22, 35], [48, 34], [2, 40], [0, 37], [40, 20], [35, 15], [42, 3], [13, 41], [16, 25], [33, 13], [48, 34], [20, 16], [38, 30], [7, 26], [37, 2], [49, 29], [44, 43], [33, 13], [31, 0]] 13 {0: 37, 1: 49, 2: 40, 4: 32, 5: 42, 6: 6, 7: 26, 9: 23, 12: 27, 13: 41, 14: 24, 16: 25, 17: 17, 20: 16, 22: 35, 23: 33, 25: 18, 26: 46, 27: 45, 28: 49, 31: 0, 32: 4, 33: 13, 34: 12, 35: 15, 36: 5, 37: 2, 38: 30, 40: 20, 42: 3, 43: 38, 44: 43, 46: 47, 47: 19, 48: 34, 49: 29} 

进入fix_effective
修改vm超载的情况 v_id = 13, v_p_cost = 0.281729099678, v_rp = 0.3, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 49, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 28]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
1
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 10, v_p_cost = 0.561941703029, v_rp = 0.5, v_m_cost = 0.408166724666, v_rm = 0.5
取出4前有这些容器： [0, 4]
取出4后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.5
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.835842181546, v_rp = 0.5, v_m_cost = 0.765506145419, v_rm = 0.7
取出20前有这些容器： [17, 20]
取出20后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.678965527977, v_rp = 0.7, v_m_cost = 0.762532157587, v_rm = 0.3
取出38前有这些容器： [31, 38]
取出38后有： [31] v_p_cost=0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改hm过载  h_id = 0, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 5, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
20
修改hm过载  h_id = 20, h_p_cost = 1.5, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [10, 25, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.5],mem尺寸[0.5, 0.7, 1.0]
10
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
25
该物理机上的虚拟机对应cpu尺寸[0.5],mem尺寸[1.0]
47
修改hm过载  h_id = 29, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 38, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 16]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 47, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 15]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 0.5]
15
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [27, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
33
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.844889086104, v_rp = 0.5, v_m_cost = 0.702589371404, v_rm = 0.5
取出3前有这些容器： [3, 13, 24, 30]
取出3后有： [13, 24, 30] v_p_cost=0.787382036422, v_rp = 0.5, v_m_cost = 0.70130977487, v_rm = 0.5
取出30前有这些容器： [13, 24, 30]
取出30后有： [13, 24] v_p_cost=0.6443965383, v_rp = 0.5, v_m_cost = 0.50600021802, v_rm = 0.5
取出13前有这些容器： [13, 24]
取出13后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.7
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.747569332916, v_rp = 0.3, v_m_cost = 0.743810681647, v_rm = 1.0
取出36前有这些容器： [8, 34, 36]
取出36后有： [8, 34] v_p_cost=0.681875117913, v_rp = 0.3, v_m_cost = 0.685711205099, v_rm = 1.0
取出34前有这些容器： [8, 34]
取出34后有： [8] v_p_cost=0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 1.0
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.702565593495, v_rp = 0.5, v_m_cost = 0.891665947836, v_rm = 0.7
取出37前有这些容器： [20, 37]
取出37后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.86463478992, v_rp = 0.5, v_m_cost = 0.744720492863, v_rm = 0.7
取出2前有这些容器： [2, 21, 22]
取出2后有： [21, 22] v_p_cost=0.761491906012, v_rp = 0.5, v_m_cost = 0.557003507928, v_rm = 0.7
取出22前有这些容器： [21, 22]
取出22后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.475373866715, v_rp = 0.5, v_m_cost = 0.577503805194, v_rm = 0.5
取出10前有这些容器： [10, 31]
取出10后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.5
修改vm超载的情况 v_id = 20, v_p_cost = 0.947959463841, v_rp = 0.5, v_m_cost = 0.983627954639, v_rm = 0.7
取出15前有这些容器： [15, 43, 47]
取出15后有： [43, 47] v_p_cost=0.798197651366, v_rp = 0.5, v_m_cost = 0.770325854313, v_rm = 0.7
取出43前有这些容器： [43, 47]
取出43后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 26, v_p_cost = 0.531982722185, v_rp = 0.5, v_m_cost = 0.51476065859, v_rm = 0.7
取出39前有这些容器： [39, 48]
取出39后有： [48] v_p_cost=0.339680823305, v_rp = 0.5, v_m_cost = 0.363667195512, v_rm = 0.7
修改vm超载的情况 v_id = 28, v_p_cost = 0.741675493133, v_rp = 1.0, v_m_cost = 0.958192606106, v_rm = 0.5
取出9前有这些容器： [9, 23]
取出9后有： [23] v_p_cost=0.460840741494, v_rp = 1.0, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.483330295197, v_rp = 0.7, v_m_cost = 0.318607604007, v_rm = 0.3
取出40前有这些容器： [0, 40]
取出40后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 4, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 9, h_p_cost = 2.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 28, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 0.5],mem尺寸[0.5, 0.5, 0.5]
10
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 17, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 20, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [29, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.3, 1.0]
29
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 30, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 26]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.7]
26
修改hm过载  h_id = 31, h_p_cost = 1.7, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [19, 22]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 1.0]
22
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
20
修改hm过载  h_id = 41, h_p_cost = 0.6, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 15]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 46, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 25, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.7],mem尺寸[0.7, 0.7, 0.3]
3
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
25
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.368267087556, v_rp = 0.3, v_m_cost = 0.273384297823, v_rm = 1.0
取出18前有这些容器： [18]
取出18后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.871205979102, v_rp = 0.5, v_m_cost = 1.00601136251, v_rm = 0.7
取出6前有这些容器： [6, 20, 46]
取出6后有： [20, 46] v_p_cost=0.787014704616, v_rp = 0.5, v_m_cost = 0.790358420914, v_rm = 0.7
取出20前有这些容器： [20, 46]
取出20后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 1.01976546665, v_rp = 1.0, v_m_cost = 0.874357846896, v_rm = 0.7
取出39前有这些容器： [21, 31, 39]
取出39后有： [21, 31] v_p_cost=0.827463567768, v_rp = 1.0, v_m_cost = 0.723264383819, v_rm = 0.7
取出31前有这些容器： [21, 31]
取出31后有： [21] v_p_cost=0.430227139469, v_rp = 1.0, v_m_cost = 0.28072282486, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.70771217851, v_rp = 0.3, v_m_cost = 0.539834917131, v_rm = 0.3
取出26前有这些容器： [16, 26]
取出26后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 24, v_p_cost = 1.02081484792, v_rp = 1.0, v_m_cost = 0.991971334684, v_rm = 0.5
取出33前有这些容器： [1, 33, 48]
取出33后有： [1, 48] v_p_cost=0.723421882435, v_rp = 1.0, v_m_cost = 0.683446215117, v_rm = 0.5
取出48前有这些容器： [1, 48]
取出48后有： [1] v_p_cost=0.38374105913, v_rp = 1.0, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 34, v_p_cost = 0.483623484834, v_rp = 0.7, v_m_cost = 0.517327345208, v_rm = 0.5
取出25前有这些容器： [25, 37]
取出25后有： [37] v_p_cost=0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 37, v_p_cost = 0.610603201268, v_rp = 0.5, v_m_cost = 0.646944766759, v_rm = 0.7
取出38前有这些容器： [34, 38]
取出38后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.309431220171, v_rp = 0.3, v_m_cost = 0.279534147312, v_rm = 0.5
取出32前有这些容器： [28, 32]
取出32后有： [28] v_p_cost=0.186697146529, v_rp = 0.3, v_m_cost = 0.041081983725, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.640608331989, v_rp = 0.5, v_m_cost = 0.518952876214, v_rm = 1.0
取出30前有这些容器： [12, 30]
取出30后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 9]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
7
修改hm过载  h_id = 3, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 38]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 4, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.5]
41
修改hm过载  h_id = 15, h_p_cost = 2.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [24, 34, 48]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 1.0],mem尺寸[0.5, 0.5, 0.7]
34
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
24
修改hm过载  h_id = 18, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [37, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
37
修改hm过载  h_id = 19, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 28]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 26, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
10
修改hm过载  h_id = 37, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 44, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.482666321427, v_rp = 0.3, v_m_cost = 0.558976752362, v_rm = 0.7
取出30前有这些容器： [30, 48]
取出30后有： [48] v_p_cost=0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.7
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 1.43646923998, v_rp = 0.3, v_m_cost = 1.06653041749, v_rm = 0.5
取出24前有这些容器： [12, 14, 24]
取出24后有： [12, 14] v_p_cost=0.975551114026, v_rp = 0.3, v_m_cost = 0.760505773007, v_rm = 0.5
取出14前有这些容器： [12, 14]
取出14后有： [12] v_p_cost=0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.5
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.56178321739, v_rp = 0.5, v_m_cost = 0.474670059747, v_rm = 1.0
取出13前有这些容器： [7, 13]
取出13后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 1.0
修改vm超载的情况 v_id = 27, v_p_cost = 0.281729099678, v_rp = 0.7, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 38, v_p_cost = 0.755625378888, v_rp = 1.0, v_m_cost = 0.774973709559, v_rm = 0.7
取出37前有这些容器： [17, 37]
取出37后有： [17] v_p_cost=0.44445098347, v_rp = 1.0, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.636355851617, v_rp = 0.7, v_m_cost = 0.57197179063, v_rm = 0.3
取出43前有这些容器： [11, 43]
取出43后有： [11] v_p_cost=0.319134630596, v_rp = 0.7, v_m_cost = 0.2887743372, v_rm = 0.3
修改vm超载的情况 v_id = 41, v_p_cost = 0.649101839195, v_rp = 0.7, v_m_cost = 0.757714855467, v_rm = 0.5
取出9前有这些容器： [9, 18]
取出9后有： [18] v_p_cost=0.368267087556, v_rp = 0.7, v_m_cost = 0.273384297823, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.843662178736, v_rp = 0.5, v_m_cost = 0.764195406322, v_rm = 1.0
取出25前有这些容器： [23, 25, 26]
取出25后有： [23, 26] v_p_cost=0.671213089321, v_rp = 0.5, v_m_cost = 0.697434817102, v_rm = 1.0
取出26前有这些容器： [23, 26]
取出26后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 1.0
修改hm过载  h_id = 1, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [14, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
14
修改hm过载  h_id = 4, h_p_cost = 1.9, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [8, 27, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.7],mem尺寸[0.7, 0.3, 0.3]
8
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.3]
27
修改hm过载  h_id = 5, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [24, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 7, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
46
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 40, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
25
进入mbbode_rank
[7, 7, 10, 9, 7] 0
上代结果： 15760.8829213 0.778228993752 783583.280416 0.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[5, 42], [34, 12], [33, 13], [42, 3], [25, 18], [26, 46], [12, 27], [27, 45], [47, 19], [23, 33], [43, 38], [28, 49], [36, 5], [32, 4], [32, 4], [6, 6], [22, 5], [46, 47], [17, 17], [25, 18], [8, 39], [2, 40], [37, 2], [6, 6], [14, 24], [17, 17], [14, 24], [4, 32], [43, 38], [35, 15], [28, 49], [22, 35], [48, 34], [2, 40], [0, 37], [40, 20], [2, 45], [42, 3], [35, 15], [16, 25], [33, 13], [48, 34], [20, 16], [38, 30], [7, 26], [37, 2], [49, 29], [44, 43], [33, 13], [31, 0]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 22, v_p_cost = 0.894576258982, v_rp = 0.7, v_m_cost = 0.758803707449, v_rm = 1.0
取出31前有这些容器： [16, 31]
取出31后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 1.0
修改hm过载  h_id = 5, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 32, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 19]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 6, v_p_cost = 0.59805597266, v_rp = 0.7, v_m_cost = 0.767528011074, v_rm = 0.7
取出9前有这些容器： [9, 43]
取出9后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.939363290784, v_rp = 0.5, v_m_cost = 0.742432011382, v_rm = 0.5
取出0前有这些容器： [0, 14]
取出0后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.486883943038, v_rp = 0.7, v_m_cost = 0.50749600454, v_rm = 0.3
取出2前有这些容器： [1, 2]
取出2后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.3
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 0.736439625455, v_rp = 0.7, v_m_cost = 0.719150561981, v_rm = 1.0
取出32前有这些容器： [13, 21, 32]
取出32后有： [13, 21] v_p_cost=0.613705551813, v_rp = 0.7, v_m_cost = 0.480698398393, v_rm = 1.0
修改vm超载的情况 v_id = 23, v_p_cost = 0.784131806775, v_rp = 0.7, v_m_cost = 0.688074149083, v_rm = 0.5
取出48前有这些容器： [17, 48]
取出48后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 25, v_p_cost = 0.901946008812, v_rp = 0.5, v_m_cost = 0.797306849033, v_rm = 0.7
取出41前有这些容器： [41, 47]
取出41后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 14, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 19, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [37, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
37
修改hm过载  h_id = 21, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 26, h_p_cost = 1.5, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [4, 30, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 0.5],mem尺寸[1.0, 0.7, 0.7]
4
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 30, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [14, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
14
修改hm过载  h_id = 31, h_p_cost = 1.5, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [21, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.5]
21
修改hm过载  h_id = 38, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 16]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 45, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [13, 48]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.3, 0.7]
13
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 11, v_p_cost = 1.18246148448, v_rp = 0.7, v_m_cost = 0.867181956076, v_rm = 0.5
取出22前有这些容器： [21, 22, 41]
取出22后有： [21, 41] v_p_cost=0.851196717936, v_rp = 0.7, v_m_cost = 0.590901273008, v_rm = 0.5
取出41前有这些容器： [21, 41]
取出41后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.650393981807, v_rp = 0.5, v_m_cost = 0.667282156536, v_rm = 1.0
取出33前有这些容器： [8, 33]
取出33后有： [8] v_p_cost=0.353001016323, v_rp = 0.5, v_m_cost = 0.358757036968, v_rm = 1.0
修改vm超载的情况 v_id = 17, v_p_cost = 0.747177756602, v_rp = 0.7, v_m_cost = 0.689766490279, v_rm = 0.7
取出35前有这些容器： [25, 35, 47]
取出35后有： [25, 47] v_p_cost=0.65342551976, v_rp = 0.7, v_m_cost = 0.553888990104, v_rm = 0.7
修改vm超载的情况 v_id = 41, v_p_cost = 0.82910782905, v_rp = 0.7, v_m_cost = 0.747246346285, v_rm = 0.5
取出18前有这些容器： [18, 23]
取出18后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 1.7672888356, v_rp = 0.5, v_m_cost = 1.55128952721, v_rm = 0.5
取出6前有这些容器： [6, 12, 19, 24, 34]
取出6后有： [12, 19, 24, 34] v_p_cost=1.68309756111, v_rp = 0.5, v_m_cost = 1.33563658561, v_rm = 0.5
取出34前有这些容器： [12, 19, 24, 34]
取出34后有： [12, 19, 24] v_p_cost=1.35422345952, v_rp = 0.5, v_m_cost = 1.00868241748, v_rm = 0.5
取出19前有这些容器： [12, 19, 24]
取出19后有： [12, 24] v_p_cost=0.958540959823, v_rp = 0.5, v_m_cost = 0.629667963851, v_rm = 0.5
取出24前有这些容器： [12, 24]
取出24后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.894576258982, v_rp = 1.0, v_m_cost = 0.758803707449, v_rm = 0.7
取出31前有这些容器： [16, 31]
取出31后有： [16] v_p_cost=0.497339830683, v_rp = 1.0, v_m_cost = 0.31626214849, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [33, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 4, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [26, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
26
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [22, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.3]
29
修改hm过载  h_id = 26, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 39, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 8]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.683173834847, v_rp = 0.5, v_m_cost = 0.699661414872, v_rm = 0.5
取出6前有这些容器： [6, 19, 44, 45]
取出6后有： [19, 44, 45] v_p_cost=0.598982560361, v_rp = 0.5, v_m_cost = 0.484008473273, v_rm = 0.5
取出45前有这些容器： [19, 44, 45]
取出45后有： [19, 44] v_p_cost=0.511802641526, v_rp = 0.5, v_m_cost = 0.46263575861, v_rm = 0.5
取出44前有这些容器： [19, 44]
取出44后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 7, v_p_cost = 1.14460423765, v_rp = 1.0, v_m_cost = 1.08918533951, v_rm = 0.7
取出33前有这些容器： [5, 21, 33]
取出33后有： [5, 21] v_p_cost=0.847211272168, v_rp = 1.0, v_m_cost = 0.780660219944, v_rm = 0.7
取出5前有这些容器： [5, 21]
取出5后有： [21] v_p_cost=0.430227139469, v_rp = 1.0, v_m_cost = 0.28072282486, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.281729099678, v_rp = 0.3, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 0.868036775954, v_rp = 0.7, v_m_cost = 0.82284282112, v_rm = 0.5
取出27前有这些容器： [13, 14, 27, 39]
取出27后有： [13, 14, 39] v_p_cost=0.853708591382, v_rp = 0.7, v_m_cost = 0.787931490254, v_rm = 0.5
取出13前有这些容器： [13, 14, 39]
取出13后有： [14, 39] v_p_cost=0.670230179038, v_rp = 0.7, v_m_cost = 0.58795591672, v_rm = 0.5
取出39前有这些容器： [14, 39]
取出39后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 25, v_p_cost = 0.780052756552, v_rp = 0.5, v_m_cost = 0.594798981687, v_rm = 0.7
取出11前有这些容器： [11, 24]
取出11后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.788627626376, v_rp = 0.5, v_m_cost = 0.883640750807, v_rm = 0.5
取出20前有这些容器： [20, 31]
取出20后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 0.65342551976, v_rp = 0.5, v_m_cost = 0.553888990104, v_rm = 0.5
取出25前有这些容器： [25, 47]
取出25后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 18, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [43, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
43
修改hm过载  h_id = 22, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [16, 19]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 30, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [25, 28, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 0.5],mem尺寸[0.7, 0.5, 0.5]
25
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 32, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 11]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
11
修改hm过载  h_id = 36, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 44, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 46, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 48, h_p_cost = 2.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 9, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 0.7],mem尺寸[0.5, 0.5, 0.5]
0
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
23
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
9
修改hm过载  h_id = 49, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [38, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
45
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.695526026067, v_rp = 0.3, v_m_cost = 0.557891939643, v_rm = 1.0
取出43前有这些容器： [7, 43]
取出43后有： [7] v_p_cost=0.378304805046, v_rp = 0.3, v_m_cost = 0.274694486214, v_rm = 1.0
取出7前有这些容器： [7]
取出7后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 11, v_p_cost = 0.919794962073, v_rp = 0.7, v_m_cost = 0.876909886717, v_rm = 0.5
取出2前有这些容器： [2, 19, 41]
取出2后有： [19, 41] v_p_cost=0.816652078165, v_rp = 0.7, v_m_cost = 0.689192901782, v_rm = 0.5
取出19前有这些容器： [19, 41]
取出19后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.878419143324, v_rp = 0.3, v_m_cost = 0.805506952824, v_rm = 0.5
取出5前有这些容器： [0, 5]
取出5后有： [0] v_p_cost=0.461435010625, v_rp = 0.3, v_m_cost = 0.305569557739, v_rm = 0.5
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 0.458778262967, v_rp = 0.7, v_m_cost = 0.835860999419, v_rm = 0.5
取出6前有这些容器： [6, 9, 35]
取出6后有： [9, 35] v_p_cost=0.374586988481, v_rp = 0.7, v_m_cost = 0.620208057819, v_rm = 0.5
取出35前有这些容器： [9, 35]
取出35后有： [9] v_p_cost=0.280834751639, v_rp = 0.7, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.933715856967, v_rp = 0.3, v_m_cost = 1.00127416946, v_rm = 0.5
取出13前有这些容器： [8, 13, 31]
取出13后有： [8, 31] v_p_cost=0.750237444622, v_rp = 0.3, v_m_cost = 0.801298595927, v_rm = 0.5
取出8前有这些容器： [8, 31]
取出8后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.846195367714, v_rp = 0.7, v_m_cost = 0.710246751466, v_rm = 0.5
取出18前有这些容器： [14, 18]
取出18后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 1.4898314634, v_rp = 0.7, v_m_cost = 1.19590651123, v_rm = 0.7
取出25前有这些容器： [23, 24, 25, 46]
取出25后有： [23, 24, 46] v_p_cost=1.31738237399, v_rp = 0.7, v_m_cost = 1.12914592201, v_rm = 0.7
取出46前有这些容器： [23, 24, 46]
取出46后有： [23, 24] v_p_cost=0.92175886745, v_rp = 0.7, v_m_cost = 0.779886692948, v_rm = 0.7
取出23前有这些容器： [23, 24]
取出23后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 10, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 15, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 30]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 29, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 40, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 28]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 43, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 46, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 29]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.3]
16
修改hm过载  h_id = 47, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [32, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
41
进入mbbode_rank
[7, 11, 8, 11, 3] 4
上代结果： 15760.8829213 0.778228993752 783583.280416 0.0
本代结果替代后： 14866.4024847 1.05974629716 783500.399526 1625.0
执行全局精英解替换： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[5, 42], [34, 12], [33, 13], [42, 3], [25, 18], [26, 46], [12, 27], [27, 45], [47, 19], [23, 33], [14, 23], [28, 49], [36, 5], [32, 4], [32, 4], [6, 6], [22, 21], [46, 47], [17, 17], [25, 18], [8, 39], [2, 40], [37, 2], [6, 6], [14, 24], [17, 17], [14, 24], [4, 31], [43, 38], [35, 15], [28, 49], [19, 32], [48, 34], [2, 40], [0, 37], [40, 20], [2, 40], [42, 3], [35, 15], [16, 25], [33, 13], [48, 34], [20, 16], [38, 30], [7, 26], [37, 2], [49, 29], [44, 43], [33, 13], [31, 0]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 14, v_p_cost = 0.749427912198, v_rp = 0.7, v_m_cost = 0.664559659362, v_rm = 0.7
取出10前有这些容器： [10, 24, 26]
取出10后有： [24, 26] v_p_cost=0.671290473783, v_rp = 0.7, v_m_cost = 0.529597413127, v_rm = 0.7
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.514125271719, v_rp = 0.3, v_m_cost = 0.679551355435, v_rm = 0.7
取出32前有这些容器： [20, 32]
取出32后有： [20] v_p_cost=0.391391198077, v_rp = 0.3, v_m_cost = 0.441099191848, v_rm = 0.7
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 0.828428619017, v_rp = 1.0, v_m_cost = 0.996454496151, v_rm = 0.7
取出2前有这些容器： [2, 9, 17]
取出2后有： [9, 17] v_p_cost=0.725285735109, v_rp = 1.0, v_m_cost = 0.808737511215, v_rm = 0.7
取出9前有这些容器： [9, 17]
取出9后有： [17] v_p_cost=0.44445098347, v_rp = 1.0, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.569685517714, v_rp = 0.3, v_m_cost = 0.509302148179, v_rm = 0.3
取出25前有这些容器： [25, 31]
取出25后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.38374105913, v_rp = 0.3, v_m_cost = 0.319779019605, v_rm = 0.5
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 31, v_p_cost = 0.891067880963, v_rp = 0.5, v_m_cost = 0.754584873321, v_rm = 0.5
取出21前有这些容器： [21, 23]
取出21后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 0.875927638913, v_rp = 0.5, v_m_cost = 0.598337805578, v_rm = 0.5
取出7前有这些容器： [7, 12]
取出7后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 7, h_p_cost = 1.3, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [13, 28]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.3, 0.5]
13
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 17]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [21, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
21
修改hm过载  h_id = 38, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 23]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
23
修改hm过载  h_id = 44, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 46, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
5
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.32887410159, v_rp = 0.3, v_m_cost = 0.326954168131, v_rm = 1.0
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 1.24063471598, v_rp = 0.5, v_m_cost = 1.20161189055, v_rm = 0.7
取出18前有这些容器： [18, 20, 47]
取出18后有： [20, 47] v_p_cost=0.872367628422, v_rp = 0.5, v_m_cost = 0.928227592732, v_rm = 0.7
取出20前有这些容器： [20, 47]
取出20后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.517414890827, v_rp = 0.5, v_m_cost = 0.524649113845, v_rm = 0.5
取出49前有这些容器： [19, 49]
取出49后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.816474461279, v_rp = 0.3, v_m_cost = 0.60503648569, v_rm = 0.3
取出11前有这些容器： [11, 16]
取出11后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.5
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.50391836755, v_rp = 0.5, v_m_cost = 0.324279437155, v_rm = 0.3
取出28前有这些容器： [28, 43]
取出28后有： [43] v_p_cost=0.317221221021, v_rp = 0.5, v_m_cost = 0.28319745343, v_rm = 0.3
修改vm超载的情况 v_id = 28, v_p_cost = 1.2216947703, v_rp = 1.0, v_m_cost = 1.12989486284, v_rm = 0.5
取出1前有这些容器： [1, 5, 41]
取出1后有： [5, 41] v_p_cost=0.837953711166, v_rp = 1.0, v_m_cost = 0.810115843233, v_rm = 0.5
取出5前有这些容器： [5, 41]
取出5后有： [41] v_p_cost=0.420969578467, v_rp = 1.0, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 1.08175451977, v_rp = 0.7, v_m_cost = 1.10603405895, v_rm = 0.5
取出30前有这些容器： [14, 23, 30]
取出30后有： [14, 23] v_p_cost=0.938769021653, v_rp = 0.7, v_m_cost = 0.910724502104, v_rm = 0.5
取出23前有这些容器： [14, 23]
取出23后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.742269762264, v_rp = 0.7, v_m_cost = 0.789900115383, v_rm = 0.3
取出9前有这些容器： [0, 9]
取出9后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.5
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改hm过载  h_id = 12, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 19, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 26, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 25]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 31, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 19]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 1.0]
0
修改hm过载  h_id = 32, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 7]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 11]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 39, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 46, h_p_cost = 2.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 26, 29]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.5],mem尺寸[1.0, 0.7, 0.3]
26
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.3]
29
修改hm过载  h_id = 49, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [28, 48]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
28
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 15, v_p_cost = 0.627690092633, v_rp = 0.3, v_m_cost = 0.650164553968, v_rm = 0.5
取出15前有这些容器： [14, 15]
取出15后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.503713855959, v_rp = 0.5, v_m_cost = 0.343041272288, v_rm = 1.0
取出25前有这些容器： [22, 25]
取出25后有： [22] v_p_cost=0.331264766544, v_rp = 0.5, v_m_cost = 0.276280683068, v_rm = 1.0
修改vm超载的情况 v_id = 25, v_p_cost = 0.53897817991, v_rp = 0.5, v_m_cost = 0.608824294696, v_rm = 0.7
取出10前有这些容器： [10, 23]
取出10后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.741752877595, v_rp = 0.5, v_m_cost = 0.790355202131, v_rm = 0.5
取出9前有这些容器： [9, 24]
取出9后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 38, v_p_cost = 0.678965527977, v_rp = 1.0, v_m_cost = 0.762532157587, v_rm = 0.7
取出38前有这些容器： [31, 38]
取出38后有： [31] v_p_cost=0.397236428299, v_rp = 1.0, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.361576107877, v_rp = 0.7, v_m_cost = 0.37670524178, v_rm = 0.3
取出40前有这些容器： [40, 48]
取出40后有： [48] v_p_cost=0.339680823305, v_rp = 0.7, v_m_cost = 0.363667195512, v_rm = 0.3
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 42, v_p_cost = 0.798197651366, v_rp = 0.5, v_m_cost = 0.770325854313, v_rm = 0.5
取出43前有这些容器： [43, 47]
取出43后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.879756861241, v_rp = 0.7, v_m_cost = 0.866199936606, v_rm = 0.5
取出29前有这些容器： [5, 18, 29]
取出29后有： [5, 18] v_p_cost=0.785251220255, v_rp = 0.7, v_m_cost = 0.773321692908, v_rm = 0.5
取出18前有这些容器： [5, 18]
取出18后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.540054992478, v_rp = 0.5, v_m_cost = 0.459964309215, v_rm = 1.0
取出30前有这些容器： [26, 28, 30]
取出30后有： [26, 28] v_p_cost=0.397069494356, v_rp = 0.5, v_m_cost = 0.264654752366, v_rm = 1.0
修改hm过载  h_id = 3, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
46
修改hm过载  h_id = 4, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 6, h_p_cost = 1.9, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 41, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.7],mem尺寸[0.5, 0.5, 0.5]
0
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 8, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [36, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 17, h_p_cost = 1.9, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [10, 11, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.7],mem尺寸[0.5, 0.5, 0.3]
10
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.3]
11
修改hm过载  h_id = 19, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [6, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
6
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 28, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 33, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 25]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 35, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
修改hm过载  h_id = 37, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
33
修改hm过载  h_id = 38, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
20
修改hm过载  h_id = 39, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 28]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 45, h_p_cost = 1.4, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 30]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.7]
14
修改hm过载  h_id = 49, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 24]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
1
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.775876714016, v_rp = 0.7, v_m_cost = 0.863407675126, v_rm = 1.0
取出32前有这些容器： [23, 32, 39]
取出32后有： [23, 39] v_p_cost=0.653142640374, v_rp = 0.7, v_m_cost = 0.624955511539, v_rm = 1.0
修改vm超载的情况 v_id = 4, v_p_cost = 0.459070385667, v_rp = 0.3, v_m_cost = 0.45445314769, v_rm = 1.0
取出2前有这些容器： [2, 13, 25]
取出2后有： [13, 25] v_p_cost=0.355927501759, v_rp = 0.3, v_m_cost = 0.266736162754, v_rm = 1.0
取出25前有这些容器： [13, 25]
取出25后有： [13] v_p_cost=0.183478412344, v_rp = 0.3, v_m_cost = 0.199975573534, v_rm = 1.0
修改vm超载的情况 v_id = 8, v_p_cost = 0.708612419097, v_rp = 0.5, v_m_cost = 0.724296645277, v_rm = 0.7
取出43前有这些容器： [20, 43]
取出43后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.881887704423, v_rp = 0.5, v_m_cost = 0.616203092635, v_rm = 0.5
取出41前有这些容器： [24, 41]
取出41后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.716382996342, v_rp = 0.3, v_m_cost = 0.458759560188, v_rm = 0.5
取出44前有这些容器： [42, 44, 46]
取出44后有： [42, 46] v_p_cost=0.600262854513, v_rp = 0.3, v_m_cost = 0.375138255211, v_rm = 0.5
取出42前有这些容器： [42, 46]
取出42后有： [46] v_p_cost=0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.5
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.721268103879, v_rp = 0.5, v_m_cost = 0.632141334791, v_rm = 1.0
取出8前有这些容器： [8, 18]
取出8后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 1.0
修改vm超载的情况 v_id = 22, v_p_cost = 0.827463567768, v_rp = 0.7, v_m_cost = 0.723264383819, v_rm = 1.0
取出31前有这些容器： [21, 31]
取出31后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 1.0
修改vm超载的情况 v_id = 31, v_p_cost = 0.800264680401, v_rp = 0.5, v_m_cost = 0.808691566719, v_rm = 0.5
取出40前有这些容器： [33, 40, 47]
取出40后有： [33, 47] v_p_cost=0.778369395829, v_rp = 0.5, v_m_cost = 0.795653520451, v_rm = 0.5
取出33前有这些容器： [33, 47]
取出33后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 0.609708853229, v_rp = 0.7, v_m_cost = 0.811284725775, v_rm = 0.5
取出9前有这些容器： [9, 34]
取出9后有： [34] v_p_cost=0.32887410159, v_rp = 0.7, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.38374105913, v_rp = 0.3, v_m_cost = 0.319779019605, v_rm = 0.5
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.659951546769, v_rp = 0.5, v_m_cost = 0.674258507198, v_rm = 1.0
取出10前有这些容器： [6, 10, 12]
取出10后有： [6, 12] v_p_cost=0.581814108353, v_rp = 0.5, v_m_cost = 0.539296260964, v_rm = 1.0
取出6前有这些容器： [6, 12]
取出6后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 4, h_p_cost = 0.6, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 15]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 19, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [27, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.5]
31
修改hm过载  h_id = 33, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
6
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [21, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 1.0]
21
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 43, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 44, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 11]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 49, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
37
进入mbbode_rank
[6, 6, 11, 9, 8] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 8, 4: 22, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 21: 9, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 31: 29, 32: 47, 34: 23, 36: 49, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 22, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 4]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.655245840694, v_rp = 0.5, v_m_cost = 0.498467854487, v_rm = 0.5
取出49前有这些容器： [34, 42, 49]
取出49后有： [34, 42] v_p_cost=0.533513449564, v_rp = 0.5, v_m_cost = 0.352833194276, v_rm = 0.5
取出42前有这些容器： [34, 42]
取出42后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 4, v_p_cost = 0.592903495096, v_rp = 0.3, v_m_cost = 0.770557354616, v_rm = 1.0
取出38前有这些容器： [37, 38]
取出38后有： [37] v_p_cost=0.311174395419, v_rp = 0.3, v_m_cost = 0.450566755988, v_rm = 1.0
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 9, v_p_cost = 0.453283841054, v_rp = 1.0, v_m_cost = 0.551091146864, v_rm = 0.5
取出25前有这些容器： [9, 25]
取出25后有： [9] v_p_cost=0.280834751639, v_rp = 1.0, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.831937288035, v_rp = 0.5, v_m_cost = 0.835440980021, v_rm = 0.7
取出27前有这些容器： [14, 27, 48]
取出27后有： [14, 48] v_p_cost=0.817609103464, v_rp = 0.5, v_m_cost = 0.800529649155, v_rm = 0.7
取出48前有这些容器： [14, 48]
取出48后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 25, v_p_cost = 0.691348778172, v_rp = 0.5, v_m_cost = 0.710701169525, v_rm = 0.7
取出26前有这些容器： [26, 47]
取出26后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.500379312207, v_rp = 0.3, v_m_cost = 0.630258543895, v_rm = 0.5
取出2前有这些容器： [2, 31]
取出2后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.857058517165, v_rp = 0.7, v_m_cost = 0.654828786805, v_rm = 0.5
取出46前有这些容器： [0, 46]
取出46后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.805459378365, v_rp = 1.0, v_m_cost = 0.847794276391, v_rm = 0.7
取出6前有这些容器： [6, 8, 18]
取出6后有： [8, 18] v_p_cost=0.721268103879, v_rp = 1.0, v_m_cost = 0.632141334791, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 3, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 6]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 8, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [5, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
5
修改hm过载  h_id = 9, h_p_cost = 1.1, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [3, 15, 21]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.5],mem尺寸[0.7, 0.5, 0.3]
3
修改hm过载  h_id = 11, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [42, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
42
修改hm过载  h_id = 16, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 18, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [39, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.7]
39
修改hm过载  h_id = 27, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [11, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.3]
29
修改hm过载  h_id = 30, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
9
修改hm过载  h_id = 33, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [35, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 0.5]
40
修改hm过载  h_id = 38, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 12]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 39, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 26]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
26
修改hm过载  h_id = 47, h_p_cost = 2.3, h_m_cost = 2.5
该物理机上放置的虚拟机为：  [2, 4, 28]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3, 1.0],mem尺寸[1.0, 1.0, 0.5]
4
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.5]
2
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.04130961995, v_rp = 0.5, v_m_cost = 0.974982864451, v_rm = 0.5
取出44前有这些容器： [11, 19, 26, 44]
取出44后有： [11, 19, 26] v_p_cost=0.925189478121, v_rp = 0.5, v_m_cost = 0.891361559474, v_rm = 0.5
取出26前有这些容器： [11, 19, 26]
取出26后有： [11, 19] v_p_cost=0.714817130294, v_rp = 0.5, v_m_cost = 0.667788790833, v_rm = 0.5
取出11前有这些容器： [11, 19]
取出11后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.7
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 14, v_p_cost = 0.844659185086, v_rp = 0.7, v_m_cost = 0.625803664091, v_rm = 0.7
取出1前有这些容器： [1, 24]
取出1后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 25, v_p_cost = 0.837020653988, v_rp = 0.5, v_m_cost = 0.679929344002, v_rm = 0.7
取出48前有这些容器： [16, 48]
取出48后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 37, v_p_cost = 0.559113868761, v_rp = 0.5, v_m_cost = 0.622090647119, v_rm = 0.7
取出10前有这些容器： [10, 47]
取出10后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 38, v_p_cost = 1.07007141766, v_rp = 1.0, v_m_cost = 1.06789330362, v_rm = 0.7
取出9前有这些容器： [9, 18, 41]
取出9后有： [18, 41] v_p_cost=0.789236666023, v_rp = 1.0, v_m_cost = 0.583562745972, v_rm = 0.7
修改vm超载的情况 v_id = 45, v_p_cost = 0.561347433898, v_rp = 0.5, v_m_cost = 0.576459215388, v_rm = 1.0
取出4前有这些容器： [4, 23]
取出4后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 1.0
修改hm过载  h_id = 2, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 9]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 3, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 10, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 14]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 16, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 20]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
20
修改hm过载  h_id = 17, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 27, h_p_cost = 1.1, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [3, 13, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.5],mem尺寸[0.7, 0.3, 0.5]
3
修改hm过载  h_id = 33, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [28, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 34, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [32, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
34
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [6, 16, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.5],mem尺寸[0.7, 1.0, 1.0]
16
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 43, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [36, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.14791684471, v_rp = 0.5, v_m_cost = 0.965473584849, v_rm = 0.5
取出22前有这些容器： [19, 22, 41]
取出22后有： [19, 41] v_p_cost=0.816652078165, v_rp = 0.5, v_m_cost = 0.689192901782, v_rm = 0.5
取出19前有这些容器： [19, 41]
取出19后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 0.7
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 5, v_p_cost = 0.554224985795, v_rp = 0.5, v_m_cost = 0.771744862541, v_rm = 0.7
取出32前有这些容器： [15, 32, 38]
取出32后有： [15, 38] v_p_cost=0.431490912153, v_rp = 0.5, v_m_cost = 0.533292698954, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.681787720656, v_rp = 0.5, v_m_cost = 0.418530126806, v_rm = 1.0
取出3前有这些容器： [3, 4, 11, 42]
取出3后有： [4, 11, 42] v_p_cost=0.624280670974, v_rp = 0.5, v_m_cost = 0.417250530272, v_rm = 1.0
取出4前有这些容器： [4, 11, 42]
取出4后有： [11, 42] v_p_cost=0.52377397857, v_rp = 0.5, v_m_cost = 0.314653363345, v_rm = 1.0
取出42前有这些容器： [11, 42]
取出42后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 1.0
修改vm超载的情况 v_id = 25, v_p_cost = 0.955374823479, v_rp = 0.5, v_m_cost = 1.10267822524, v_rm = 0.7
取出2前有这些容器： [2, 20, 23]
取出2后有： [20, 23] v_p_cost=0.852231939571, v_rp = 0.5, v_m_cost = 0.914961240309, v_rm = 0.7
取出20前有这些容器： [20, 23]
取出20后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.5
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.978274023625, v_rp = 0.7, v_m_cost = 0.800918533764, v_rm = 0.5
取出49前有这些容器： [24, 46, 49]
取出49后有： [24, 46] v_p_cost=0.856541632495, v_rp = 0.7, v_m_cost = 0.655283873552, v_rm = 0.5
取出46前有这些容器： [24, 46]
取出46后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.515571248119, v_rp = 0.5, v_m_cost = 0.368036151856, v_rm = 1.0
取出28前有这些容器： [28, 34]
取出28后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 1.0
修改vm超载的情况 v_id = 48, v_p_cost = 1.14663648338, v_rp = 1.0, v_m_cost = 1.06903781827, v_rm = 0.7
取出33前有这些容器： [18, 33, 47]
取出33后有： [18, 47] v_p_cost=0.849243517901, v_rp = 1.0, v_m_cost = 0.760512698707, v_rm = 0.7
取出18前有这些容器： [18, 47]
取出18后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 11]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
1
修改hm过载  h_id = 2, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 3, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
17
修改hm过载  h_id = 14, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 19]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 38, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 47, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[0.5, 0.5]
40
修改hm过载  h_id = 49, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 38]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.7]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.510736369541, v_rp = 0.5, v_m_cost = 0.63581489526, v_rm = 0.5
取出35前有这些容器： [5, 35]
取出35后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.378304805046, v_rp = 0.3, v_m_cost = 0.274694486214, v_rm = 0.7
取出7前有这些容器： [7]
取出7后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.501323191005, v_rp = 0.3, v_m_cost = 0.393714757351, v_rm = 1.0
取出25前有这些容器： [25, 34]
取出25后有： [34] v_p_cost=0.32887410159, v_rp = 0.3, v_m_cost = 0.326954168131, v_rm = 1.0
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 13, v_p_cost = 0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 0.3
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.79969101275, v_rp = 0.5, v_m_cost = 0.637353265421, v_rm = 0.3
取出28前有这些容器： [22, 28, 38]
取出28后有： [22, 38] v_p_cost=0.612993866221, v_rp = 0.5, v_m_cost = 0.596271281696, v_rm = 0.3
取出38前有这些容器： [22, 38]
取出38后有： [22] v_p_cost=0.331264766544, v_rp = 0.5, v_m_cost = 0.276280683068, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.353001016323, v_rp = 0.5, v_m_cost = 0.358757036968, v_rm = 0.3
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.91830940915, v_rp = 0.5, v_m_cost = 0.626440596639, v_rm = 0.7
取出41前有这些容器： [16, 41]
取出41后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.856600625653, v_rp = 0.7, v_m_cost = 0.685039098119, v_rm = 0.3
取出19前有这些容器： [19, 24]
取出19后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.3
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 49, v_p_cost = 0.678198737942, v_rp = 1.0, v_m_cost = 0.685070898623, v_rm = 0.5
取出29前有这些容器： [20, 29, 39]
取出29后有： [20, 39] v_p_cost=0.583693096956, v_rp = 1.0, v_m_cost = 0.592192654925, v_rm = 0.5
取出39前有这些容器： [20, 39]
取出39后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.5
修改hm过载  h_id = 2, h_p_cost = 1.4, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 7, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [21, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
21
修改hm过载  h_id = 15, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
19
修改hm过载  h_id = 16, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 17, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [33, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[1.0, 0.5]
40
修改hm过载  h_id = 29, h_p_cost = 2.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [27, 32, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.5],mem尺寸[0.3, 0.7, 0.5]
42
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
27
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
32
修改hm过载  h_id = 38, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 42, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 29]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 45, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
9
修改hm过载  h_id = 47, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 3]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 0.7]
3
进入mbbode_rank
[2, 10, 10, 9, 9] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 8, 4: 22, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 21: 9, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 31: 29, 32: 47, 34: 23, 36: 49, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 22, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 27]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 1.0
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 7, v_p_cost = 0.841687411769, v_rp = 1.0, v_m_cost = 0.76694851253, v_rm = 0.7
取出31前有这些容器： [17, 31]
取出31后有： [17] v_p_cost=0.44445098347, v_rp = 1.0, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.527129225628, v_rp = 0.5, v_m_cost = 0.363669034287, v_rm = 0.5
取出36前有这些容器： [0, 36]
取出36后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.800139182048, v_rp = 0.3, v_m_cost = 0.716925143188, v_rm = 0.5
取出15前有这些容器： [14, 15, 25]
取出15后有： [14, 25] v_p_cost=0.650377369574, v_rp = 0.3, v_m_cost = 0.503623042863, v_rm = 0.5
取出25前有这些容器： [14, 25]
取出25后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 23, v_p_cost = 0.583652199598, v_rp = 0.7, v_m_cost = 0.544476808074, v_rm = 0.5
取出32前有这些容器： [24, 32]
取出32后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.313515231735, v_rp = 0.7, v_m_cost = 0.411289753576, v_rm = 0.3
取出2前有这些容器： [2, 26]
取出2后有： [26] v_p_cost=0.210372347827, v_rp = 0.7, v_m_cost = 0.223572768641, v_rm = 0.3
修改vm超载的情况 v_id = 36, v_p_cost = 0.951403139938, v_rp = 0.7, v_m_cost = 0.758770456068, v_rm = 0.5
取出39前有这些容器： [21, 34, 39]
取出39后有： [21, 34] v_p_cost=0.759101241059, v_rp = 0.7, v_m_cost = 0.60767699299, v_rm = 0.5
取出34前有这些容器： [21, 34]
取出34后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.592128474853, v_rp = 0.5, v_m_cost = 0.416521563062, v_rm = 1.0
取出29前有这些容器： [12, 29]
取出29后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.7, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [17, 42, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.5],mem尺寸[0.7, 0.5, 1.0]
42
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 2, h_p_cost = 2.5, h_m_cost = 2.1
该物理机上放置的虚拟机为：  [25, 32, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 1.0],mem尺寸[0.7, 0.7, 0.7]
25
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
32
修改hm过载  h_id = 15, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
20
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [33, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
33
修改hm过载  h_id = 25, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 27, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 34, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
修改hm过载  h_id = 41, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 42, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 46, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [15, 24]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.5]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 6, v_p_cost = 0.726888273083, v_rp = 0.7, v_m_cost = 0.625539912134, v_rm = 0.7
取出22前有这些容器： [22, 46]
取出22后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 0.85062385019, v_rp = 1.0, v_m_cost = 0.682400356332, v_rm = 0.5
取出8前有这些容器： [8, 12]
取出8后有： [12] v_p_cost=0.497622833867, v_rp = 1.0, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 25, v_p_cost = 0.881080889813, v_rp = 0.5, v_m_cost = 0.636041168094, v_rm = 0.7
取出1前有这些容器： [1, 16]
取出1后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.73420535372, v_rp = 0.5, v_m_cost = 0.783134848514, v_rm = 0.7
取出43前有这些容器： [5, 43]
取出43后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 41, v_p_cost = 0.586403531467, v_rp = 0.7, v_m_cost = 0.636574602472, v_rm = 0.5
取出29前有这些容器： [4, 20, 29]
取出29后有： [4, 20] v_p_cost=0.491897890481, v_rp = 0.7, v_m_cost = 0.543696358774, v_rm = 0.5
取出4前有这些容器： [4, 20]
取出4后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.577555152454, v_rp = 0.5, v_m_cost = 0.389190862716, v_rm = 1.0
取出44前有这些容器： [0, 44]
取出44后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 1.0
修改vm超载的情况 v_id = 48, v_p_cost = 0.775321245642, v_rp = 1.0, v_m_cost = 0.74538757321, v_rm = 0.7
取出33前有这些容器： [14, 33]
取出33后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [40, 43]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.7]
40
修改hm过载  h_id = 7, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 10, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [14, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 12, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
33
修改hm过载  h_id = 23, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 17]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 25, h_p_cost = 2.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [21, 24, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 0.7],mem尺寸[0.3, 0.5, 0.5]
21
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
44
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
24
修改hm过载  h_id = 30, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 16]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 32, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 25]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 34, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [37, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
37
修改hm过载  h_id = 38, h_p_cost = 1.9, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [1, 6, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7, 0.5],mem尺寸[1.0, 0.7, 0.7]
26
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [36, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.09119975751, v_rp = 0.5, v_m_cost = 0.898134364869, v_rm = 0.5
取出39前有这些容器： [14, 39, 41]
取出39后有： [14, 41] v_p_cost=0.898897858626, v_rp = 0.5, v_m_cost = 0.747040901791, v_rm = 0.5
取出41前有这些容器： [14, 41]
取出41后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 7, v_p_cost = 0.693900127715, v_rp = 1.0, v_m_cost = 1.02693766737, v_rm = 0.7
取出6前有这些容器： [6, 9, 34]
取出6后有： [9, 34] v_p_cost=0.609708853229, v_rp = 1.0, v_m_cost = 0.811284725775, v_rm = 0.7
取出9前有这些容器： [9, 34]
取出9后有： [34] v_p_cost=0.32887410159, v_rp = 1.0, v_m_cost = 0.326954168131, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.856523241192, v_rp = 0.3, v_m_cost = 0.852876502094, v_rm = 0.3
取出19前有这些容器： [19, 23]
取出19后有： [23] v_p_cost=0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.3
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.519518118439, v_rp = 0.5, v_m_cost = 0.336681365632, v_rm = 0.7
取出40前有这些容器： [12, 40]
取出40后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.87283888703, v_rp = 0.5, v_m_cost = 0.903510662997, v_rm = 0.5
取出2前有这些容器： [2, 7, 20]
取出2后有： [7, 20] v_p_cost=0.769696003122, v_rp = 0.5, v_m_cost = 0.715793678061, v_rm = 0.5
取出7前有这些容器： [7, 20]
取出7后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.664175411742, v_rp = 0.3, v_m_cost = 0.809323792956, v_rm = 0.5
取出37前有这些容器： [8, 37]
取出37后有： [8] v_p_cost=0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 0.666517845519, v_rp = 0.5, v_m_cost = 0.480620291984, v_rm = 0.5
取出10前有这些容器： [1, 10, 42]
取出10后有： [1, 42] v_p_cost=0.588380407104, v_rp = 0.5, v_m_cost = 0.345658045749, v_rm = 0.5
取出42前有这些容器： [1, 42]
取出42后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.5
修改hm过载  h_id = 3, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [39, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
39
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.5]
31
修改hm过载  h_id = 20, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 21, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 41]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 40]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.5]
42
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
25
修改hm过载  h_id = 41, h_p_cost = 2.2, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [2, 6, 12]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 0.5],mem尺寸[1.0, 0.7, 0.7]
12
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
6
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
2
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 44, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [43, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
43
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [18, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 1.0]
45
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.374586988481, v_rp = 0.5, v_m_cost = 0.620208057819, v_rm = 0.5
取出35前有这些容器： [9, 35]
取出35后有： [9] v_p_cost=0.280834751639, v_rp = 0.5, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 2, v_p_cost = 1.04349861682, v_rp = 1.0, v_m_cost = 0.741994736086, v_rm = 1.0
取出39前有这些容器： [21, 39, 41]
取出39后有： [21, 41] v_p_cost=0.851196717936, v_rp = 1.0, v_m_cost = 0.590901273008, v_rm = 1.0
修改vm超载的情况 v_id = 4, v_p_cost = 0.50391836755, v_rp = 0.3, v_m_cost = 0.324279437155, v_rm = 1.0
取出28前有这些容器： [28, 43]
取出28后有： [43] v_p_cost=0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 1.0
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 7, v_p_cost = 0.846195367714, v_rp = 1.0, v_m_cost = 0.710246751466, v_rm = 0.7
取出18前有这些容器： [14, 18]
取出18后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.62035690751, v_rp = 0.5, v_m_cost = 0.562095482952, v_rm = 0.7
取出32前有这些容器： [12, 32]
取出32后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.795288937745, v_rp = 0.7, v_m_cost = 0.774631881298, v_rm = 0.5
取出7前有这些容器： [5, 7]
取出7后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 28, v_p_cost = 0.559113868761, v_rp = 1.0, v_m_cost = 0.622090647119, v_rm = 0.5
取出10前有这些容器： [10, 47]
取出10后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.65039939714, v_rp = 0.5, v_m_cost = 0.565055020268, v_rm = 0.3
取出11前有这些容器： [11, 22]
取出11后有： [22] v_p_cost=0.331264766544, v_rp = 0.5, v_m_cost = 0.276280683068, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.527129225628, v_rp = 0.5, v_m_cost = 0.363669034287, v_rm = 0.5
取出36前有这些容器： [0, 36]
取出36后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.881080889813, v_rp = 0.5, v_m_cost = 0.636041168094, v_rm = 0.7
取出1前有这些容器： [1, 16]
取出1后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [15, 23, 25]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 0.5],mem尺寸[0.5, 0.5, 0.7]
15
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
25
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 3, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 8, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [1, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.3]
21
修改hm过载  h_id = 14, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [34, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [45, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.7]
45
修改hm过载  h_id = 27, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [6, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
6
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
修改hm过载  h_id = 35, h_p_cost = 1.7, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [18, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 1.0]
18
修改hm过载  h_id = 44, h_p_cost = 1.3, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 48]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 47, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [17, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 48, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.5]
4
进入mbbode_rank
[4, 7, 8, 9, 12] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [7, 36], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 22, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 7]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
6
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 11, v_p_cost = 0.445767382363, v_rp = 0.7, v_m_cost = 0.59235818338, v_rm = 0.5
取出40前有这些容器： [6, 40, 48]
取出40后有： [6, 48] v_p_cost=0.423872097791, v_rp = 0.7, v_m_cost = 0.579320137112, v_rm = 0.5
取出6前有这些容器： [6, 48]
取出6后有： [48] v_p_cost=0.339680823305, v_rp = 0.7, v_m_cost = 0.363667195512, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.5
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.77312805545, v_rp = 0.7, v_m_cost = 0.905734320123, v_rm = 0.3
取出32前有这些容器： [8, 32, 33]
取出32后有： [8, 33] v_p_cost=0.650393981807, v_rp = 0.7, v_m_cost = 0.667282156536, v_rm = 0.3
取出33前有这些容器： [8, 33]
取出33后有： [8] v_p_cost=0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.3
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 0.941894556301, v_rp = 0.7, v_m_cost = 0.79315304537, v_rm = 0.5
取出24前有这些容器： [24, 47]
取出24后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 0.640325328805, v_rp = 1.0, v_m_cost = 0.51157170534, v_rm = 0.5
取出30前有这些容器： [16, 30]
取出30后有： [16] v_p_cost=0.497339830683, v_rp = 1.0, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 26, v_p_cost = 0.806802381749, v_rp = 0.5, v_m_cost = 0.763816621773, v_rm = 0.7
取出34前有这些容器： [14, 34]
取出34后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 38, v_p_cost = 0.818206006766, v_rp = 1.0, v_m_cost = 0.752720007108, v_rm = 0.7
取出31前有这些容器： [31, 41]
取出31后有： [41] v_p_cost=0.420969578467, v_rp = 1.0, v_m_cost = 0.310178448149, v_rm = 0.7
修改hm过载  h_id = 2, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [27, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.7]
27
修改hm过载  h_id = 19, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 28, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
37
修改hm过载  h_id = 29, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 32, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [41, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [29, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 37, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [35, 44]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.5]
44
修改hm过载  h_id = 41, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [33, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
33
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.08411459752, v_rp = 0.5, v_m_cost = 0.981964312703, v_rm = 0.5
取出4前有这些容器： [4, 19, 39, 46]
取出4后有： [19, 39, 46] v_p_cost=0.983607905117, v_rp = 0.5, v_m_cost = 0.879367145776, v_rm = 0.5
取出39前有这些容器： [19, 39, 46]
取出39后有： [19, 46] v_p_cost=0.791306006237, v_rp = 0.5, v_m_cost = 0.728273682699, v_rm = 0.5
取出46前有这些容器： [19, 46]
取出46后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 7, v_p_cost = 0.678965527977, v_rp = 1.0, v_m_cost = 0.762532157587, v_rm = 0.7
取出38前有这些容器： [31, 38]
取出38后有： [31] v_p_cost=0.397236428299, v_rp = 1.0, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 1.23942018617, v_rp = 0.7, v_m_cost = 0.99386596157, v_rm = 0.5
取出22前有这些容器： [14, 21, 22]
取出22后有： [14, 21] v_p_cost=0.908155419627, v_rp = 0.7, v_m_cost = 0.717585278502, v_rm = 0.5
取出21前有这些容器： [14, 21]
取出21后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.3
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.44445098347, v_rp = 0.3, v_m_cost = 0.324406953571, v_rm = 0.5
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 0.878419143324, v_rp = 1.0, v_m_cost = 0.805506952824, v_rm = 0.5
取出5前有这些容器： [0, 5]
取出5后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 31, v_p_cost = 0.420127039126, v_rp = 0.5, v_m_cost = 0.546977283155, v_rm = 0.5
取出32前有这些容器： [32, 33]
取出32后有： [33] v_p_cost=0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.775132257207, v_rp = 0.7, v_m_cost = 0.760878211452, v_rm = 0.5
取出1前有这些容器： [1, 20]
取出1后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 1.00751138684, v_rp = 0.5, v_m_cost = 1.01908992589, v_rm = 1.0
取出36前有这些容器： [23, 36, 47]
取出36后有： [23, 47] v_p_cost=0.941817171839, v_rp = 0.5, v_m_cost = 0.960990449345, v_rm = 1.0
取出23前有这些容器： [23, 47]
取出23后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 1.0
修改vm超载的情况 v_id = 46, v_p_cost = 0.692561613646, v_rp = 0.7, v_m_cost = 0.860406254772, v_rm = 0.7
取出29前有这些容器： [9, 29, 43]
取出29后有： [9, 43] v_p_cost=0.59805597266, v_rp = 0.7, v_m_cost = 0.767528011074, v_rm = 0.7
取出9前有这些容器： [9, 43]
取出9后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.7
修改hm过载  h_id = 4, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 6, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 14, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 15, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 17, h_p_cost = 2.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 35]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 1.0]
2
修改hm过载  h_id = 24, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [28, 30]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
30
修改hm过载  h_id = 30, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 32, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
41
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [21, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
21
修改hm过载  h_id = 37, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 31]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
修改hm过载  h_id = 42, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 48, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
23
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.742647225634, v_rp = 0.5, v_m_cost = 0.626015243114, v_rm = 0.5
取出38前有这些容器： [24, 38]
取出38后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 7, v_p_cost = 0.640048497009, v_rp = 1.0, v_m_cost = 0.777520924119, v_rm = 0.7
取出37前有这些容器： [34, 37]
取出37后有： [34] v_p_cost=0.32887410159, v_rp = 1.0, v_m_cost = 0.326954168131, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.400718126972, v_rp = 1.0, v_m_cost = 0.531305980819, v_rm = 0.5
取出29前有这些容器： [13, 29, 32]
取出29后有： [13, 32] v_p_cost=0.306212485987, v_rp = 1.0, v_m_cost = 0.438427737121, v_rm = 0.5
修改vm超载的情况 v_id = 10, v_p_cost = 0.800111060941, v_rp = 0.5, v_m_cost = 0.775902738084, v_rm = 0.5
取出11前有这些容器： [11, 47]
取出11后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.5
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.3
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 1.12958199756, v_rp = 0.5, v_m_cost = 1.03447509343, v_rm = 0.5
取出43前有这些容器： [20, 41, 43]
取出43后有： [20, 41] v_p_cost=0.812360776544, v_rp = 0.5, v_m_cost = 0.751277639996, v_rm = 0.5
取出20前有这些容器： [20, 41]
取出20后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 37, v_p_cost = 0.647101643158, v_rp = 0.5, v_m_cost = 0.529564248815, v_rm = 0.7
取出15前有这些容器： [15, 16]
取出15后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 45, v_p_cost = 0.587925405419, v_rp = 0.5, v_m_cost = 0.500352692143, v_rm = 1.0
取出39前有这些容器： [39, 46]
取出39后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.9, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [1, 11, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7, 0.5],mem尺寸[1.0, 0.5, 0.7]
26
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
1
修改hm过载  h_id = 2, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 25]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
25
修改hm过载  h_id = 12, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [0, 10, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 1.0],mem尺寸[0.5, 0.5, 0.7]
0
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 15, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 19, h_p_cost = 1.3, h_m_cost = 1.1
该物理机上放置的虚拟机为：  [13, 29, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.5],mem尺寸[0.3, 0.3, 0.5]
13
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
20
修改hm过载  h_id = 32, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [37, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
37
修改hm过载  h_id = 34, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 40]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 0.5]
40
修改hm过载  h_id = 43, h_p_cost = 1.9, h_m_cost = 1.8
该物理机上放置的虚拟机为：  [34, 39, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7, 0.5],mem尺寸[0.5, 0.3, 1.0]
47
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.3]
34
修改hm过载  h_id = 48, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
8
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 0.746972261677, v_rp = 0.7, v_m_cost = 0.592995607739, v_rm = 0.5
取出35前有这些容器： [24, 35, 39]
取出35后有： [24, 39] v_p_cost=0.653220024835, v_rp = 0.7, v_m_cost = 0.457118107564, v_rm = 0.5
修改vm超载的情况 v_id = 14, v_p_cost = 0.814844054888, v_rp = 0.7, v_m_cost = 0.606840772794, v_rm = 0.7
取出43前有这些容器： [12, 43]
取出43后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.319288250056, v_rp = 0.3, v_m_cost = 0.321563165836, v_rm = 0.5
取出40前有这些容器： [33, 40]
取出40后有： [33] v_p_cost=0.297392965484, v_rp = 0.3, v_m_cost = 0.308525119567, v_rm = 0.5
修改vm超载的情况 v_id = 17, v_p_cost = 0.731072021382, v_rp = 0.7, v_m_cost = 0.80476638736, v_rm = 0.7
取出48前有这些容器： [20, 48]
取出48后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.602708821475, v_rp = 0.7, v_m_cost = 0.632763061096, v_rm = 0.5
取出49前有这些容器： [47, 49]
取出49后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 26, v_p_cost = 0.630309026015, v_rp = 0.5, v_m_cost = 0.739341093188, v_rm = 0.7
取出37前有这些容器： [11, 37]
取出37后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 0.7
修改vm超载的情况 v_id = 29, v_p_cost = 0.57475695707, v_rp = 0.5, v_m_cost = 0.574187406844, v_rm = 0.3
取出4前有这些容器： [4, 22, 30]
取出4后有： [22, 30] v_p_cost=0.474250264666, v_rp = 0.5, v_m_cost = 0.471590239918, v_rm = 0.3
取出30前有这些容器： [22, 30]
取出30后有： [22] v_p_cost=0.331264766544, v_rp = 0.5, v_m_cost = 0.276280683068, v_rm = 0.3
修改vm超载的情况 v_id = 43, v_p_cost = 1.30058055716, v_rp = 1.0, v_m_cost = 1.05412609241, v_rm = 0.7
取出7前有这些容器： [0, 7, 23]
取出7后有： [0, 23] v_p_cost=0.922275752119, v_rp = 1.0, v_m_cost = 0.779431606201, v_rm = 0.7
取出23前有这些容器： [0, 23]
取出23后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.7
修改vm超载的情况 v_id = 46, v_p_cost = 0.816652078165, v_rp = 0.7, v_m_cost = 0.689192901782, v_rm = 0.7
取出19前有这些容器： [19, 41]
取出19后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.9, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [6, 16, 17]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.7],mem尺寸[0.7, 1.0, 0.7]
16
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 2, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [9, 22]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 1.0]
22
修改hm过载  h_id = 3, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 15, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [30, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 19, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 41]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 24, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
11
修改hm过载  h_id = 26, h_p_cost = 2.0, h_m_cost = 2.1
该物理机上放置的虚拟机为：  [25, 37, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 1.0],mem尺寸[0.7, 0.7, 0.7]
25
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
37
修改hm过载  h_id = 36, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 20]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 37, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [32, 48]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
32
修改hm过载  h_id = 41, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 12]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
进入mbbode_rank
[3, 12, 9, 10, 6] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [10, 0], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [26, 5], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.803205370549, v_rp = 0.5, v_m_cost = 0.732766213703, v_rm = 0.5
取出4前有这些容器： [4, 38, 41]
取出4后有： [38, 41] v_p_cost=0.702698678145, v_rp = 0.5, v_m_cost = 0.630169046777, v_rm = 0.5
取出38前有这些容器： [38, 41]
取出38后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.6, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3]
该物理机上的虚拟机对应cpu尺寸[0.3],mem尺寸[0.7]
3
修改hm过载  h_id = 17, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [17, 40]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 22, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 5]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 2, v_p_cost = 1.09429114119, v_rp = 1.0, v_m_cost = 1.00957856933, v_rm = 1.0
取出35前有这些容器： [8, 23, 28, 35]
取出35后有： [8, 23, 28] v_p_cost=1.00053890435, v_rp = 1.0, v_m_cost = 0.873701069155, v_rm = 1.0
取出28前有这些容器： [8, 23, 28]
取出28后有： [8, 23] v_p_cost=0.813841757817, v_rp = 1.0, v_m_cost = 0.83261908543, v_rm = 1.0
修改vm超载的情况 v_id = 3, v_p_cost = 0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.7
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.45708541308, v_rp = 0.5, v_m_cost = 0.499198668396, v_rm = 0.3
取出36前有这些容器： [20, 36]
取出36后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.778457585506, v_rp = 0.5, v_m_cost = 0.807973877008, v_rm = 1.0
取出9前有这些容器： [9, 12]
取出9后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 4, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 9]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
1
修改hm过载  h_id = 12, h_p_cost = 0.6, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 40]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 26, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 44, h_p_cost = 1.5, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [19, 21]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.3]
21
修改hm过载  h_id = 47, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [28, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
46
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 13, v_p_cost = 0.819932319989, v_rp = 0.3, v_m_cost = 0.780275052374, v_rm = 0.3
取出35前有这些容器： [17, 35, 38]
取出35后有： [17, 38] v_p_cost=0.726180083148, v_rp = 0.3, v_m_cost = 0.644397552199, v_rm = 0.3
取出38前有这些容器： [17, 38]
取出38后有： [17] v_p_cost=0.44445098347, v_rp = 0.3, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 14, v_p_cost = 0.778139346977, v_rp = 0.7, v_m_cost = 0.589222097916, v_rm = 0.7
取出43前有这些容器： [24, 43]
取出43后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.331264766544, v_rp = 0.3, v_m_cost = 0.276280683068, v_rm = 0.5
取出22前有这些容器： [22]
取出22后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 1.16310292333, v_rp = 0.7, v_m_cost = 0.82338439397, v_rm = 0.3
取出42前有这些容器： [12, 23, 42]
取出42后有： [12, 23] v_p_cost=0.958463575361, v_rp = 0.7, v_m_cost = 0.797505367826, v_rm = 0.3
取出23前有这些容器： [12, 23]
取出23后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.507765313311, v_rp = 0.5, v_m_cost = 0.532097888208, v_rm = 0.3
取出26前有这些容器： [26, 33]
取出26后有： [33] v_p_cost=0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 24, v_p_cost = 0.839739815671, v_rp = 1.0, v_m_cost = 0.580264043953, v_rm = 0.5
取出7前有这些容器： [0, 7]
取出7后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 28, v_p_cost = 1.07932897866, v_rp = 1.0, v_m_cost = 1.03843768033, v_rm = 0.5
取出9前有这些容器： [9, 18, 21]
取出9后有： [18, 21] v_p_cost=0.798494227024, v_rp = 1.0, v_m_cost = 0.554107122683, v_rm = 0.5
取出18前有这些容器： [18, 21]
取出18后有： [21] v_p_cost=0.430227139469, v_rp = 1.0, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 0.702875689726, v_rp = 0.7, v_m_cost = 0.608553356805, v_rm = 0.5
取出11前有这些容器： [1, 11]
取出11后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.502762828798, v_rp = 0.7, v_m_cost = 0.572059137294, v_rm = 0.5
取出15前有这些容器： [8, 15]
取出15后有： [8] v_p_cost=0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.559969630821, v_rp = 0.7, v_m_cost = 0.695246951934, v_rm = 0.3
取出30前有这些容器： [5, 30]
取出30后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 44, v_p_cost = 1.45659259292, v_rp = 0.7, v_m_cost = 1.54113822138, v_rm = 0.5
取出40前有这些容器： [6, 14, 32, 34, 40, 41]
取出40后有： [6, 14, 32, 34, 41] v_p_cost=1.43469730834, v_rp = 0.7, v_m_cost = 1.52810017511, v_rm = 0.5
取出6前有这些容器： [6, 14, 32, 34, 41]
取出6后有： [14, 32, 34, 41] v_p_cost=1.35050603386, v_rp = 0.7, v_m_cost = 1.31244723351, v_rm = 0.5
取出32前有这些容器： [14, 32, 34, 41]
取出32后有： [14, 34, 41] v_p_cost=1.22777196022, v_rp = 0.7, v_m_cost = 1.07399506992, v_rm = 0.5
取出34前有这些容器： [14, 34, 41]
取出34后有： [14, 41] v_p_cost=0.898897858626, v_rp = 0.7, v_m_cost = 0.747040901791, v_rm = 0.5
取出41前有这些容器： [14, 41]
取出41后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 14, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 16, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 30]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
30
修改hm过载  h_id = 20, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 25, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
1
修改hm过载  h_id = 26, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 11]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 31, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [42, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 37, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 24]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 40, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [40, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
40
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [36, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 48, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [39, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.7]
39
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 2, v_p_cost = 1.24587173311, v_rp = 1.0, v_m_cost = 1.09986139752, v_rm = 1.0
取出22前有这些容器： [5, 12, 22]
取出22后有： [5, 12] v_p_cost=0.914606966566, v_rp = 1.0, v_m_cost = 0.823580714449, v_rm = 1.0
修改vm超载的情况 v_id = 11, v_p_cost = 0.87634210025, v_rp = 0.7, v_m_cost = 1.15334809847, v_rm = 0.5
取出6前有这些容器： [6, 37, 47]
取出6后有： [37, 47] v_p_cost=0.792150825764, v_rp = 0.7, v_m_cost = 0.937695156872, v_rm = 0.5
取出37前有这些容器： [37, 47]
取出37后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.860843716183, v_rp = 0.3, v_m_cost = 0.77815938362, v_rm = 0.5
取出36前有这些容器： [14, 36, 43]
取出36后有： [14, 43] v_p_cost=0.795149501179, v_rp = 0.3, v_m_cost = 0.720059907072, v_rm = 0.5
取出43前有这些容器： [14, 43]
取出43后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 1.11022302463e-16, v_rm = 0.5
修改vm超载的情况 v_id = 20, v_p_cost = 0.844521754299, v_rp = 0.5, v_m_cost = 0.791638017448, v_rm = 0.7
取出3前有这些容器： [3, 20, 46]
取出3后有： [20, 46] v_p_cost=0.787014704616, v_rp = 0.5, v_m_cost = 0.790358420914, v_rm = 0.7
取出20前有这些容器： [20, 46]
取出20后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.952600480772, v_rp = 0.7, v_m_cost = 0.655958116383, v_rm = 0.3
取出45前有这些容器： [17, 41, 45]
取出45后有： [17, 41] v_p_cost=0.865420561937, v_rp = 0.7, v_m_cost = 0.63458540172, v_rm = 0.3
取出41前有这些容器： [17, 41]
取出41后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 38, v_p_cost = 0.66457581077, v_rp = 1.0, v_m_cost = 0.804109577249, v_rm = 0.7
取出9前有这些容器： [1, 9]
取出9后有： [1] v_p_cost=0.38374105913, v_rp = 1.0, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.468896443071, v_rp = 0.3, v_m_cost = 0.502076437526, v_rm = 0.5
取出15前有这些容器： [11, 15]
取出15后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 0.5
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 1.26667999735, v_rp = 0.7, v_m_cost = 0.857001561031, v_rm = 0.5
取出44前有这些容器： [16, 24, 39, 44]
取出44后有： [16, 24, 39] v_p_cost=1.15055985552, v_rp = 0.7, v_m_cost = 0.773380256054, v_rm = 0.5
取出39前有这些容器： [16, 24, 39]
取出39后有： [16, 24] v_p_cost=0.958257956639, v_rp = 0.7, v_m_cost = 0.622286792976, v_rm = 0.5
取出24前有这些容器： [16, 24]
取出24后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.540716176971, v_rp = 0.5, v_m_cost = 0.340144887043, v_rm = 1.0
取出25前有这些容器： [18, 25]
取出25后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 1.0
修改vm超载的情况 v_id = 48, v_p_cost = 0.887783947202, v_rp = 1.0, v_m_cost = 0.922577820902, v_rm = 0.7
取出26前有这些容器： [19, 26, 38]
取出26后有： [19, 38] v_p_cost=0.677411599375, v_rp = 1.0, v_m_cost = 0.699005052261, v_rm = 0.7
修改hm过载  h_id = 1, h_p_cost = 2.0, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [19, 26, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.5],mem尺寸[1.0, 0.7, 1.0]
26
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 13, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 40]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 0.5]
40
修改hm过载  h_id = 29, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [30, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
30
修改hm过载  h_id = 40, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 14]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 41, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 42, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 43, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.7
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.57624178237, v_rp = 0.3, v_m_cost = 0.699806367482, v_rm = 1.0
取出4前有这些容器： [4, 8, 32]
取出4后有： [8, 32] v_p_cost=0.475735089966, v_rp = 0.3, v_m_cost = 0.597209200556, v_rm = 1.0
取出32前有这些容器： [8, 32]
取出32后有： [8] v_p_cost=0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 1.0
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 1.0
修改vm超载的情况 v_id = 9, v_p_cost = 0.526534956497, v_rp = 1.0, v_m_cost = 0.53196152501, v_rm = 0.5
取出36前有这些容器： [23, 36]
取出36后有： [23] v_p_cost=0.460840741494, v_rp = 1.0, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.609252549582, v_rp = 0.5, v_m_cost = 0.474639467891, v_rm = 0.7
取出3前有这些容器： [3, 13, 18]
取出3后有： [13, 18] v_p_cost=0.5517454999, v_rp = 0.5, v_m_cost = 0.473359871357, v_rm = 0.7
取出13前有这些容器： [13, 18]
取出13后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.461435010625, v_rp = 0.3, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 17, v_p_cost = 0.818206006766, v_rp = 0.7, v_m_cost = 0.752720007108, v_rm = 0.7
取出31前有这些容器： [31, 41]
取出31后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 29, v_p_cost = 0.761491906012, v_rp = 0.5, v_m_cost = 0.557003507928, v_rm = 0.3
取出22前有这些容器： [21, 22]
取出22后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.73420535372, v_rp = 0.3, v_m_cost = 0.783134848514, v_rm = 0.5
取出43前有这些容器： [5, 43]
取出43后有： [5] v_p_cost=0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.5
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.582944153019, v_rp = 0.5, v_m_cost = 0.300573512358, v_rm = 1.0
取出42前有这些容器： [7, 42]
取出42后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 1.0
修改vm超载的情况 v_id = 46, v_p_cost = 1.37049306845, v_rp = 0.7, v_m_cost = 1.08339283366, v_rm = 0.7
取出10前有这些容器： [10, 12, 16, 33]
取出10后有： [12, 16, 33] v_p_cost=1.29235563003, v_rp = 0.7, v_m_cost = 0.948430587421, v_rm = 0.7
取出33前有这些容器： [12, 16, 33]
取出33后有： [12, 16] v_p_cost=0.99496266455, v_rp = 0.7, v_m_cost = 0.639905467854, v_rm = 0.7
取出16前有这些容器： [12, 16]
取出16后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.7
修改hm过载  h_id = 2, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 1.0]
11
修改hm过载  h_id = 4, h_p_cost = 1.5, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [9, 21]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.3]
21
修改hm过载  h_id = 5, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 16, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [29, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.3]
29
修改hm过载  h_id = 20, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 23, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 30]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 24, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 25, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 8]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
8
修改hm过载  h_id = 34, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 14]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 36, h_p_cost = 2.5, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [20, 24, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 1.0],mem尺寸[0.7, 0.5, 0.7]
20
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
24
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [36, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 45, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
25
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [5, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
5
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [41, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
45
进入mbbode_rank
[4, 10, 6, 12, 8] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 8, 4: 22, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 21: 9, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 31: 29, 32: 47, 34: 23, 36: 49, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 3]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 0.7]
3
修改hm过载  h_id = 22, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 2, v_p_cost = 1.12501615324, v_rp = 1.0, v_m_cost = 1.28318584142, v_rm = 1.0
取出37前有这些容器： [8, 23, 37]
取出37后有： [8, 23] v_p_cost=0.813841757817, v_rp = 1.0, v_m_cost = 0.83261908543, v_rm = 1.0
修改vm超载的情况 v_id = 13, v_p_cost = 0.38598108439, v_rp = 0.3, v_m_cost = 0.232894049136, v_rm = 0.3
取出40前有这些容器： [35, 36, 40, 42]
取出40后有： [35, 36, 42] v_p_cost=0.364085799818, v_rp = 0.3, v_m_cost = 0.219856002868, v_rm = 0.3
取出36前有这些容器： [35, 36, 42]
取出36后有： [35, 42] v_p_cost=0.298391584815, v_rp = 0.3, v_m_cost = 0.16175652632, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.5
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 23, v_p_cost = 0.978316261028, v_rp = 0.7, v_m_cost = 0.803390549374, v_rm = 0.5
取出47前有这些容器： [16, 47]
取出47后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.891890556433, v_rp = 0.7, v_m_cost = 0.651330182416, v_rm = 0.5
取出45前有这些容器： [1, 41, 45]
取出45后有： [1, 41] v_p_cost=0.804710637597, v_rp = 0.7, v_m_cost = 0.629957467753, v_rm = 0.5
取出1前有这些容器： [1, 41]
取出1后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 0.748248899243, v_rp = 0.7, v_m_cost = 0.776218078153, v_rm = 0.7
取出22前有这些容器： [5, 22]
取出22后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.7
修改hm过载  h_id = 7, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [27, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.7]
27
修改hm过载  h_id = 8, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 18, h_p_cost = 0.8, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 16]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 24, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [13, 15, 30]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.7],mem尺寸[0.3, 0.5, 0.7]
13
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 28, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 6]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 43, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
33
修改hm过载  h_id = 48, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.779351933545, v_rp = 0.7, v_m_cost = 0.643633917992, v_rm = 1.0
取出38前有这些容器： [12, 38]
取出38后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.772092521374, v_rp = 0.5, v_m_cost = 0.756591400475, v_rm = 0.7
取出37前有这些容器： [24, 37]
取出37后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 0, h_p_cost = 3.0, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [7, 19, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 1.0],mem尺寸[0.7, 1.0, 0.7]
7
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
19
修改hm过载  h_id = 3, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.7]
22
修改hm过载  h_id = 4, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 5]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
5
修改hm过载  h_id = 7, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 11, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [23, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 13, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [33, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 19, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 25]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 23, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [35, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.5]
41
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.11481219831, v_rp = 0.5, v_m_cost = 1.3302159955, v_rm = 0.5
取出9前有这些容器： [8, 9, 47]
取出9后有： [8, 47] v_p_cost=0.833977446668, v_rp = 0.5, v_m_cost = 0.845885437852, v_rm = 0.5
取出8前有这些容器： [8, 47]
取出8后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.479873774184, v_rp = 0.3, v_m_cost = 0.594667395232, v_rm = 0.3
取出6前有这些容器： [6, 19]
取出6后有： [19] v_p_cost=0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.4247145978, v_rp = 0.5, v_m_cost = 0.515300155478, v_rm = 0.3
取出30前有这些容器： [30, 38]
取出30后有： [38] v_p_cost=0.281729099678, v_rp = 0.5, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 0.938846406114, v_rp = 0.7, v_m_cost = 0.742887098129, v_rm = 1.0
取出24前有这些容器： [14, 24]
取出24后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 1.0
修改vm超载的情况 v_id = 26, v_p_cost = 1.03700894354, v_rp = 0.5, v_m_cost = 0.939215927643, v_rm = 0.7
取出40前有这些容器： [4, 5, 12, 40]
取出40后有： [4, 5, 12] v_p_cost=1.01511365897, v_rp = 0.5, v_m_cost = 0.926177881375, v_rm = 0.7
取出4前有这些容器： [4, 5, 12]
取出4后有： [5, 12] v_p_cost=0.914606966566, v_rp = 0.5, v_m_cost = 0.823580714449, v_rm = 0.7
取出5前有这些容器： [5, 12]
取出5后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 28, v_p_cost = 0.633385297308, v_rp = 1.0, v_m_cost = 0.730629445534, v_rm = 0.5
取出15前有这些容器： [15, 25, 37]
取出15后有： [25, 37] v_p_cost=0.483623484834, v_rp = 1.0, v_m_cost = 0.517327345208, v_rm = 0.5
取出25前有这些容器： [25, 37]
取出25后有： [37] v_p_cost=0.311174395419, v_rp = 1.0, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.653449490027, v_rp = 0.5, v_m_cost = 0.727883729123, v_rm = 0.7
取出29前有这些容器： [2, 29, 44, 48]
取出29后有： [2, 44, 48] v_p_cost=0.558943849041, v_rp = 0.5, v_m_cost = 0.635005485425, v_rm = 0.7
取出2前有这些容器： [2, 44, 48]
取出2后有： [44, 48] v_p_cost=0.455800965133, v_rp = 0.5, v_m_cost = 0.447288500489, v_rm = 0.7
修改vm超载的情况 v_id = 43, v_p_cost = 0.818206006766, v_rp = 1.0, v_m_cost = 0.752720007108, v_rm = 0.7
取出31前有这些容器： [31, 41]
取出31后有： [41] v_p_cost=0.420969578467, v_rp = 1.0, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.711469373718, v_rp = 0.5, v_m_cost = 0.63524979682, v_rm = 1.0
取出27前有这些容器： [18, 27, 34]
取出27后有： [18, 34] v_p_cost=0.697141189146, v_rp = 0.5, v_m_cost = 0.600338465954, v_rm = 1.0
取出34前有这些容器： [18, 34]
取出34后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 1.0
修改hm过载  h_id = 3, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [17, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.3]
21
修改hm过载  h_id = 4, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 6, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [31, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
31
修改hm过载  h_id = 12, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 13, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 23]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 17, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [26, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 19, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [42, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 29, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 33]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
33
修改hm过载  h_id = 30, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
修改hm过载  h_id = 45, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [9, 11]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
25
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.462930643302, v_rp = 0.3, v_m_cost = 0.500641035507, v_rm = 0.7
取出36前有这些容器： [31, 36]
取出36后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.44445098347, v_rp = 0.3, v_m_cost = 0.324406953571, v_rm = 1.0
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 6, v_p_cost = 1.1568178928, v_rp = 0.7, v_m_cost = 0.934331719705, v_rm = 0.7
取出30前有这些容器： [14, 22, 30, 42]
取出30后有： [14, 22, 42] v_p_cost=1.01383239468, v_rp = 0.7, v_m_cost = 0.739022162855, v_rm = 0.7
取出42前有这些容器： [14, 22, 42]
取出42后有： [14, 22] v_p_cost=0.809193046702, v_rp = 0.7, v_m_cost = 0.71314313671, v_rm = 0.7
取出22前有这些容器： [14, 22]
取出22后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.82910782905, v_rp = 0.5, v_m_cost = 0.747246346285, v_rm = 0.7
取出18前有这些容器： [18, 23]
取出18后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 26, v_p_cost = 0.740104209063, v_rp = 0.5, v_m_cost = 0.598952785349, v_rm = 0.7
取出11前有这些容器： [11, 41]
取出11后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.3
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 28, v_p_cost = 1.02493339953, v_rp = 1.0, v_m_cost = 0.82303237056, v_rm = 0.5
取出26前有这些容器： [16, 26, 43]
取出26后有： [16, 43] v_p_cost=0.814561051704, v_rp = 1.0, v_m_cost = 0.599459601919, v_rm = 0.5
取出43前有这些容器： [16, 43]
取出43后有： [16] v_p_cost=0.497339830683, v_rp = 1.0, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.280834751639, v_rp = 0.5, v_m_cost = 0.484330557644, v_rm = 0.3
取出9前有这些容器： [9]
取出9后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.707178906636, v_rp = 0.5, v_m_cost = 0.601648654344, v_rm = 1.0
取出34前有这些容器： [7, 34]
取出34后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.8, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [4, 26, 38]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 1.0],mem尺寸[1.0, 0.7, 0.7]
4
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 16, h_p_cost = 2.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [7, 29, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0],mem尺寸[0.7, 0.3, 0.5]
29
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
7
修改hm过载  h_id = 26, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [42, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
42
修改hm过载  h_id = 29, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 31, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [12, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
12
修改hm过载  h_id = 33, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [25, 27, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.3],mem尺寸[0.7, 0.3, 0.5]
40
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
25
修改hm过载  h_id = 34, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 41, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [14, 28]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
14
修改hm过载  h_id = 44, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 37]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
进入mbbode_rank
[4, 9, 12, 9, 6] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 8, 4: 22, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 21: 9, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 31: 29, 32: 47, 34: 23, 36: 49, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 5]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 22, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 4]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 12, v_p_cost = 0.669404718991, v_rp = 0.5, v_m_cost = 0.783680041019, v_rm = 0.7
取出36前有这些容器： [32, 36, 47]
取出36后有： [32, 47] v_p_cost=0.603710503988, v_rp = 0.5, v_m_cost = 0.725580564471, v_rm = 0.7
取出32前有这些容器： [32, 47]
取出32后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.510736369541, v_rp = 0.3, v_m_cost = 0.63581489526, v_rm = 0.3
取出35前有这些容器： [5, 35]
取出35后有： [5] v_p_cost=0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 0.865606918238, v_rp = 0.7, v_m_cost = 0.589646446313, v_rm = 0.5
取出18前有这些容器： [16, 18]
取出18后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 0.567219471474, v_rp = 1.0, v_m_cost = 0.519754593138, v_rm = 0.5
取出13前有这些容器： [1, 13]
取出13后有： [1] v_p_cost=0.38374105913, v_rp = 1.0, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 28, v_p_cost = 0.934291504359, v_rp = 1.0, v_m_cost = 0.923583239549, v_rm = 0.5
取出30前有这些容器： [19, 30, 46]
取出30后有： [19, 46] v_p_cost=0.791306006237, v_rp = 1.0, v_m_cost = 0.728273682699, v_rm = 0.5
取出46前有这些容器： [19, 46]
取出46后有： [19] v_p_cost=0.395682499698, v_rp = 1.0, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.522588421885, v_rp = 0.7, v_m_cost = 0.459369199806, v_rm = 0.3
取出10前有这些容器： [10, 17]
取出10后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 14, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 23, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 34, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 44]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
44
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [12, 29, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.5],mem尺寸[0.7, 0.3, 1.0]
12
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.3, 1.0]
29
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
20
修改hm过载  h_id = 44, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
46
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.684036977212, v_rp = 0.3, v_m_cost = 0.357344132215, v_rm = 1.0
取出28前有这些容器： [16, 28]
取出28后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 1.0
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.789792227546, v_rp = 0.5, v_m_cost = 0.632978812617, v_rm = 0.7
取出34前有这些容器： [24, 34]
取出34后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 0.743647851923, v_rp = 1.0, v_m_cost = 0.87062417408, v_rm = 0.7
取出32前有这些容器： [14, 30, 32]
取出32后有： [14, 30] v_p_cost=0.620913778281, v_rp = 1.0, v_m_cost = 0.632172010492, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.876335089781, v_rp = 0.5, v_m_cost = 0.905288100548, v_rm = 0.7
取出10前有这些容器： [10, 43, 47]
取出10后有： [43, 47] v_p_cost=0.798197651366, v_rp = 0.5, v_m_cost = 0.770325854313, v_rm = 0.7
取出43前有这些容器： [43, 47]
取出43后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.54861492946, v_rp = 0.5, v_m_cost = 0.326942272402, v_rm = 0.3
取出45前有这些容器： [0, 45]
取出45后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 24, v_p_cost = 0.593489096613, v_rp = 1.0, v_m_cost = 0.613901358033, v_rm = 0.5
取出27前有这些容器： [13, 19, 27]
取出27后有： [13, 19] v_p_cost=0.579160912042, v_rp = 1.0, v_m_cost = 0.578990027167, v_rm = 0.5
取出13前有这些容器： [13, 19]
取出13后有： [19] v_p_cost=0.395682499698, v_rp = 1.0, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 30, v_p_cost = 0.676458258179, v_rp = 0.7, v_m_cost = 0.83358978671, v_rm = 0.7
取出9前有这些容器： [9, 46]
取出9后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.723421882435, v_rp = 0.5, v_m_cost = 0.683446215117, v_rm = 0.5
取出48前有这些容器： [1, 48]
取出48后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.5
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.789236666023, v_rp = 0.5, v_m_cost = 0.583562745972, v_rm = 1.0
取出18前有这些容器： [18, 41]
取出18后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 1.0
修改vm超载的情况 v_id = 49, v_p_cost = 0.491897890481, v_rp = 1.0, v_m_cost = 0.543696358774, v_rm = 0.5
取出4前有这些容器： [4, 20]
取出4后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.5
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 34]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 16, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [41, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
41
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [17, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 27, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 32, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
6
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
33
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.714377098183, v_rp = 0.5, v_m_cost = 0.808462514652, v_rm = 0.5
取出33前有这些容器： [5, 33]
取出33后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 11, v_p_cost = 0.746571892601, v_rp = 0.7, v_m_cost = 0.548078784037, v_rm = 0.5
取出18前有这些容器： [7, 18]
取出18后有： [7] v_p_cost=0.378304805046, v_rp = 0.7, v_m_cost = 0.274694486214, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 0.3
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 25, v_p_cost = 0.667753704332, v_rp = 0.5, v_m_cost = 0.588800320971, v_rm = 0.7
取出27前有这些容器： [25, 27, 47]
取出27后有： [25, 47] v_p_cost=0.65342551976, v_rp = 0.5, v_m_cost = 0.553888990104, v_rm = 0.7
取出25前有这些容器： [25, 47]
取出25后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.8281920426, v_rp = 0.5, v_m_cost = 0.644185973176, v_rm = 0.5
取出1前有这些容器： [1, 17]
取出1后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 0.499880679294, v_rp = 0.7, v_m_cost = 0.514644915758, v_rm = 0.5
取出36前有这些容器： [29, 36, 48]
取出36后有： [29, 48] v_p_cost=0.434186464291, v_rp = 0.7, v_m_cost = 0.45654543921, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.970459327794, v_rp = 0.7, v_m_cost = 1.09815977282, v_rm = 0.5
取出15前有这些容器： [15, 37, 39, 43]
取出15后有： [37, 39, 43] v_p_cost=0.820697515319, v_rp = 0.7, v_m_cost = 0.884857672495, v_rm = 0.5
取出39前有这些容器： [37, 39, 43]
取出39后有： [37, 43] v_p_cost=0.628395616439, v_rp = 0.7, v_m_cost = 0.733764209418, v_rm = 0.5
取出37前有这些容器： [37, 43]
取出37后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.3
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 44, v_p_cost = 0.865354501157, v_rp = 0.7, v_m_cost = 0.821965420797, v_rm = 0.5
取出45前有这些容器： [9, 16, 45]
取出45后有： [9, 16] v_p_cost=0.778174582322, v_rp = 0.7, v_m_cost = 0.800592706134, v_rm = 0.5
取出9前有这些容器： [9, 16]
取出9后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 16]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 3, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [31, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
31
修改hm过载  h_id = 6, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [36, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 18, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [10, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.3]
10
修改hm过载  h_id = 21, h_p_cost = 1.7, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [9, 39]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.3]
39
修改hm过载  h_id = 23, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
20
修改hm过载  h_id = 28, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 24]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 35, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 39, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.5]
42
修改hm过载  h_id = 44, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 29, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.5],mem尺寸[0.7, 0.3, 0.7]
3
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.485474099613, v_rp = 0.5, v_m_cost = 0.510209583789, v_rm = 0.5
取出42前有这些容器： [9, 42]
取出42后有： [9] v_p_cost=0.280834751639, v_rp = 0.5, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.433961302559, v_rp = 0.3, v_m_cost = 0.331483774371, v_rm = 0.7
取出36前有这些容器： [18, 36]
取出36后有： [18] v_p_cost=0.368267087556, v_rp = 0.3, v_m_cost = 0.273384297823, v_rm = 0.7
取出18前有这些容器： [18]
取出18后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.925427413815, v_rp = 0.3, v_m_cost = 0.811535354455, v_rm = 1.0
取出17前有这些容器： [17, 47]
取出17后有： [47] v_p_cost=0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 1.0
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 9, v_p_cost = 1.4068367083, v_rp = 1.0, v_m_cost = 1.22982318264, v_rm = 0.5
取出33前有这些容器： [0, 11, 33, 34]
取出33后有： [0, 11, 34] v_p_cost=1.10944374281, v_rp = 1.0, v_m_cost = 0.92129806307, v_rm = 0.5
取出11前有这些容器： [0, 11, 34]
取出11后有： [0, 34] v_p_cost=0.790309112215, v_rp = 1.0, v_m_cost = 0.63252372587, v_rm = 0.5
取出34前有这些容器： [0, 34]
取出34后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.582379646227, v_rp = 0.5, v_m_cost = 0.420096437358, v_rm = 1.0
取出28前有这些容器： [19, 28]
取出28后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 1.0
修改vm超载的情况 v_id = 17, v_p_cost = 0.921776949387, v_rp = 0.7, v_m_cost = 1.13773090478, v_rm = 0.7
取出15前有这些容器： [15, 23, 37]
取出15后有： [23, 37] v_p_cost=0.772015136913, v_rp = 0.7, v_m_cost = 0.92442880445, v_rm = 0.7
取出37前有这些容器： [23, 37]
取出37后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.524908351192, v_rp = 0.5, v_m_cost = 0.609044431817, v_rm = 0.5
取出35前有这些容器： [32, 35, 39, 44]
取出35后有： [32, 39, 44] v_p_cost=0.431156114351, v_rp = 0.5, v_m_cost = 0.473166931642, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.640608331989, v_rp = 0.7, v_m_cost = 0.518952876214, v_rm = 0.5
取出30前有这些容器： [12, 30]
取出30后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.856541632495, v_rp = 0.7, v_m_cost = 0.655283873552, v_rm = 0.3
取出46前有这些容器： [24, 46]
取出46后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.3
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 8, h_p_cost = 1.3, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 7]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [27, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.5]
31
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 41]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 36, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 37, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
6
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [36, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
进入mbbode_rank
[4, 6, 11, 9, 10] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [31, 29], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 8, 4: 22, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 21: 9, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 31: 29, 32: 47, 34: 23, 36: 49, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 22, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 10, v_p_cost = 0.790309112215, v_rp = 0.5, v_m_cost = 0.63252372587, v_rm = 0.5
取出34前有这些容器： [0, 34]
取出34后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.63073824282, v_rp = 0.5, v_m_cost = 0.700430501209, v_rm = 0.7
取出15前有这些容器： [15, 47]
取出15后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.676049319437, v_rp = 0.5, v_m_cost = 0.486980308904, v_rm = 0.7
取出2前有这些容器： [2, 18, 42]
取出2后有： [18, 42] v_p_cost=0.572906435529, v_rp = 0.5, v_m_cost = 0.299263323968, v_rm = 0.7
取出42前有这些容器： [18, 42]
取出42后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.7
修改vm超载的情况 v_id = 28, v_p_cost = 0.579160912042, v_rp = 1.0, v_m_cost = 0.578990027167, v_rm = 0.5
取出13前有这些容器： [13, 19]
取出13后有： [19] v_p_cost=0.395682499698, v_rp = 1.0, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.736118763295, v_rp = 0.5, v_m_cost = 0.788711732285, v_rm = 0.3
取出11前有这些容器： [5, 11]
取出11后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 41, v_p_cost = 0.720547134206, v_rp = 0.7, v_m_cost = 0.394157948369, v_rm = 0.5
取出45前有这些容器： [24, 25, 45]
取出45后有： [24, 25] v_p_cost=0.633367215371, v_rp = 0.7, v_m_cost = 0.372785233707, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 8]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 7, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 28]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 8, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [42, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
42
修改hm过载  h_id = 19, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.567185057112, v_rp = 0.5, v_m_cost = 0.562859117159, v_rm = 0.5
取出32前有这些容器： [17, 32]
取出32后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 9, v_p_cost = 0.586804317426, v_rp = 1.0, v_m_cost = 0.704402852334, v_rm = 0.5
取出6前有这些容器： [6, 11, 13]
取出6后有： [11, 13] v_p_cost=0.50261304294, v_rp = 1.0, v_m_cost = 0.488749910734, v_rm = 0.5
修改vm超载的情况 v_id = 10, v_p_cost = 1.08922357656, v_rp = 0.5, v_m_cost = 0.953950493722, v_rm = 0.5
取出3前有这些容器： [3, 16, 20, 30]
取出3后有： [16, 20, 30] v_p_cost=1.03171652688, v_rp = 0.5, v_m_cost = 0.952670897187, v_rm = 0.5
取出30前有这些容器： [16, 20, 30]
取出30后有： [16, 20] v_p_cost=0.888731028759, v_rp = 0.5, v_m_cost = 0.757361340338, v_rm = 0.5
取出20前有这些容器： [16, 20]
取出20后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.663880056554, v_rp = 0.5, v_m_cost = 0.684926972535, v_rm = 0.7
取出4前有这些容器： [4, 8, 26]
取出4后有： [8, 26] v_p_cost=0.56337336415, v_rp = 0.5, v_m_cost = 0.582329805609, v_rm = 0.7
取出26前有这些容器： [8, 26]
取出26后有： [8] v_p_cost=0.353001016323, v_rp = 0.5, v_m_cost = 0.358757036968, v_rm = 0.7
修改vm超载的情况 v_id = 17, v_p_cost = 0.659139556685, v_rp = 0.7, v_m_cost = 0.759025043858, v_rm = 0.7
取出9前有这些容器： [7, 9]
取出9后有： [7] v_p_cost=0.378304805046, v_rp = 0.7, v_m_cost = 0.274694486214, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.707947910861, v_rp = 0.5, v_m_cost = 0.637051493335, v_rm = 0.7
取出48前有这些容器： [18, 48]
取出48后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 0.856523241192, v_rp = 1.0, v_m_cost = 0.852876502094, v_rm = 0.5
取出19前有这些容器： [19, 23]
取出19后有： [23] v_p_cost=0.460840741494, v_rp = 1.0, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 25, v_p_cost = 1.35629427279, v_rp = 0.5, v_m_cost = 1.07175443606, v_rm = 0.7
取出31前有这些容器： [0, 12, 31]
取出31后有： [0, 12] v_p_cost=0.959057844492, v_rp = 0.5, v_m_cost = 0.629212877103, v_rm = 0.7
取出0前有这些容器： [0, 12]
取出0后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 49, v_p_cost = 0.752234345011, v_rp = 1.0, v_m_cost = 0.586459131217, v_rm = 0.5
取出22前有这些容器： [22, 41]
取出22后有： [41] v_p_cost=0.420969578467, v_rp = 1.0, v_m_cost = 0.310178448149, v_rm = 0.5
修改hm过载  h_id = 11, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 13, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 15, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [9, 10]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [17, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
42
修改hm过载  h_id = 41, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 8]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 44, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [27, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.3]
29
修改hm过载  h_id = 47, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 16]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 49, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [14, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
14
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.913893372667, v_rp = 0.5, v_m_cost = 0.794606797162, v_rm = 0.7
取出6前有这些容器： [0, 6, 18]
取出6后有： [0, 18] v_p_cost=0.829702098181, v_rp = 0.5, v_m_cost = 0.578953855562, v_rm = 0.7
取出18前有这些容器： [0, 18]
取出18后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.789792227546, v_rp = 1.0, v_m_cost = 0.632978812617, v_rm = 0.5
取出34前有这些容器： [24, 34]
取出34后有： [24] v_p_cost=0.460918125956, v_rp = 1.0, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.5
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.468426246207, v_rp = 0.7, v_m_cost = 0.361072582353, v_rm = 0.3
取出28前有这些容器： [28, 38]
取出28后有： [38] v_p_cost=0.281729099678, v_rp = 0.7, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 1.10259991102, v_rp = 0.5, v_m_cost = 1.01294482211, v_rm = 0.7
取出42前有这些容器： [5, 42, 47]
取出42后有： [5, 47] v_p_cost=0.897960563044, v_rp = 0.5, v_m_cost = 0.987065795968, v_rm = 0.7
取出5前有这些容器： [5, 47]
取出5后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.607608776126, v_rp = 0.3, v_m_cost = 0.6661143276, v_rm = 0.5
取出26前有这些容器： [26, 31]
取出26后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.5
修改hm过载  h_id = 11, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 46]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 28, h_p_cost = 2.4, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 24, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.7],mem尺寸[1.0, 0.5, 0.5]
1
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
36
修改hm过载  h_id = 31, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [42, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 47, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 29]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 48, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 10]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
5
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.644319153838, v_rp = 0.5, v_m_cost = 0.673837621995, v_rm = 0.5
取出13前有这些容器： [13, 23]
取出13后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 1.01863013385, v_rp = 0.3, v_m_cost = 0.786266191553, v_rm = 0.7
取出30前有这些容器： [7, 16, 30]
取出30后有： [7, 16] v_p_cost=0.875644635729, v_rp = 0.3, v_m_cost = 0.590956634703, v_rm = 0.7
取出7前有这些容器： [7, 16]
取出7后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.7
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 1.51346907832, v_rp = 1.0, v_m_cost = 1.57229087417, v_rm = 0.7
取出15前有这些容器： [8, 15, 18, 22, 37]
取出15后有： [8, 18, 22, 37] v_p_cost=1.36370726584, v_rp = 1.0, v_m_cost = 1.35898877385, v_rm = 0.7
取出37前有这些容器： [8, 18, 22, 37]
取出37后有： [8, 18, 22] v_p_cost=1.05253287042, v_rp = 1.0, v_m_cost = 0.908422017859, v_rm = 0.7
取出22前有这些容器： [8, 18, 22]
取出22后有： [8, 18] v_p_cost=0.721268103879, v_rp = 1.0, v_m_cost = 0.632141334791, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.305146040378, v_rp = 0.3, v_m_cost = 0.128476193071, v_rm = 0.5
取出4前有这些容器： [4, 42]
取出4后有： [42] v_p_cost=0.204639347974, v_rp = 0.3, v_m_cost = 0.0258790261448, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.3
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 37, v_p_cost = 0.51212991272, v_rp = 0.5, v_m_cost = 0.430427784732, v_rm = 0.7
取出25前有这些容器： [25, 48]
取出25后有： [48] v_p_cost=0.339680823305, v_rp = 0.5, v_m_cost = 0.363667195512, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.727620104952, v_rp = 0.7, v_m_cost = 0.589247944427, v_rm = 0.3
取出33前有这些容器： [21, 33]
取出33后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.444994243418, v_rp = 0.3, v_m_cost = 0.410575473108, v_rm = 0.5
取出44前有这些容器： [34, 44]
取出44后有： [34] v_p_cost=0.32887410159, v_rp = 0.3, v_m_cost = 0.326954168131, v_rm = 0.5
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.676458258179, v_rp = 0.7, v_m_cost = 0.83358978671, v_rm = 0.5
取出9前有这些容器： [9, 46]
取出9后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 3.2, h_m_cost = 3.0
该物理机上放置的虚拟机为：  [22, 29, 35, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 1.0, 1.0],mem尺寸[1.0, 0.3, 1.0, 0.7]
29
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 1.0],mem尺寸[1.0, 1.0, 0.7]
22
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
35
修改hm过载  h_id = 2, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 11, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 0.3],mem尺寸[0.7, 0.5, 0.5]
40
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
11
修改hm过载  h_id = 15, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [27, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.5]
42
修改hm过载  h_id = 17, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [34, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 21, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 30]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 27, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [32, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 30, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 37]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 34, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 16]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
10
修改hm过载  h_id = 35, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 37, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [41, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 39, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 9]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 47, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 48, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
进入mbbode_rank
[4, 8, 7, 12, 9] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [3, 8], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [21, 9], [1, 34], [7, 30], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改hm过载  h_id = 8, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 37]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.406314549432, v_rp = 0.3, v_m_cost = 0.310147051863, v_rm = 1.0
取出45前有这些容器： [11, 45]
取出45后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 1.0
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 10, v_p_cost = 0.858671438924, v_rp = 0.5, v_m_cost = 0.748111116698, v_rm = 0.5
取出31前有这些容器： [0, 31]
取出31后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 19, v_p_cost = 0.844278669946, v_rp = 1.0, v_m_cost = 1.03412545605, v_rm = 1.0
取出44前有这些容器： [5, 37, 44]
取出44后有： [5, 37] v_p_cost=0.728158528118, v_rp = 1.0, v_m_cost = 0.950504151073, v_rm = 1.0
修改vm超载的情况 v_id = 30, v_p_cost = 0.787014704616, v_rp = 0.7, v_m_cost = 0.790358420914, v_rm = 0.7
取出20前有这些容器： [20, 46]
取出20后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.64571176744, v_rp = 0.7, v_m_cost = 0.562234985247, v_rm = 0.5
取出35前有这些容器： [21, 35, 49]
取出35后有： [21, 49] v_p_cost=0.551959530598, v_rp = 0.7, v_m_cost = 0.426357485071, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.473136650519, v_rp = 0.3, v_m_cost = 0.635424020722, v_rm = 0.5
取出39前有这些容器： [9, 39]
取出39后有： [9] v_p_cost=0.280834751639, v_rp = 0.3, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 1.05433679384, v_rp = 0.7, v_m_cost = 0.682963681855, v_rm = 0.5
取出25前有这些容器： [24, 25, 41]
取出25后有： [24, 41] v_p_cost=0.881887704423, v_rp = 0.7, v_m_cost = 0.616203092635, v_rm = 0.5
取出41前有这些容器： [24, 41]
取出41后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.978599264212, v_rp = 0.5, v_m_cost = 0.810771720248, v_rm = 1.0
取出47前有这些容器： [12, 47]
取出47后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 36]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 37, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 6]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [20, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
20
修改hm过载  h_id = 46, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [34, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 1.0]
34
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 18, v_p_cost = 0.924483576007, v_rp = 0.7, v_m_cost = 0.708683229539, v_rm = 0.3
取出45前有这些容器： [12, 45, 48]
取出45后有： [12, 48] v_p_cost=0.837303657172, v_rp = 0.7, v_m_cost = 0.687310514876, v_rm = 0.3
取出48前有这些容器： [12, 48]
取出48后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 2.13131639539, v_rp = 0.7, v_m_cost = 1.67366799851, v_rm = 1.0
取出44前有这些容器： [7, 18, 21, 34, 39, 43, 44]
取出44后有： [7, 18, 21, 34, 39, 43] v_p_cost=2.01519625356, v_rp = 0.7, v_m_cost = 1.59004669353, v_rm = 1.0
取出39前有这些容器： [7, 18, 21, 34, 39, 43]
取出39后有： [7, 18, 21, 34, 43] v_p_cost=1.82289435468, v_rp = 0.7, v_m_cost = 1.43895323046, v_rm = 1.0
取出43前有这些容器： [7, 18, 21, 34, 43]
取出43后有： [7, 18, 21, 34] v_p_cost=1.50567313366, v_rp = 0.7, v_m_cost = 1.15575577703, v_rm = 1.0
取出34前有这些容器： [7, 18, 21, 34]
取出34后有： [7, 18, 21] v_p_cost=1.17679903207, v_rp = 0.7, v_m_cost = 0.828801608896, v_rm = 1.0
取出18前有这些容器： [7, 18, 21]
取出18后有： [7, 21] v_p_cost=0.808531944514, v_rp = 0.7, v_m_cost = 0.555417311073, v_rm = 1.0
取出7前有这些容器： [7, 21]
取出7后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 1.0
修改vm超载的情况 v_id = 27, v_p_cost = 0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.741843948953, v_rp = 0.5, v_m_cost = 0.632932073139, v_rm = 0.7
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.761811181984, v_rp = 0.5, v_m_cost = 0.971458958528, v_rm = 1.0
取出9前有这些容器： [9, 47]
取出9后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 1.0
修改hm过载  h_id = 3, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 13, h_p_cost = 0.8, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 20, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 34, h_p_cost = 2.4, h_m_cost = 1.8
该物理机上放置的虚拟机为：  [8, 11, 21, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.5, 0.7],mem尺寸[0.7, 0.5, 0.3, 0.3]
8
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.7],mem尺寸[0.5, 0.3, 0.3]
21
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.3]
11
修改hm过载  h_id = 45, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
30
修改hm过载  h_id = 47, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 48, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.583933574828, v_rp = 0.5, v_m_cost = 0.483623542684, v_rm = 0.5
取出28前有这些容器： [28, 31]
取出28后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.5
修改vm超载的情况 v_id = 8, v_p_cost = 0.816474461279, v_rp = 0.5, v_m_cost = 0.60503648569, v_rm = 0.7
取出11前有这些容器： [11, 16]
取出11后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.610679938431, v_rp = 1.0, v_m_cost = 0.519326744812, v_rm = 0.5
取出15前有这些容器： [15, 24]
取出15后有： [24] v_p_cost=0.460918125956, v_rp = 1.0, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.600321847671, v_rp = 0.5, v_m_cost = 0.404893479778, v_rm = 0.7
取出42前有这些容器： [19, 42]
取出42后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.489375743381, v_rp = 0.3, v_m_cost = 0.485136729241, v_rm = 0.3
取出35前有这些容器： [35, 46]
取出35后有： [46] v_p_cost=0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.3
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.535435329841, v_rp = 0.3, v_m_cost = 0.438142050177, v_rm = 0.5
取出3前有这些容器： [3, 14]
取出3后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.795015799351, v_rp = 0.7, v_m_cost = 0.632168438932, v_rm = 0.3
取出33前有这些容器： [12, 33]
取出33后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 0.610603201268, v_rp = 0.5, v_m_cost = 0.646944766759, v_rm = 0.7
取出38前有这些容器： [34, 38]
取出38后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 0.833977446668, v_rp = 1.0, v_m_cost = 0.845885437852, v_rm = 0.5
取出8前有这些容器： [8, 47]
取出8后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.431312317271, v_rp = 0.5, v_m_cost = 0.534848725951, v_rm = 0.3
取出27前有这些容器： [5, 27]
取出27后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 39, v_p_cost = 0.533370023376, v_rp = 0.7, v_m_cost = 0.468439809795, v_rm = 0.3
取出2前有这些容器： [2, 21]
取出2后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.3
修改vm超载的情况 v_id = 49, v_p_cost = 0.822755788515, v_rp = 1.0, v_m_cost = 0.599101439785, v_rm = 0.5
取出7前有这些容器： [7, 17]
取出7后有： [17] v_p_cost=0.44445098347, v_rp = 1.0, v_m_cost = 0.324406953571, v_rm = 0.5
修改hm过载  h_id = 10, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [17, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
17
修改hm过载  h_id = 23, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 3]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 0.7]
3
修改hm过载  h_id = 27, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 29, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [34, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
34
修改hm过载  h_id = 32, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [9, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
46
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [20, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
20
修改hm过载  h_id = 42, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [14, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
14
修改hm过载  h_id = 43, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 45, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [32, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.5]
42
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.5]
31
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
12
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.758233706978, v_rp = 0.5, v_m_cost = 0.782387168029, v_rm = 0.5
取出33前有这些容器： [23, 33]
取出33后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.505831777125, v_rp = 0.3, v_m_cost = 0.329856320925, v_rm = 0.7
取出28前有这些容器： [11, 28]
取出28后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 0.7
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 1.19293410583, v_rp = 0.3, v_m_cost = 1.03292215632, v_rm = 1.0
取出22前有这些容器： [1, 14, 22]
取出22后有： [1, 14] v_p_cost=0.861669339289, v_rp = 0.3, v_m_cost = 0.756641473247, v_rm = 1.0
取出1前有这些容器： [1, 14]
取出1后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 1.0
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=1.11022302463e-16, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 1.0
修改vm超载的情况 v_id = 8, v_p_cost = 0.677352606218, v_rp = 0.5, v_m_cost = 0.669249827694, v_rm = 0.7
取出38前有这些容器： [38, 46]
取出38后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 17, v_p_cost = 0.778174582322, v_rp = 0.7, v_m_cost = 0.800592706134, v_rm = 0.7
取出9前有这些容器： [9, 16]
取出9后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.265719571765, v_rp = 0.7, v_m_cost = 0.433761720437, v_rm = 0.3
取出32前有这些容器： [30, 32]
取出32后有： [30] v_p_cost=0.142985498122, v_rp = 0.7, v_m_cost = 0.19530955685, v_rm = 0.3
修改vm超载的情况 v_id = 24, v_p_cost = 0.511489773685, v_rp = 1.0, v_m_cost = 0.592815638783, v_rm = 0.5
取出29前有这些容器： [5, 29]
取出29后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.272396367661, v_rp = 0.5, v_m_cost = 0.373436913336, v_rm = 0.3
取出10前有这些容器： [4, 10, 35]
取出10后有： [4, 35] v_p_cost=0.194258929246, v_rp = 0.5, v_m_cost = 0.238474667102, v_rm = 0.3
修改vm超载的情况 v_id = 30, v_p_cost = 0.942073817337, v_rp = 0.7, v_m_cost = 0.648050272935, v_rm = 0.7
取出17前有这些容器： [12, 17]
取出17后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 32, v_p_cost = 0.878927272722, v_rp = 1.0, v_m_cost = 0.914194132284, v_rm = 0.7
取出26前有这些容器： [26, 34, 48]
取出26后有： [34, 48] v_p_cost=0.668554924895, v_rp = 1.0, v_m_cost = 0.690621363643, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.395682499698, v_rp = 0.7, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 46, v_p_cost = 1.36338101944, v_rp = 0.7, v_m_cost = 1.10287640677, v_rm = 0.7
取出41前有这些容器： [0, 41, 47]
取出41后有： [0, 47] v_p_cost=0.94241144097, v_rp = 0.7, v_m_cost = 0.792697958623, v_rm = 0.7
取出0前有这些容器： [0, 47]
取出0后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [26, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 1, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [32, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
41
修改hm过载  h_id = 4, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 9, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 8]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 23, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 25, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 4]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 31, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [21, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.3, 1.0]
21
修改hm过载  h_id = 34, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [48, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
48
修改hm过载  h_id = 36, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 24]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
7
修改hm过载  h_id = 42, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [29, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 47, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [17, 28]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
17
修改hm过载  h_id = 48, h_p_cost = 1.7, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [27, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 1.0]
27
进入mbbode_rank
[2, 10, 8, 9, 11] 0
上代结果： 14866.4024847 1.05974629716 783500.399526 1625.0
本代结果替代后： 14866.4024847 1.57037331834 783500.388562 1430.0
执行全局精英解替换： 14866.4024847 1.57037331834 783500.388562 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 22], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 22], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [37, 8], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 37, v_p_cost = 0.858077169793, v_rp = 0.5, v_m_cost = 0.916403607421, v_rm = 0.7
取出31前有这些容器： [23, 31]
取出31后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改hm过载  h_id = 22, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 37]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 22, v_p_cost = 0.75847628713, v_rp = 0.7, v_m_cost = 0.803789732079, v_rm = 1.0
取出3前有这些容器： [3, 4, 5, 13]
取出3后有： [4, 5, 13] v_p_cost=0.700969237448, v_rp = 0.7, v_m_cost = 0.802510135545, v_rm = 1.0
取出4前有这些容器： [4, 5, 13]
取出4后有： [5, 13] v_p_cost=0.600462545043, v_rp = 0.7, v_m_cost = 0.699912968618, v_rm = 1.0
修改vm超载的情况 v_id = 27, v_p_cost = 0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.3
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 39, v_p_cost = 0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.3
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 41, v_p_cost = 1.01097129709, v_rp = 0.7, v_m_cost = 0.893264608639, v_rm = 0.5
取出26前有这些容器： [24, 26, 48]
取出26后有： [24, 48] v_p_cost=0.800598949261, v_rp = 0.7, v_m_cost = 0.669691839998, v_rm = 0.5
取出48前有这些容器： [24, 48]
取出48后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.905885994095, v_rp = 0.7, v_m_cost = 0.629976511311, v_rm = 0.5
取出17前有这些容器： [0, 17]
取出17后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.795015799351, v_rp = 0.5, v_m_cost = 0.632168438932, v_rm = 1.0
取出33前有这些容器： [12, 33]
取出33后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 3, h_p_cost = 1.3, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 32]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 5, h_p_cost = 2.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [35, 37, 39]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7],mem尺寸[1.0, 0.7, 0.3]
37
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.3]
39
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
35
修改hm过载  h_id = 18, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.3]
16
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [21, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.3]
21
修改hm过载  h_id = 44, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
19
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.869319478235, v_rp = 0.7, v_m_cost = 0.87796164549, v_rm = 1.0
取出20前有这些容器： [14, 20]
取出20后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 1.0
修改vm超载的情况 v_id = 3, v_p_cost = 0.697141189146, v_rp = 0.3, v_m_cost = 0.600338465954, v_rm = 0.7
取出34前有这些容器： [18, 34]
取出34后有： [18] v_p_cost=0.368267087556, v_rp = 0.3, v_m_cost = 0.273384297823, v_rm = 0.7
取出18前有这些容器： [18]
取出18后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.378304805046, v_rp = 0.3, v_m_cost = 0.274694486214, v_rm = 1.0
取出7前有这些容器： [7]
取出7后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 9, v_p_cost = 0.597096572173, v_rp = 1.0, v_m_cost = 0.570749705861, v_rm = 0.5
取出44前有这些容器： [44, 47]
取出44后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.396941246853, v_rp = 0.3, v_m_cost = 0.176972489222, v_rm = 0.3
取出39前有这些容器： [39, 42]
取出39后有： [42] v_p_cost=0.204639347974, v_rp = 0.3, v_m_cost = 0.0258790261448, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.479873774184, v_rp = 0.5, v_m_cost = 0.594667395232, v_rm = 0.5
取出6前有这些容器： [6, 19]
取出6后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.725285735109, v_rp = 0.5, v_m_cost = 0.808737511215, v_rm = 0.7
取出9前有这些容器： [9, 17]
取出9后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 35, v_p_cost = 1.24181822892, v_rp = 1.0, v_m_cost = 1.23618262703, v_rm = 1.0
取出1前有这些容器： [1, 23, 31]
取出1后有： [23, 31] v_p_cost=0.858077169793, v_rp = 1.0, v_m_cost = 0.916403607421, v_rm = 1.0
修改vm超载的情况 v_id = 40, v_p_cost = 0.50391836755, v_rp = 0.3, v_m_cost = 0.324279437155, v_rm = 0.5
取出28前有这些容器： [28, 43]
取出28后有： [43] v_p_cost=0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 0.5
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 43, v_p_cost = 0.596495018598, v_rp = 1.0, v_m_cost = 0.722673638888, v_rm = 0.7
取出10前有这些容器： [10, 32, 46]
取出10后有： [32, 46] v_p_cost=0.518357580182, v_rp = 1.0, v_m_cost = 0.587711392653, v_rm = 0.7
修改hm过载  h_id = 6, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 4]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 37, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [37, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 38, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 30]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.7]
30
修改hm过载  h_id = 47, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
25
修改hm过载  h_id = 49, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
10
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.736639804852, v_rp = 0.3, v_m_cost = 0.698047355128, v_rm = 0.7
取出36前有这些容器： [22, 36, 48]
取出36后有： [22, 48] v_p_cost=0.670945589849, v_rp = 0.3, v_m_cost = 0.63994787858, v_rm = 0.7
取出22前有这些容器： [22, 48]
取出22后有： [48] v_p_cost=0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.7
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 1.0
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 20, v_p_cost = 0.829573734955, v_rp = 0.5, v_m_cost = 0.810127195094, v_rm = 0.7
取出13前有这些容器： [13, 34, 43]
取出13后有： [34, 43] v_p_cost=0.646095322611, v_rp = 0.5, v_m_cost = 0.61015162156, v_rm = 0.7
取出43前有这些容器： [34, 43]
取出43后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 1.30916847294, v_rp = 1.0, v_m_cost = 1.13131437406, v_rm = 0.5
取出1前有这些容器： [1, 17, 47]
取出1后有： [17, 47] v_p_cost=0.925427413815, v_rp = 1.0, v_m_cost = 0.811535354455, v_rm = 0.5
取出17前有这些容器： [17, 47]
取出17后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.716371058895, v_rp = 0.5, v_m_cost = 0.731315896159, v_rm = 0.7
取出11前有这些容器： [11, 31]
取出11后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 1.00485117059, v_rp = 0.7, v_m_cost = 0.840982645315, v_rm = 0.5
取出44前有这些容器： [16, 20, 44]
取出44后有： [16, 20] v_p_cost=0.888731028759, v_rp = 0.7, v_m_cost = 0.757361340338, v_rm = 0.5
取出20前有这些容器： [16, 20]
取出20后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 49, v_p_cost = 0.969200323936, v_rp = 1.0, v_m_cost = 0.837667445947, v_rm = 0.5
取出26前有这些容器： [0, 26, 33]
取出26后有： [0, 33] v_p_cost=0.758827976109, v_rp = 1.0, v_m_cost = 0.614094677307, v_rm = 0.5
取出33前有这些容器： [0, 33]
取出33后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.5
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
42
修改hm过载  h_id = 13, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 15, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 24, h_p_cost = 2.2, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [1, 33, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 1.0],mem尺寸[1.0, 0.7, 0.7]
33
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.7]
1
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
48
修改hm过载  h_id = 25, h_p_cost = 0.6, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 15]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 28, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
20
修改hm过载  h_id = 32, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [38, 44]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
44
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 31]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
31
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.02340459281, v_rp = 0.5, v_m_cost = 1.27818320473, v_rm = 0.5
取出9前有这些容器： [9, 23, 38]
取出9后有： [23, 38] v_p_cost=0.742569841172, v_rp = 0.5, v_m_cost = 0.79385264709, v_rm = 0.5
取出38前有这些容器： [23, 38]
取出38后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 1.09206625595, v_rp = 0.3, v_m_cost = 0.671513581783, v_rm = 0.7
取出28前有这些容器： [17, 24, 28]
取出28后有： [17, 24] v_p_cost=0.905369109425, v_rp = 0.3, v_m_cost = 0.630431598058, v_rm = 0.7
取出17前有这些容器： [17, 24]
取出17后有： [24] v_p_cost=0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 0.7
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.68878416356, v_rp = 0.5, v_m_cost = 0.749624311415, v_rm = 0.5
取出33前有这些容器： [20, 33]
取出33后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 0.5
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.893305333565, v_rp = 0.5, v_m_cost = 0.702657772997, v_rm = 0.3
取出19前有这些容器： [12, 19]
取出19后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.5, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.575880559119, v_rp = 0.3, v_m_cost = 0.68010097212, v_rm = 0.5
取出10前有这些容器： [4, 10, 31]
取出10后有： [4, 31] v_p_cost=0.497743120703, v_rp = 0.3, v_m_cost = 0.545138725886, v_rm = 0.5
取出4前有这些容器： [4, 31]
取出4后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 1.14791261222, v_rp = 0.7, v_m_cost = 1.19226111887, v_rm = 0.7
取出49前有这些容器： [1, 22, 37, 49]
取出49后有： [1, 22, 37] v_p_cost=1.02618022109, v_rp = 0.7, v_m_cost = 1.04662645866, v_rm = 0.7
取出37前有这些容器： [1, 22, 37]
取出37后有： [1, 22] v_p_cost=0.715005825674, v_rp = 0.7, v_m_cost = 0.596059702673, v_rm = 0.7
取出22前有这些容器： [1, 22]
取出22后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 49, v_p_cost = 0.48944263578, v_rp = 1.0, v_m_cost = 0.576969295838, v_rm = 0.5
取出15前有这些容器： [15, 48]
取出15后有： [48] v_p_cost=0.339680823305, v_rp = 1.0, v_m_cost = 0.363667195512, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
20
修改hm过载  h_id = 1, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 46]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 5, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [37, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 17, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 14]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
11
修改hm过载  h_id = 19, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 6]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 24, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 1.0]
0
修改hm过载  h_id = 29, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 31, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [28, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 35, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [29, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 36, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 42, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [9, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
10
进入mbbode_rank
[2, 12, 9, 7, 10] 0
上代结果： 14866.4024847 1.57037331834 783500.388562 1430.0
本代结果替代后： 14417.0799408 1.57029460402 783480.158484 1430.0
执行全局精英解替换： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 9, 4: 21, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 32: 47, 34: 23, 36: 49, 37: 22, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 6, v_p_cost = 0.736118763295, v_rp = 0.7, v_m_cost = 0.788711732285, v_rm = 0.7
取出11前有这些容器： [5, 11]
取出11后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.741843948953, v_rp = 0.7, v_m_cost = 0.632932073139, v_rm = 0.3
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.3
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.598129526271, v_rp = 0.5, v_m_cost = 0.426240486291, v_rm = 1.0
取出4前有这些容器： [4, 12]
取出4后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 3, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [32, 33]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
33
修改hm过载  h_id = 19, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
14
修改hm过载  h_id = 28, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 8]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
8
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 39, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 36]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
36
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.817609103464, v_rp = 0.7, v_m_cost = 0.800529649155, v_rm = 1.0
取出48前有这些容器： [14, 48]
取出48后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 1.0
修改vm超载的情况 v_id = 4, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 1.0
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 7, v_p_cost = 1.20272442141, v_rp = 1.0, v_m_cost = 1.00637361678, v_rm = 0.7
取出49前有这些容器： [16, 24, 32, 49]
取出49后有： [16, 24, 32] v_p_cost=1.08099203028, v_rp = 1.0, v_m_cost = 0.860738956564, v_rm = 0.7
取出32前有这些容器： [16, 24, 32]
取出32后有： [16, 24] v_p_cost=0.958257956639, v_rp = 1.0, v_m_cost = 0.622286792976, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.703746364856, v_rp = 0.3, v_m_cost = 0.471019720528, v_rm = 0.3
取出10前有这些容器： [10, 41, 42]
取出10后有： [41, 42] v_p_cost=0.625608926441, v_rp = 0.3, v_m_cost = 0.336057474293, v_rm = 0.3
取出42前有这些容器： [41, 42]
取出42后有： [41] v_p_cost=0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.3
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 28, v_p_cost = 0.691739783947, v_rp = 1.0, v_m_cost = 0.733916383128, v_rm = 0.5
取出27前有这些容器： [19, 27, 38]
取出27后有： [19, 38] v_p_cost=0.677411599375, v_rp = 1.0, v_m_cost = 0.699005052261, v_rm = 0.5
取出38前有这些容器： [19, 38]
取出38后有： [19] v_p_cost=0.395682499698, v_rp = 1.0, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 30, v_p_cost = 0.798796664712, v_rp = 0.7, v_m_cost = 0.801693224437, v_rm = 0.7
取出28前有这些容器： [9, 22, 28]
取出28后有： [9, 22] v_p_cost=0.612099518183, v_rp = 0.7, v_m_cost = 0.760611240712, v_rm = 0.7
取出9前有这些容器： [9, 22]
取出9后有： [22] v_p_cost=0.331264766544, v_rp = 0.7, v_m_cost = 0.276280683068, v_rm = 0.7
修改vm超载的情况 v_id = 35, v_p_cost = 1.2359729987, v_rp = 1.0, v_m_cost = 1.23474025991, v_rm = 1.0
取出1前有这些容器： [1, 20, 23]
取出1后有： [20, 23] v_p_cost=0.852231939571, v_rp = 1.0, v_m_cost = 0.914961240309, v_rm = 1.0
修改vm超载的情况 v_id = 40, v_p_cost = 0.50261304294, v_rp = 0.3, v_m_cost = 0.488749910734, v_rm = 0.5
取出13前有这些容器： [11, 13]
取出13后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 0.5
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 42, v_p_cost = 0.779240545418, v_rp = 0.5, v_m_cost = 0.692459251428, v_rm = 0.5
取出35前有这些容器： [18, 35, 43]
取出35后有： [18, 43] v_p_cost=0.685488308576, v_rp = 0.5, v_m_cost = 0.556581751253, v_rm = 0.5
取出43前有这些容器： [18, 43]
取出43后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.56815634918, v_rp = 0.7, v_m_cost = 0.508501115547, v_rm = 0.5
取出45前有这些容器： [45, 47]
取出45后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改hm过载  h_id = 6, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [23, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 1.0]
23
修改hm过载  h_id = 14, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 17, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
7
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 21]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 26, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 6]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 32, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 5]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 34, h_p_cost = 1.7, h_m_cost = 2.5
该物理机上放置的虚拟机为：  [1, 10, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5, 0.5],mem尺寸[1.0, 0.5, 1.0]
10
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 42, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 47, h_p_cost = 2.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [28, 41, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 0.5],mem尺寸[0.5, 0.5, 0.5]
42
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
41
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
28
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.517490825103, v_rp = 0.5, v_m_cost = 0.602534562011, v_rm = 0.7
取出4前有这些容器： [4, 5]
取出4后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.742569841172, v_rp = 0.5, v_m_cost = 0.79385264709, v_rm = 0.7
取出38前有这些容器： [23, 38]
取出38后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.604420508747, v_rp = 0.5, v_m_cost = 0.500879114589, v_rm = 0.5
取出30前有这些容器： [0, 30]
取出30后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.814844054888, v_rp = 0.7, v_m_cost = 0.606840772794, v_rm = 0.5
取出43前有这些容器： [12, 43]
取出43后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 38, v_p_cost = 1.26019250947, v_rp = 1.0, v_m_cost = 0.890897578849, v_rm = 0.7
取出7前有这些容器： [7, 24, 41]
取出7后有： [24, 41] v_p_cost=0.881887704423, v_rp = 1.0, v_m_cost = 0.616203092635, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.514418413955, v_rp = 0.7, v_m_cost = 0.496375766459, v_rm = 0.3
取出6前有这些容器： [6, 21]
取出6后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.3
修改vm超载的情况 v_id = 44, v_p_cost = 0.973074920648, v_rp = 0.7, v_m_cost = 0.913471349046, v_rm = 0.5
取出32前有这些容器： [8, 16, 32]
取出32后有： [8, 16] v_p_cost=0.850340847006, v_rp = 0.7, v_m_cost = 0.675019185458, v_rm = 0.5
取出8前有这些容器： [8, 16]
取出8后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.678071179939, v_rp = 1.0, v_m_cost = 0.926872116603, v_rm = 0.7
取出9前有这些容器： [9, 31]
取出9后有： [31] v_p_cost=0.397236428299, v_rp = 1.0, v_m_cost = 0.442541558959, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 4, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [0, 11]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
0
修改hm过载  h_id = 6, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
45
修改hm过载  h_id = 9, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 12, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [9, 16]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 1.0]
16
修改hm过载  h_id = 20, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 24, h_p_cost = 2.5, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [7, 13, 33, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3, 0.5, 0.7],mem尺寸[0.7, 0.3, 0.7, 0.7]
13
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7],mem尺寸[0.7, 0.7, 0.7]
33
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.7]
46
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
7
修改hm过载  h_id = 25, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
修改hm过载  h_id = 30, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [26, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 33, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [43, 48]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
43
修改hm过载  h_id = 43, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
20
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 46, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 28]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 13, v_p_cost = 0.597846523087, v_rp = 0.3, v_m_cost = 0.418859315416, v_rm = 0.3
取出4前有这些容器： [4, 16]
取出4后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 16, v_p_cost = 0.515475219453, v_rp = 0.5, v_m_cost = 0.403056691847, v_rm = 1.0
取出29前有这些容器： [29, 41]
取出29后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 1.0
修改vm超载的情况 v_id = 18, v_p_cost = 0.297392965484, v_rp = 0.7, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.558011212599, v_rp = 0.5, v_m_cost = 0.729629641467, v_rm = 0.7
取出10前有这些容器： [6, 10, 19]
取出10后有： [6, 19] v_p_cost=0.479873774184, v_rp = 0.5, v_m_cost = 0.594667395232, v_rm = 0.7
修改vm超载的情况 v_id = 29, v_p_cost = 0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 36, v_p_cost = 0.914855674647, v_rp = 0.7, v_m_cost = 0.991586134798, v_rm = 0.5
取出28前有这些容器： [5, 28, 37]
取出28后有： [5, 37] v_p_cost=0.728158528118, v_rp = 0.7, v_m_cost = 0.950504151073, v_rm = 0.5
取出37前有这些容器： [5, 37]
取出37后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 1.15904761028, v_rp = 0.3, v_m_cost = 1.41400051749, v_rm = 0.5
取出9前有这些容器： [9, 31, 47]
取出9后有： [31, 47] v_p_cost=0.878212858644, v_rp = 0.3, v_m_cost = 0.929669959843, v_rm = 0.5
取出31前有这些容器： [31, 47]
取出31后有： [47] v_p_cost=0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.5
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.642389333325, v_rp = 0.7, v_m_cost = 0.738243921707, v_rm = 0.5
取出2前有这些容器： [2, 26, 34]
取出2后有： [26, 34] v_p_cost=0.539246449417, v_rp = 0.7, v_m_cost = 0.550526936772, v_rm = 0.5
取出26前有这些容器： [26, 34]
取出26后有： [34] v_p_cost=0.32887410159, v_rp = 0.7, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 1.4751872716, v_rp = 0.7, v_m_cost = 1.11998859089, v_rm = 0.7
取出3前有这些容器： [3, 21, 23, 24, 36]
取出3后有： [21, 23, 24, 36] v_p_cost=1.41768022192, v_rp = 0.7, v_m_cost = 1.11870899436, v_rm = 0.7
取出36前有这些容器： [21, 23, 24, 36]
取出36后有： [21, 23, 24] v_p_cost=1.35198600692, v_rp = 0.7, v_m_cost = 1.06060951781, v_rm = 0.7
取出21前有这些容器： [21, 23, 24]
取出21后有： [23, 24] v_p_cost=0.92175886745, v_rp = 0.7, v_m_cost = 0.779886692948, v_rm = 0.7
取出23前有这些容器： [23, 24]
取出23后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 49, v_p_cost = 0.658815453901, v_rp = 1.0, v_m_cost = 0.652441532712, v_rm = 0.5
取出11前有这些容器： [11, 48]
取出11后有： [48] v_p_cost=0.339680823305, v_rp = 1.0, v_m_cost = 0.363667195512, v_rm = 0.5
修改hm过载  h_id = 6, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 16, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [9, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 17, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [31, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
31
修改hm过载  h_id = 26, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
26
修改hm过载  h_id = 32, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 40, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [43, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
43
修改hm过载  h_id = 41, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 44, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
30
修改hm过载  h_id = 47, h_p_cost = 1.7, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [24, 39]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.3]
39
修改hm过载  h_id = 48, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 29]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.3]
16
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
8
进入mbbode_rank
[2, 9, 7, 14, 8] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [34, 45], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.467531898168, v_rp = 0.7, v_m_cost = 0.525412541369, v_rm = 0.5
取出28前有这些容器： [9, 28]
取出28后有： [9] v_p_cost=0.280834751639, v_rp = 0.7, v_m_cost = 0.484330557644, v_rm = 0.5
修改hm过载  h_id = 21, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.382235792082, v_rp = 0.3, v_m_cost = 0.422587765555, v_rm = 0.7
取出4前有这些容器： [4, 38]
取出4后有： [38] v_p_cost=0.281729099678, v_rp = 0.3, v_m_cost = 0.319990598628, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.812360776544, v_rp = 0.5, v_m_cost = 0.751277639996, v_rm = 0.7
取出20前有这些容器： [20, 41]
取出20后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.741843948953, v_rp = 0.7, v_m_cost = 0.632932073139, v_rm = 0.5
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 32, v_p_cost = 0.897960563044, v_rp = 1.0, v_m_cost = 0.987065795968, v_rm = 0.7
取出5前有这些容器： [5, 47]
取出5后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.71445764932, v_rp = 0.7, v_m_cost = 0.725739012389, v_rm = 0.3
取出43前有这些容器： [31, 43]
取出43后有： [31] v_p_cost=0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 47, v_p_cost = 0.576960883322, v_rp = 0.5, v_m_cost = 0.557483353439, v_rm = 1.0
取出44前有这些容器： [23, 44]
取出44后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 2.5, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [33, 43, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 1.0],mem尺寸[0.7, 0.7, 0.5]
33
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
43
修改hm过载  h_id = 2, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [6, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
6
修改hm过载  h_id = 14, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 15, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [31, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
31
修改hm过载  h_id = 44, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 11, v_p_cost = 0.681293325793, v_rp = 0.7, v_m_cost = 0.564724502908, v_rm = 0.5
取出45前有这些容器： [1, 26, 45]
取出45后有： [1, 26] v_p_cost=0.594113406957, v_rp = 0.7, v_m_cost = 0.543351788245, v_rm = 0.5
取出26前有这些容器： [1, 26]
取出26后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.3
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 0.405680036404, v_rp = 0.7, v_m_cost = 0.543444999686, v_rm = 0.5
取出29前有这些容器： [29, 37]
取出29后有： [37] v_p_cost=0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 28, v_p_cost = 0.873610779856, v_rp = 1.0, v_m_cost = 0.815876907275, v_rm = 0.5
取出19前有这些容器： [14, 19]
取出19后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 1.07054959472, v_rp = 0.7, v_m_cost = 1.28514677424, v_rm = 0.5
取出9前有这些容器： [9, 23, 34]
取出9后有： [23, 34] v_p_cost=0.789714843084, v_rp = 0.7, v_m_cost = 0.800816216592, v_rm = 0.5
取出34前有这些容器： [23, 34]
取出34后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.480871377828, v_rp = 0.7, v_m_cost = 0.508500693101, v_rm = 0.5
取出13前有这些容器： [13, 33]
取出13后有： [33] v_p_cost=0.297392965484, v_rp = 0.7, v_m_cost = 0.308525119567, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.3
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 43, v_p_cost = 0.960201401073, v_rp = 1.0, v_m_cost = 0.842545771741, v_rm = 0.7
取出2前有这些容器： [0, 2, 46]
取出2后有： [0, 46] v_p_cost=0.857058517165, v_rp = 1.0, v_m_cost = 0.654828786805, v_rm = 0.7
修改vm超载的情况 v_id = 46, v_p_cost = 0.762457418812, v_rp = 0.7, v_m_cost = 0.499687549324, v_rm = 0.7
取出10前有这些容器： [10, 12, 28]
取出10后有： [12, 28] v_p_cost=0.684319980396, v_rp = 0.7, v_m_cost = 0.364725303089, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.511436529476, v_rp = 0.5, v_m_cost = 0.439867800278, v_rm = 1.0
取出39前有这些容器： [11, 39]
取出39后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 1.7, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [16, 23, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.5],mem尺寸[1.0, 0.5, 0.5]
16
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 3, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 10, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
7
修改hm过载  h_id = 12, h_p_cost = 0.6, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 4]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
12
修改hm过载  h_id = 17, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 22]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 1.0]
11
修改hm过载  h_id = 18, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [32, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
32
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 29, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [40, 49]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.5]
40
修改hm过载  h_id = 40, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 20]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
20
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
33
修改hm过载  h_id = 44, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [31, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
31
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.732143973886, v_rp = 0.3, v_m_cost = 0.760745204137, v_rm = 0.7
取出37前有这些容器： [37, 41]
取出37后有： [41] v_p_cost=0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.7
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.589433222114, v_rp = 0.3, v_m_cost = 0.566697984305, v_rm = 1.0
取出25前有这些容器： [5, 25]
取出25后有： [5] v_p_cost=0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 1.0
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 33, v_p_cost = 0.947802068994, v_rp = 0.5, v_m_cost = 0.813520649027, v_rm = 0.7
取出2前有这些容器： [1, 2, 24]
取出2后有： [1, 24] v_p_cost=0.844659185086, v_rp = 0.5, v_m_cost = 0.625803664091, v_rm = 0.7
取出1前有这些容器： [1, 24]
取出1后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 43, v_p_cost = 1.12696257849, v_rp = 1.0, v_m_cost = 1.13893221141, v_rm = 0.7
取出10前有这些容器： [10, 19, 23, 39]
取出10后有： [19, 23, 39] v_p_cost=1.04882514007, v_rp = 1.0, v_m_cost = 1.00396996517, v_rm = 0.7
取出39前有这些容器： [19, 23, 39]
取出39后有： [19, 23] v_p_cost=0.856523241192, v_rp = 1.0, v_m_cost = 0.852876502094, v_rm = 0.7
取出19前有这些容器： [19, 23]
取出19后有： [23] v_p_cost=0.460840741494, v_rp = 1.0, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 48, v_p_cost = 1.15904761028, v_rp = 1.0, v_m_cost = 1.41400051749, v_rm = 0.7
取出9前有这些容器： [9, 31, 47]
取出9后有： [31, 47] v_p_cost=0.878212858644, v_rp = 1.0, v_m_cost = 0.929669959843, v_rm = 0.7
取出31前有这些容器： [31, 47]
取出31后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 49, v_p_cost = 0.521495180137, v_rp = 1.0, v_m_cost = 0.505387977037, v_rm = 0.5
取出36前有这些容器： [36, 44, 48]
取出36后有： [44, 48] v_p_cost=0.455800965133, v_rp = 1.0, v_m_cost = 0.447288500489, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.7, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [39, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 0.5]
39
修改hm过载  h_id = 7, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [17, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.3]
21
修改hm过载  h_id = 14, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
37
修改hm过载  h_id = 22, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [25, 29, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[0.7, 0.3, 0.7]
25
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 34, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 14]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.7]
14
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 39, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 10]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 43, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [12, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
12
修改hm过载  h_id = 45, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 46, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 28]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.17238772371, v_rp = 0.5, v_m_cost = 1.06181423111, v_rm = 0.5
取出40前有这些容器： [20, 21, 34, 40]
取出40后有： [20, 21, 34] v_p_cost=1.15049243914, v_rp = 0.5, v_m_cost = 1.04877618484, v_rm = 0.5
取出34前有这些容器： [20, 21, 34]
取出34后有： [20, 21] v_p_cost=0.821618337545, v_rp = 0.5, v_m_cost = 0.721822016707, v_rm = 0.5
取出20前有这些容器： [20, 21]
取出20后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.620633709011, v_rp = 0.3, v_m_cost = 0.790251546947, v_rm = 0.7
取出4前有这些容器： [2, 4, 5]
取出4后有： [2, 5] v_p_cost=0.520127016607, v_rp = 0.3, v_m_cost = 0.68765438002, v_rm = 0.7
取出2前有这些容器： [2, 5]
取出2后有： [5] v_p_cost=0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.7
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 1.0
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 15, v_p_cost = 0.368267087556, v_rp = 0.3, v_m_cost = 0.273384297823, v_rm = 0.5
取出18前有这些容器： [18]
取出18后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.911098725993, v_rp = 0.5, v_m_cost = 0.752315920913, v_rm = 1.0
取出29前有这些容器： [29, 41, 46]
取出29后有： [41, 46] v_p_cost=0.816593085007, v_rp = 0.5, v_m_cost = 0.659437677215, v_rm = 1.0
取出46前有这些容器： [41, 46]
取出46后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 1.0
修改vm超载的情况 v_id = 18, v_p_cost = 0.427294537247, v_rp = 0.7, v_m_cost = 0.534188060965, v_rm = 0.3
取出44前有这些容器： [37, 44]
取出44后有： [37] v_p_cost=0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.3
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 25, v_p_cost = 0.677411599375, v_rp = 0.5, v_m_cost = 0.699005052261, v_rm = 0.7
取出38前有这些容器： [19, 38]
取出38后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.7
修改vm超载的情况 v_id = 32, v_p_cost = 0.792785770078, v_rp = 1.0, v_m_cost = 0.842885207875, v_rm = 0.7
取出27前有这些容器： [9, 12, 27]
取出27后有： [9, 12] v_p_cost=0.778457585506, v_rp = 1.0, v_m_cost = 0.807973877008, v_rm = 0.7
取出9前有这些容器： [9, 12]
取出9后有： [12] v_p_cost=0.497622833867, v_rp = 1.0, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.5
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.490988665141, v_rp = 0.7, v_m_cost = 0.578419059134, v_rm = 0.5
取出35前有这些容器： [31, 35]
取出35后有： [31] v_p_cost=0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.5
修改hm过载  h_id = 1, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [7, 39]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.3]
39
修改hm过载  h_id = 16, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 20, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [19, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 23, h_p_cost = 1.3, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 48]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 28, h_p_cost = 2.0, h_m_cost = 2.5
该物理机上放置的虚拟机为：  [4, 21, 23, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.7, 0.5],mem尺寸[1.0, 0.3, 0.5, 0.7]
4
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.5],mem尺寸[0.3, 0.5, 0.7]
21
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
33
修改hm过载  h_id = 31, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [28, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
28
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
6
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [29, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
29
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [42, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
42
修改hm过载  h_id = 41, h_p_cost = 1.4, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 30]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.7]
17
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 25]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 46, h_p_cost = 2.0, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [15, 16, 26, 36]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.5, 0.7],mem尺寸[0.5, 1.0, 0.7, 0.5]
15
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[1.0, 0.7, 0.5]
16
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [8, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 1.0]
8
进入mbbode_rank
[2, 8, 12, 10, 8] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [17, 33], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 9, 4: 21, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 17: 33, 19: 35, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 32: 47, 34: 23, 36: 49, 37: 22, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 21]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.3]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 1.05765542914, v_rp = 0.7, v_m_cost = 1.03678024171, v_rm = 1.0
取出13前有这些容器： [8, 13, 34, 39]
取出13后有： [8, 34, 39] v_p_cost=0.874177016793, v_rp = 0.7, v_m_cost = 0.836804668177, v_rm = 1.0
取出39前有这些容器： [8, 34, 39]
取出39后有： [8, 34] v_p_cost=0.681875117913, v_rp = 0.7, v_m_cost = 0.685711205099, v_rm = 1.0
修改vm超载的情况 v_id = 12, v_p_cost = 0.570731390942, v_rp = 0.5, v_m_cost = 0.523480548474, v_rm = 0.7
取出15前有这些容器： [15, 41]
取出15后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [42, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 7, h_p_cost = 2.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 28]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
7
修改hm过载  h_id = 12, h_p_cost = 0.8, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 30, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 33, h_p_cost = 1.5, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [2, 29]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.3]
29
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 1.15745663092, v_rp = 0.3, v_m_cost = 1.00014932381, v_rm = 1.0
取出28前有这些容器： [9, 12, 28, 39]
取出28后有： [9, 12, 39] v_p_cost=0.970759484386, v_rp = 0.3, v_m_cost = 0.959067340086, v_rm = 1.0
取出39前有这些容器： [9, 12, 39]
取出39后有： [9, 12] v_p_cost=0.778457585506, v_rp = 0.3, v_m_cost = 0.807973877008, v_rm = 1.0
取出9前有这些容器： [9, 12]
取出9后有： [12] v_p_cost=0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 1.0
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=1.11022302463e-16, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 20, v_p_cost = 1.27612593152, v_rp = 0.5, v_m_cost = 1.20718830796, v_rm = 0.7
取出43前有这些容器： [14, 43, 47]
取出43后有： [14, 47] v_p_cost=0.958904710504, v_rp = 0.5, v_m_cost = 0.923990854526, v_rm = 0.7
取出14前有这些容器： [14, 47]
取出14后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 22, v_p_cost = 0.891145265424, v_rp = 0.7, v_m_cost = 0.586747469346, v_rm = 1.0
取出21前有这些容器： [21, 24]
取出21后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 1.0
修改vm超载的情况 v_id = 23, v_p_cost = 0.830409510673, v_rp = 0.7, v_m_cost = 0.779866950746, v_rm = 0.5
取出40前有这些容器： [16, 37, 40]
取出40后有： [16, 37] v_p_cost=0.808514226101, v_rp = 0.7, v_m_cost = 0.766828904478, v_rm = 0.5
取出37前有这些容器： [16, 37]
取出37后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 30, v_p_cost = 0.72265596462, v_rp = 0.7, v_m_cost = 0.717379874916, v_rm = 0.7
取出22前有这些容器： [20, 22]
取出22后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.976661756382, v_rp = 0.5, v_m_cost = 1.03417432573, v_rm = 1.0
取出15前有这些容器： [11, 15, 26, 33]
取出15后有： [11, 26, 33] v_p_cost=0.826899943907, v_rp = 0.5, v_m_cost = 0.820872225409, v_rm = 1.0
取出26前有这些容器： [11, 26, 33]
取出26后有： [11, 33] v_p_cost=0.61652759608, v_rp = 0.5, v_m_cost = 0.597299456768, v_rm = 1.0
取出33前有这些容器： [11, 33]
取出33后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 1.0
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [27, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.3]
29
修改hm过载  h_id = 2, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [3, 15, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.7],mem尺寸[0.7, 0.5, 0.3]
3
修改hm过载  h_id = 3, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 4, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 5, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [47, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 0.7]
47
修改hm过载  h_id = 6, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
修改hm过载  h_id = 8, h_p_cost = 2.4, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [14, 19, 22]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.7],mem尺寸[0.7, 1.0, 1.0]
14
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 1.0]
22
修改hm过载  h_id = 18, h_p_cost = 2.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [13, 23, 43]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 1.0],mem尺寸[0.3, 0.5, 0.7]
13
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 25, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 35, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [31, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
31
修改hm过载  h_id = 43, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[0.5, 0.5]
40
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 1]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 1.0]
0
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.688639265297, v_rp = 0.5, v_m_cost = 0.725806963282, v_rm = 0.5
取出6前有这些容器： [6, 13, 41]
取出6后有： [13, 41] v_p_cost=0.604447990811, v_rp = 0.5, v_m_cost = 0.510154021682, v_rm = 0.5
取出13前有这些容器： [13, 41]
取出13后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.409951691111, v_rp = 0.3, v_m_cost = 0.384170559932, v_rm = 0.7
取出27前有这些容器： [27, 46]
取出27后有： [46] v_p_cost=0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.7
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.850340847006, v_rp = 0.7, v_m_cost = 0.675019185458, v_rm = 0.7
取出8前有这些容器： [8, 16]
取出8后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.3
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.522588421885, v_rp = 0.7, v_m_cost = 0.459369199806, v_rm = 0.3
取出10前有这些容器： [10, 17]
取出10后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 1.58155869072, v_rp = 0.7, v_m_cost = 1.45292840061, v_rm = 0.3
取出48前有这些容器： [14, 18, 19, 48]
取出48后有： [14, 18, 19] v_p_cost=1.24187786741, v_rp = 0.7, v_m_cost = 1.0892612051, v_rm = 0.3
取出18前有这些容器： [14, 18, 19]
取出18后有： [14, 19] v_p_cost=0.873610779856, v_rp = 0.7, v_m_cost = 0.815876907275, v_rm = 0.3
取出19前有这些容器： [14, 19]
取出19后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.3
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = 1.11022302463e-16, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 1.0559935538, v_rp = 0.5, v_m_cost = 0.835616902012, v_rm = 0.7
取出35前有这些容器： [24, 25, 34, 35]
取出35后有： [24, 25, 34] v_p_cost=0.962241316961, v_rp = 0.5, v_m_cost = 0.699739401837, v_rm = 0.7
取出25前有这些容器： [24, 25, 34]
取出25后有： [24, 34] v_p_cost=0.789792227546, v_rp = 0.5, v_m_cost = 0.632978812617, v_rm = 0.7
取出34前有这些容器： [24, 34]
取出34后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 36, v_p_cost = 1.06262478544, v_rp = 0.7, v_m_cost = 0.639419789303, v_rm = 0.5
取出28前有这些容器： [7, 12, 28]
取出28后有： [7, 12] v_p_cost=0.875927638913, v_rp = 0.7, v_m_cost = 0.598337805578, v_rm = 0.5
取出7前有这些容器： [7, 12]
取出7后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改hm过载  h_id = 1, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [31, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
31
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 11, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 17, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 20, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 48]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 30, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 32]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
2
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [16, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [39, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 1.0]
45
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [44, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.5]
44
修改hm过载  h_id = 44, h_p_cost = 0.6, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 40]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 45, h_p_cost = 1.3, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [13, 24]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.3, 0.5]
13
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 13, v_p_cost = 0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 14, v_p_cost = 0.878212858644, v_rp = 0.7, v_m_cost = 0.929669959843, v_rm = 0.7
取出31前有这些容器： [31, 47]
取出31后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.5
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 23, v_p_cost = 0.650393981807, v_rp = 0.7, v_m_cost = 0.667282156536, v_rm = 0.5
取出33前有这些容器： [8, 33]
取出33后有： [8] v_p_cost=0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 1.08000248009, v_rp = 1.0, v_m_cost = 0.743739756722, v_rm = 0.5
取出28前有这些容器： [12, 19, 28]
取出28后有： [12, 19] v_p_cost=0.893305333565, v_rp = 1.0, v_m_cost = 0.702657772997, v_rm = 0.5
取出19前有这些容器： [12, 19]
取出19后有： [12] v_p_cost=0.497622833867, v_rp = 1.0, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.52117600047, v_rp = 0.5, v_m_cost = 0.478047631208, v_rm = 0.3
取出39前有这些容器： [34, 39]
取出39后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.3
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 31, v_p_cost = 0.811236078101, v_rp = 0.5, v_m_cost = 0.832337704469, v_rm = 0.5
取出26前有这些容器： [11, 26, 38]
取出26后有： [11, 38] v_p_cost=0.600863730274, v_rp = 0.5, v_m_cost = 0.608764935828, v_rm = 0.5
取出38前有这些容器： [11, 38]
取出38后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.548430241069, v_rp = 0.7, v_m_cost = 0.544999571278, v_rm = 0.5
取出40前有这些容器： [23, 36, 40]
取出40后有： [23, 36] v_p_cost=0.526534956497, v_rp = 0.7, v_m_cost = 0.53196152501, v_rm = 0.5
取出36前有这些容器： [23, 36]
取出36后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.511668015255, v_rp = 0.7, v_m_cost = 0.351173479356, v_rm = 0.3
取出27前有这些容器： [16, 27]
取出27后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 43, v_p_cost = 0.800793403036, v_rp = 1.0, v_m_cost = 0.85234212115, v_rm = 0.7
取出10前有这些容器： [10, 20, 22]
取出10后有： [20, 22] v_p_cost=0.72265596462, v_rp = 1.0, v_m_cost = 0.717379874916, v_rm = 0.7
取出22前有这些容器： [20, 22]
取出22后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 2.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [24, 47, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0],mem尺寸[0.5, 1.0, 0.5]
47
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.5]
24
修改hm过载  h_id = 5, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 12]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 9, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
6
修改hm过载  h_id = 10, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 12, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 28, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 36]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
23
修改hm过载  h_id = 32, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 34, h_p_cost = 2.2, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [10, 17, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 1.0],mem尺寸[0.5, 0.7, 0.7]
10
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
17
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
43
修改hm过载  h_id = 37, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.5]
34
修改hm过载  h_id = 46, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 29, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[0.7, 0.3, 0.7]
5
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 1.0]
0
进入mbbode_rank
[3, 9, 11, 7, 10] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [14, 45], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [25, 0], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 1, v_p_cost = 0.804609191556, v_rp = 0.7, v_m_cost = 0.924163368686, v_rm = 1.0
取出32前有这些容器： [8, 32, 34]
取出32后有： [8, 34] v_p_cost=0.681875117913, v_rp = 0.7, v_m_cost = 0.685711205099, v_rm = 1.0
修改vm超载的情况 v_id = 3, v_p_cost = 0.742569841172, v_rp = 0.3, v_m_cost = 0.79385264709, v_rm = 0.7
取出38前有这些容器： [23, 38]
取出38后有： [23] v_p_cost=0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.7
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 5, v_p_cost = 0.557327925005, v_rp = 0.5, v_m_cost = 0.851076962321, v_rm = 0.7
取出6前有这些容器： [6, 9, 39]
取出6后有： [9, 39] v_p_cost=0.473136650519, v_rp = 0.5, v_m_cost = 0.635424020722, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.640563825424, v_rp = 0.3, v_m_cost = 0.699174241929, v_rm = 0.5
取出36前有这些容器： [13, 20, 36]
取出36后有： [13, 20] v_p_cost=0.574869610421, v_rp = 0.3, v_m_cost = 0.641074765381, v_rm = 0.5
取出13前有这些容器： [13, 20]
取出13后有： [20] v_p_cost=0.391391198077, v_rp = 0.3, v_m_cost = 0.441099191848, v_rm = 0.5
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 24, v_p_cost = 0.861669339289, v_rp = 1.0, v_m_cost = 0.756641473247, v_rm = 0.5
取出1前有这些容器： [1, 14]
取出1后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.461908189539, v_rp = 0.5, v_m_cost = 0.305849764627, v_rm = 0.3
取出3前有这些容器： [3, 43, 45]
取出3后有： [43, 45] v_p_cost=0.404401139856, v_rp = 0.5, v_m_cost = 0.304570168092, v_rm = 0.3
取出45前有这些容器： [43, 45]
取出45后有： [43] v_p_cost=0.317221221021, v_rp = 0.5, v_m_cost = 0.28319745343, v_rm = 0.3
修改hm过载  h_id = 1, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 8]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 5, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 12, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 38, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 39, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
30
修改hm过载  h_id = 43, h_p_cost = 0.6, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 40]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 46, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 29]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.3]
16
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.498825383605, v_rp = 0.3, v_m_cost = 0.566731438569, v_rm = 0.7
取出2前有这些容器： [2, 19]
取出2后有： [19] v_p_cost=0.395682499698, v_rp = 0.3, v_m_cost = 0.379014453633, v_rm = 0.7
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 5, v_p_cost = 0.621409922983, v_rp = 0.5, v_m_cost = 0.68365779414, v_rm = 0.7
取出38前有这些容器： [38, 48]
取出38后有： [48] v_p_cost=0.339680823305, v_rp = 0.5, v_m_cost = 0.363667195512, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.744908767834, v_rp = 0.7, v_m_cost = 0.563438231558, v_rm = 0.7
取出3前有这些容器： [3, 11, 18]
取出3后有： [11, 18] v_p_cost=0.687401718152, v_rp = 0.7, v_m_cost = 0.562158635023, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.755625378888, v_rp = 0.5, v_m_cost = 0.774973709559, v_rm = 0.5
取出37前有这些容器： [17, 37]
取出37后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.507571017062, v_rp = 0.3, v_m_cost = 0.635485353429, v_rm = 0.3
取出6前有这些容器： [6, 29, 34]
取出6后有： [29, 34] v_p_cost=0.423379742576, v_rp = 0.3, v_m_cost = 0.419832411829, v_rm = 0.3
取出29前有这些容器： [29, 34]
取出29后有： [34] v_p_cost=0.32887410159, v_rp = 0.3, v_m_cost = 0.326954168131, v_rm = 0.3
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.403568825282, v_rp = 0.3, v_m_cost = 0.722782721232, v_rm = 0.5
取出32前有这些容器： [9, 32]
取出32后有： [9] v_p_cost=0.280834751639, v_rp = 0.3, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.545302915203, v_rp = 0.5, v_m_cost = 0.509850500046, v_rm = 0.3
取出39前有这些容器： [8, 39]
取出39后有： [8] v_p_cost=0.353001016323, v_rp = 0.5, v_m_cost = 0.358757036968, v_rm = 0.3
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 1.34964915472, v_rp = 0.7, v_m_cost = 1.06338598482, v_rm = 1.0
取出20前有这些容器： [16, 20, 24]
取出20后有： [16, 24] v_p_cost=0.958257956639, v_rp = 0.7, v_m_cost = 0.622286792976, v_rm = 1.0
取出24前有这些容器： [16, 24]
取出24后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 1.0
修改vm超载的情况 v_id = 34, v_p_cost = 0.504164051535, v_rp = 0.7, v_m_cost = 0.521310109747, v_rm = 0.5
取出45前有这些容器： [5, 45]
取出45后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.527593568848, v_rp = 0.7, v_m_cost = 0.50677022207, v_rm = 0.3
取出26前有这些容器： [26, 43]
取出26后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.537089720296, v_rp = 0.5, v_m_cost = 0.393799753126, v_rm = 1.0
取出44前有这些容器： [41, 44]
取出44后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 1.0
修改hm过载  h_id = 11, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 28, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 29, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 30, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [5, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
5
修改hm过载  h_id = 33, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 4]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 1.0]
4
修改hm过载  h_id = 35, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 36, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 42, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
10
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.515475219453, v_rp = 0.5, v_m_cost = 0.403056691847, v_rm = 0.5
取出29前有这些容器： [29, 41]
取出29后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.7
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 0.649627789831, v_rp = 0.7, v_m_cost = 0.541723019232, v_rm = 0.5
取出36前有这些容器： [28, 31, 36]
取出36后有： [28, 31] v_p_cost=0.583933574828, v_rp = 0.7, v_m_cost = 0.483623542684, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.427294537247, v_rp = 0.3, v_m_cost = 0.534188060965, v_rm = 0.3
取出44前有这些容器： [37, 44]
取出44后有： [37] v_p_cost=0.311174395419, v_rp = 0.3, v_m_cost = 0.450566755988, v_rm = 0.3
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 0.5
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.3
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 22, v_p_cost = 0.980037645827, v_rp = 0.7, v_m_cost = 1.00990591619, v_rm = 1.0
取出45前有这些容器： [2, 23, 34, 45]
取出45后有： [2, 23, 34] v_p_cost=0.892857726992, v_rp = 0.7, v_m_cost = 0.988533201528, v_rm = 1.0
取出2前有这些容器： [2, 23, 34]
取出2后有： [23, 34] v_p_cost=0.789714843084, v_rp = 0.7, v_m_cost = 0.800816216592, v_rm = 1.0
取出34前有这些容器： [23, 34]
取出34后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 1.0
修改vm超载的情况 v_id = 31, v_p_cost = 0.785251220255, v_rp = 0.5, v_m_cost = 0.773321692908, v_rm = 0.5
取出18前有这些容器： [5, 18]
取出18后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 34, v_p_cost = 0.612099518183, v_rp = 0.7, v_m_cost = 0.760611240712, v_rm = 0.5
取出9前有这些容器： [9, 22]
取出9后有： [22] v_p_cost=0.331264766544, v_rp = 0.7, v_m_cost = 0.276280683068, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.562119554645, v_rp = 0.7, v_m_cost = 0.652515395242, v_rm = 0.3
取出6前有这些容器： [6, 14]
取出6后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.3
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 42, v_p_cost = 0.893246340407, v_rp = 0.5, v_m_cost = 0.67290254843, v_rm = 0.5
取出46前有这些容器： [12, 46]
取出46后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.775132257207, v_rp = 0.7, v_m_cost = 0.760878211452, v_rm = 0.5
取出1前有这些容器： [1, 20]
取出1后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.9, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [0, 17, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.7],mem尺寸[0.5, 0.7, 0.5]
0
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
17
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [30, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 5, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 10, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [32, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.5]
42
修改hm过载  h_id = 12, h_p_cost = 1.5, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [9, 21]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.3]
21
修改hm过载  h_id = 17, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [16, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 25, h_p_cost = 2.0, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [4, 7, 23]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0, 0.7],mem尺寸[1.0, 0.7, 0.5]
4
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.5]
23
修改hm过载  h_id = 40, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 24]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 45, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
14
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
35
修改hm过载  h_id = 46, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 47, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 48, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 33]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 49, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
5
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.882211814269, v_rp = 0.5, v_m_cost = 0.823969732054, v_rm = 0.5
取出2前有这些容器： [2, 16, 38]
取出2后有： [16, 38] v_p_cost=0.779068930361, v_rp = 0.5, v_m_cost = 0.636252747118, v_rm = 0.5
取出38前有这些容器： [16, 38]
取出38后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.454743477982, v_rp = 0.3, v_m_cost = 0.443821155494, v_rm = 0.7
取出3前有这些容器： [3, 31]
取出3后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.81063520234, v_rp = 0.5, v_m_cost = 0.598711023851, v_rm = 0.7
取出42前有这些容器： [26, 42, 46]
取出42后有： [26, 46] v_p_cost=0.605995854367, v_rp = 0.5, v_m_cost = 0.572831997707, v_rm = 0.7
取出26前有这些容器： [26, 46]
取出26后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 0.978599264212, v_rp = 0.7, v_m_cost = 0.810771720248, v_rm = 0.5
取出47前有这些容器： [12, 47]
取出47后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 20, v_p_cost = 0.741843948953, v_rp = 0.5, v_m_cost = 0.632932073139, v_rm = 0.7
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.721268103879, v_rp = 0.7, v_m_cost = 0.632141334791, v_rm = 0.5
取出8前有这些容器： [8, 18]
取出8后有： [18] v_p_cost=0.368267087556, v_rp = 0.7, v_m_cost = 0.273384297823, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.508364577884, v_rp = 0.7, v_m_cost = 0.415685071094, v_rm = 0.3
取出10前有这些容器： [10, 21]
取出10后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.3
修改vm超载的情况 v_id = 42, v_p_cost = 0.587984398577, v_rp = 0.5, v_m_cost = 0.53010791671, v_rm = 0.5
取出39前有这些容器： [19, 39]
取出39后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改hm过载  h_id = 10, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [37, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
37
修改hm过载  h_id = 13, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 19, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [6, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
6
修改hm过载  h_id = 25, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
10
修改hm过载  h_id = 28, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 48]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.7]
22
修改hm过载  h_id = 40, h_p_cost = 3.0, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [2, 26, 28, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0, 0.5],mem尺寸[1.0, 0.7, 0.5, 0.5]
26
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 0.5],mem尺寸[1.0, 0.5, 0.5]
42
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.5]
2
修改hm过载  h_id = 41, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 43, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [30, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
30
修改hm过载  h_id = 45, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [17, 38]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
17
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [0, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.3]
0
进入mbbode_rank
[3, 9, 7, 6, 15] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 9, 4: 21, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 32: 47, 34: 23, 36: 49, 37: 22, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 4]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 13, v_p_cost = 0.297392965484, v_rp = 0.3, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 18, v_p_cost = 0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.3
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 0.869319478235, v_rp = 0.5, v_m_cost = 0.87796164549, v_rm = 0.7
取出20前有这些容器： [14, 20]
取出20后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.5
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 1.07055246827, v_rp = 0.7, v_m_cost = 0.792294530199, v_rm = 0.5
取出30前有这些容器： [16, 21, 30]
取出30后有： [16, 21] v_p_cost=0.927566970151, v_rp = 0.7, v_m_cost = 0.59698497335, v_rm = 0.5
取出21前有这些容器： [16, 21]
取出21后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.592128474853, v_rp = 0.5, v_m_cost = 0.416521563062, v_rm = 1.0
取出29前有这些容器： [12, 29]
取出29后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 1, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [8, 19]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
8
修改hm过载  h_id = 2, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 3]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 0.7]
3
修改hm过载  h_id = 15, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [18, 21]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.3]
21
修改hm过载  h_id = 16, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [15, 23, 46]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 0.7],mem尺寸[0.5, 0.5, 0.7]
15
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.7]
23
修改hm过载  h_id = 23, h_p_cost = 1.7, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [27, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.3, 1.0]
27
修改hm过载  h_id = 45, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 34]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
12
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.02813759743, v_rp = 0.5, v_m_cost = 0.825779237625, v_rm = 0.5
取出13前有这些容器： [1, 13, 24]
取出13后有： [1, 24] v_p_cost=0.844659185086, v_rp = 0.5, v_m_cost = 0.625803664091, v_rm = 0.5
取出1前有这些容器： [1, 24]
取出1后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.996410514068, v_rp = 0.5, v_m_cost = 0.750764438643, v_rm = 0.7
取出49前有这些容器： [17, 21, 49]
取出49后有： [17, 21] v_p_cost=0.874678122938, v_rp = 0.5, v_m_cost = 0.605129778431, v_rm = 0.7
取出21前有这些容器： [17, 21]
取出21后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 17, v_p_cost = 1.39306955214, v_rp = 0.7, v_m_cost = 1.39294564319, v_rm = 0.7
取出26前有这些容器： [19, 20, 26, 46]
取出26后有： [19, 20, 46] v_p_cost=1.18269720431, v_rp = 0.7, v_m_cost = 1.16937287455, v_rm = 0.7
取出20前有这些容器： [19, 20, 46]
取出20后有： [19, 46] v_p_cost=0.791306006237, v_rp = 0.7, v_m_cost = 0.728273682699, v_rm = 0.7
取出46前有这些容器： [19, 46]
取出46后有： [19] v_p_cost=0.395682499698, v_rp = 0.7, v_m_cost = 0.379014453633, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.281729099678, v_rp = 0.7, v_m_cost = 0.319990598628, v_rm = 0.3
取出38前有这些容器： [38]
取出38后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 0.503476294298, v_rp = 0.5, v_m_cost = 0.601660219066, v_rm = 0.7
取出39前有这些容器： [37, 39]
取出39后有： [37] v_p_cost=0.311174395419, v_rp = 0.5, v_m_cost = 0.450566755988, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.280834751639, v_rp = 0.5, v_m_cost = 0.484330557644, v_rm = 0.3
取出9前有这些容器： [9]
取出9后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.32887410159, v_rp = 0.7, v_m_cost = 0.326954168131, v_rm = 0.3
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 36, v_p_cost = 0.73420535372, v_rp = 0.7, v_m_cost = 0.783134848514, v_rm = 0.5
取出43前有这些容器： [5, 43]
取出43后有： [5] v_p_cost=0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 38, v_p_cost = 0.923807025509, v_rp = 1.0, v_m_cost = 0.955698108445, v_rm = 0.7
取出36前有这些容器： [10, 11, 23, 36]
取出36后有： [10, 11, 23] v_p_cost=0.858112810506, v_rp = 1.0, v_m_cost = 0.897598631897, v_rm = 0.7
取出10前有这些容器： [10, 11, 23]
取出10后有： [11, 23] v_p_cost=0.77997537209, v_rp = 1.0, v_m_cost = 0.762636385662, v_rm = 0.7
取出11前有这些容器： [11, 23]
取出11后有： [23] v_p_cost=0.460840741494, v_rp = 1.0, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 42, v_p_cost = 0.423872097791, v_rp = 0.5, v_m_cost = 0.579320137112, v_rm = 0.5
取出6前有这些容器： [6, 48]
取出6后有： [48] v_p_cost=0.339680823305, v_rp = 0.5, v_m_cost = 0.363667195512, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.627690092633, v_rp = 0.7, v_m_cost = 0.650164553968, v_rm = 0.5
取出15前有这些容器： [14, 15]
取出15后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 2.0, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [19, 33, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.5],mem尺寸[1.0, 0.7, 0.7]
33
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
37
修改hm过载  h_id = 7, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 16, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [6, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.3]
29
修改hm过载  h_id = 22, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 23, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [8, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
8
修改hm过载  h_id = 29, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 31]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 35, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [41, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 0.6
该物理机上放置的虚拟机为：  [21, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.3]
21
修改hm过载  h_id = 48, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 11]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.684673989077, v_rp = 0.3, v_m_cost = 0.719632075025, v_rm = 0.7
取出6前有这些容器： [2, 6, 16]
取出6后有： [2, 16] v_p_cost=0.600482714591, v_rp = 0.3, v_m_cost = 0.503979133426, v_rm = 0.7
取出2前有这些容器： [2, 16]
取出2后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.7
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.676458258179, v_rp = 0.7, v_m_cost = 0.83358978671, v_rm = 0.7
取出9前有这些容器： [9, 46]
取出9后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.701370422678, v_rp = 1.0, v_m_cost = 0.711362102755, v_rm = 0.5
取出4前有这些容器： [4, 11, 38]
取出4后有： [11, 38] v_p_cost=0.600863730274, v_rp = 1.0, v_m_cost = 0.608764935828, v_rm = 0.5
取出38前有这些容器： [11, 38]
取出38后有： [11] v_p_cost=0.319134630596, v_rp = 1.0, v_m_cost = 0.2887743372, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.517414890827, v_rp = 0.5, v_m_cost = 0.524649113845, v_rm = 0.7
取出49前有这些容器： [19, 49]
取出49后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.7
修改vm超载的情况 v_id = 26, v_p_cost = 0.707178906636, v_rp = 0.5, v_m_cost = 0.601648654344, v_rm = 0.7
取出34前有这些容器： [7, 34]
取出34后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 0.5
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.928480918372, v_rp = 0.7, v_m_cost = 0.834898944973, v_rm = 0.5
取出44前有这些容器： [20, 41, 44]
取出44后有： [20, 41] v_p_cost=0.812360776544, v_rp = 0.7, v_m_cost = 0.751277639996, v_rm = 0.5
取出20前有这些容器： [20, 41]
取出20后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 5, h_p_cost = 2.5, h_m_cost = 1.8
该物理机上放置的虚拟机为：  [28, 29, 34, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7, 0.3],mem尺寸[0.5, 0.3, 0.5, 0.5]
40
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7],mem尺寸[0.5, 0.3, 0.5]
29
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
34
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
28
修改hm过载  h_id = 7, h_p_cost = 1.3, h_m_cost = 2.1
该物理机上放置的虚拟机为：  [3, 12, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.5],mem尺寸[0.7, 0.7, 0.7]
3
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 8, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 30, h_p_cost = 1.9, h_m_cost = 2.4
该物理机上放置的虚拟机为：  [1, 6, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7, 0.5],mem尺寸[1.0, 0.7, 0.7]
37
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 33, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 38]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 39, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 9]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 45, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 1.0]
20
修改hm过载  h_id = 48, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 33]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
33
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.3]
16
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 1.0
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 6, v_p_cost = 0.738824794824, v_rp = 0.7, v_m_cost = 0.766715865693, v_rm = 0.7
取出29前有这些容器： [13, 23, 29]
取出29后有： [13, 23] v_p_cost=0.644319153838, v_rp = 0.7, v_m_cost = 0.673837621995, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 1.09350138404, v_rp = 1.0, v_m_cost = 1.36328240636, v_rm = 0.7
取出9前有这些容器： [5, 9, 19]
取出9后有： [5, 19] v_p_cost=0.812666632397, v_rp = 1.0, v_m_cost = 0.878951848717, v_rm = 0.7
取出19前有这些容器： [5, 19]
取出19后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 18, v_p_cost = 0.84937761573, v_rp = 0.7, v_m_cost = 0.910851209734, v_rm = 0.3
取出35前有这些容器： [17, 35, 37]
取出35后有： [17, 37] v_p_cost=0.755625378888, v_rp = 0.7, v_m_cost = 0.774973709559, v_rm = 0.3
取出37前有这些容器： [17, 37]
取出37后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.354900015166, v_rp = 0.5, v_m_cost = 0.309804716102, v_rm = 0.3
取出3前有这些容器： [3, 33]
取出3后有： [33] v_p_cost=0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.721268103879, v_rp = 0.5, v_m_cost = 0.632141334791, v_rm = 0.7
取出8前有这些容器： [8, 18]
取出8后有： [18] v_p_cost=0.368267087556, v_rp = 0.5, v_m_cost = 0.273384297823, v_rm = 0.7
修改vm超载的情况 v_id = 37, v_p_cost = 0.603005337445, v_rp = 0.5, v_m_cost = 0.533178585721, v_rm = 0.7
取出27前有这些容器： [7, 26, 27]
取出27后有： [7, 26] v_p_cost=0.588677152873, v_rp = 0.5, v_m_cost = 0.498267254854, v_rm = 0.7
取出26前有这些容器： [7, 26]
取出26后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.7
修改hm过载  h_id = 9, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 43]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
7
修改hm过载  h_id = 12, h_p_cost = 1.4, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 41]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 13, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 31]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 19, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 42]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 30, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [24, 34]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
34
修改hm过载  h_id = 32, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 14]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 1.0]
11
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
33
修改hm过载  h_id = 43, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [10, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
10
修改hm过载  h_id = 46, h_p_cost = 2.2, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [17, 28, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.5],mem尺寸[0.7, 0.5, 0.7]
37
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
17
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
28
进入mbbode_rank
[3, 11, 5, 10, 11] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [7, 5], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 1.23918377964, v_rp = 1.0, v_m_cost = 0.949194221629, v_rm = 0.7
取出33前有这些容器： [16, 17, 33]
取出33后有： [16, 17] v_p_cost=0.941790814152, v_rp = 1.0, v_m_cost = 0.640669102061, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 4]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 1.0]
4
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [17, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.3]
29
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.661406692503, v_rp = 0.5, v_m_cost = 0.636838027176, v_rm = 0.7
取出13前有这些容器： [13, 14]
取出13后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.799274383513, v_rp = 0.5, v_m_cost = 0.584872934362, v_rm = 0.7
取出7前有这些容器： [7, 41]
取出7后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.647615272485, v_rp = 0.5, v_m_cost = 0.347106628211, v_rm = 0.7
取出28前有这些容器： [24, 28]
取出28后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.600367893363, v_rp = 0.5, v_m_cost = 0.505997491508, v_rm = 0.3
取出4前有这些容器： [1, 4, 44]
取出4后有： [1, 44] v_p_cost=0.499861200959, v_rp = 0.5, v_m_cost = 0.403400324582, v_rm = 0.3
取出44前有这些容器： [1, 44]
取出44后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.3
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 26, v_p_cost = 0.601875776273, v_rp = 0.5, v_m_cost = 0.468420585104, v_rm = 0.7
取出42前有这些容器： [31, 42]
取出42后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.608567360902, v_rp = 0.7, v_m_cost = 0.759091875556, v_rm = 0.5
取出33前有这些容器： [33, 37]
取出33后有： [37] v_p_cost=0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 40, v_p_cost = 0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 0.5
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 1.0609037072, v_rp = 1.0, v_m_cost = 1.03558225762, v_rm = 0.7
取出10前有这些容器： [10, 12, 20, 35]
取出10后有： [12, 20, 35] v_p_cost=0.982766268785, v_rp = 1.0, v_m_cost = 0.900620011387, v_rm = 0.7
取出35前有这些容器： [12, 20, 35]
取出35后有： [12, 20] v_p_cost=0.889014031944, v_rp = 1.0, v_m_cost = 0.764742511212, v_rm = 0.7
取出20前有这些容器： [12, 20]
取出20后有： [12] v_p_cost=0.497622833867, v_rp = 1.0, v_m_cost = 0.323643319364, v_rm = 0.7
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
8
修改hm过载  h_id = 33, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 24]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 34, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [39, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 1.0]
47
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [22, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 1.0]
45
修改hm过载  h_id = 47, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [36, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
36
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.731251688933, v_rp = 0.5, v_m_cost = 0.390003147179, v_rm = 0.5
取出36前有这些容器： [24, 36, 42]
取出36后有： [24, 42] v_p_cost=0.665557473929, v_rp = 0.5, v_m_cost = 0.331903670631, v_rm = 0.5
取出42前有这些容器： [24, 42]
取出42后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 4, v_p_cost = 0.637152487597, v_rp = 0.3, v_m_cost = 0.734827930047, v_rm = 1.0
取出6前有这些容器： [6, 21, 32]
取出6后有： [21, 32] v_p_cost=0.552961213111, v_rp = 0.3, v_m_cost = 0.519174988447, v_rm = 1.0
取出32前有这些容器： [21, 32]
取出32后有： [21] v_p_cost=0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 1.0
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=1.11022302463e-16, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.72683330819, v_rp = 0.5, v_m_cost = 0.659038195253, v_rm = 0.7
取出3前有这些容器： [2, 3, 17, 49]
取出3后有： [2, 17, 49] v_p_cost=0.669326258507, v_rp = 0.5, v_m_cost = 0.657758598719, v_rm = 0.7
取出2前有这些容器： [2, 17, 49]
取出2后有： [17, 49] v_p_cost=0.5661833746, v_rp = 0.5, v_m_cost = 0.470041613783, v_rm = 0.7
取出49前有这些容器： [17, 49]
取出49后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.620515574944, v_rp = 0.7, v_m_cost = 0.847997753156, v_rm = 0.7
取出9前有这些容器： [9, 48]
取出9后有： [48] v_p_cost=0.339680823305, v_rp = 0.7, v_m_cost = 0.363667195512, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.600863730274, v_rp = 0.3, v_m_cost = 0.608764935828, v_rm = 0.3
取出38前有这些容器： [11, 38]
取出38后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 0.3
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.578088344606, v_rp = 0.7, v_m_cost = 0.482181175573, v_rm = 0.3
取出28前有这些容器： [20, 28]
取出28后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.875927638913, v_rp = 0.5, v_m_cost = 0.598337805578, v_rm = 0.7
取出7前有这些容器： [7, 12]
取出7后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 43, v_p_cost = 1.21659393997, v_rp = 1.0, v_m_cost = 1.07828508509, v_rm = 0.7
取出35前有这些容器： [0, 13, 14, 35]
取出35后有： [0, 13, 14] v_p_cost=1.12284170313, v_rp = 1.0, v_m_cost = 0.942407584916, v_rm = 0.7
取出13前有这些容器： [0, 13, 14]
取出13后有： [0, 14] v_p_cost=0.939363290784, v_rp = 1.0, v_m_cost = 0.742432011382, v_rm = 0.7
取出0前有这些容器： [0, 14]
取出0后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.7
修改hm过载  h_id = 5, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [3, 13, 34]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.7],mem尺寸[0.7, 0.3, 0.5]
3
修改hm过载  h_id = 7, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [5, 16]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
5
修改hm过载  h_id = 9, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 1.0]
0
修改hm过载  h_id = 12, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 15, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [41, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 24, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 24]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 28, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 39]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.5]
31
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
26
修改hm过载  h_id = 43, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 29, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.5],mem尺寸[0.7, 0.3, 0.7]
12
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.587436481592, v_rp = 0.5, v_m_cost = 0.519716510421, v_rm = 0.5
取出30前有这些容器： [17, 30]
取出30后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 4, v_p_cost = 0.499823564731, v_rp = 0.3, v_m_cost = 0.449900499911, v_rm = 1.0
取出40前有这些容器： [14, 40]
取出40后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 1.0
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.676517251337, v_rp = 0.5, v_m_cost = 0.863345011277, v_rm = 0.7
取出9前有这些容器： [9, 19]
取出9后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.7
修改vm超载的情况 v_id = 7, v_p_cost = 1.44571280959, v_rp = 1.0, v_m_cost = 1.17670839908, v_rm = 0.7
取出33前有这些容器： [11, 18, 24, 33]
取出33后有： [11, 18, 24] v_p_cost=1.14831984411, v_rp = 1.0, v_m_cost = 0.86818327951, v_rm = 0.7
取出11前有这些容器： [11, 18, 24]
取出11后有： [18, 24] v_p_cost=0.829185213511, v_rp = 1.0, v_m_cost = 0.57940894231, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.337448423714, v_rp = 0.3, v_m_cost = 0.337271981915, v_rm = 0.3
取出45前有这些容器： [4, 15, 45]
取出45后有： [4, 15] v_p_cost=0.250268504879, v_rp = 0.3, v_m_cost = 0.315899267252, v_rm = 0.3
取出4前有这些容器： [4, 15]
取出4后有： [15] v_p_cost=0.149761812475, v_rp = 0.3, v_m_cost = 0.213302100325, v_rm = 0.3
修改vm超载的情况 v_id = 21, v_p_cost = 0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 24, v_p_cost = 1.10273034724, v_rp = 1.0, v_m_cost = 1.30101396892, v_rm = 0.5
取出10前有这些容器： [5, 10, 26, 31]
取出10后有： [5, 26, 31] v_p_cost=1.02459290883, v_rp = 1.0, v_m_cost = 1.16605172268, v_rm = 0.5
取出26前有这些容器： [5, 26, 31]
取出26后有： [5, 31] v_p_cost=0.814220560998, v_rp = 1.0, v_m_cost = 0.942478954044, v_rm = 0.5
取出31前有这些容器： [5, 31]
取出31后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 30, v_p_cost = 1.42777732054, v_rp = 0.7, v_m_cost = 1.46626848205, v_rm = 0.7
取出35前有这些容器： [1, 34, 35, 38, 48]
取出35后有： [1, 34, 38, 48] v_p_cost=1.3340250837, v_rp = 0.7, v_m_cost = 1.33039098188, v_rm = 0.7
取出38前有这些容器： [1, 34, 38, 48]
取出38后有： [1, 34, 48] v_p_cost=1.05229598403, v_rp = 0.7, v_m_cost = 1.01040038325, v_rm = 0.7
取出34前有这些容器： [1, 34, 48]
取出34后有： [1, 48] v_p_cost=0.723421882435, v_rp = 0.7, v_m_cost = 0.683446215117, v_rm = 0.7
取出48前有这些容器： [1, 48]
取出48后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 38, v_p_cost = 0.7443922144, v_rp = 1.0, v_m_cost = 0.799856228816, v_rm = 0.7
取出8前有这些容器： [8, 20]
取出8后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 42, v_p_cost = 0.893246340407, v_rp = 0.5, v_m_cost = 0.67290254843, v_rm = 0.5
取出46前有这些容器： [12, 46]
取出46后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 1.12851431837, v_rp = 0.7, v_m_cost = 1.00207243307, v_rm = 0.7
取出28前有这些容器： [23, 28, 47]
取出28后有： [23, 47] v_p_cost=0.941817171839, v_rp = 0.7, v_m_cost = 0.960990449345, v_rm = 0.7
取出23前有这些容器： [23, 47]
取出23后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [8, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
8
修改hm过载  h_id = 6, h_p_cost = 1.3, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [2, 13]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[1.0, 0.3]
13
修改hm过载  h_id = 16, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 18, h_p_cost = 1.1, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [3, 29, 40]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.3],mem尺寸[0.7, 0.3, 0.5]
3
修改hm过载  h_id = 21, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [6, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [23, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 35, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 36, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 24]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [31, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 43, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [34, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
34
修改hm过载  h_id = 47, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 4]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 1.0
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 6, v_p_cost = 1.12485983577, v_rp = 0.7, v_m_cost = 0.904390656251, v_rm = 0.7
取出13前有这些容器： [1, 8, 13, 42]
取出13后有： [1, 8, 42] v_p_cost=0.941381423427, v_rp = 0.7, v_m_cost = 0.704415082718, v_rm = 0.7
取出42前有这些容器： [1, 8, 42]
取出42后有： [1, 8] v_p_cost=0.736742075453, v_rp = 0.7, v_m_cost = 0.678536056573, v_rm = 0.7
取出8前有这些容器： [1, 8]
取出8后有： [1] v_p_cost=0.38374105913, v_rp = 0.7, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 0.65039939714, v_rp = 0.7, v_m_cost = 0.565055020268, v_rm = 0.5
取出11前有这些容器： [11, 22]
取出11后有： [22] v_p_cost=0.331264766544, v_rp = 0.7, v_m_cost = 0.276280683068, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.395682499698, v_rp = 0.7, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 28, v_p_cost = 0.94241144097, v_rp = 1.0, v_m_cost = 0.792697958623, v_rm = 0.5
取出0前有这些容器： [0, 47]
取出0后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 29, v_p_cost = 0.417727913425, v_rp = 0.5, v_m_cost = 0.385794620356, v_rm = 0.3
取出4前有这些容器： [4, 43]
取出4后有： [43] v_p_cost=0.317221221021, v_rp = 0.5, v_m_cost = 0.28319745343, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 1.22634425735, v_rp = 0.5, v_m_cost = 1.18978790524, v_rm = 0.7
取出18前有这些容器： [18, 23, 31]
取出18后有： [23, 31] v_p_cost=0.858077169793, v_rp = 0.5, v_m_cost = 0.916403607421, v_rm = 0.7
取出31前有这些容器： [23, 31]
取出31后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 36, v_p_cost = 1.04041111572, v_rp = 0.7, v_m_cost = 0.807347825966, v_rm = 0.5
取出40前有这些容器： [16, 34, 39, 40]
取出40后有： [16, 34, 39] v_p_cost=1.01851583115, v_rp = 0.7, v_m_cost = 0.794309779698, v_rm = 0.5
取出39前有这些容器： [16, 34, 39]
取出39后有： [16, 34] v_p_cost=0.826213932273, v_rp = 0.7, v_m_cost = 0.643216316621, v_rm = 0.5
取出34前有这些容器： [16, 34]
取出34后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.975551114026, v_rp = 0.5, v_m_cost = 0.760505773007, v_rm = 1.0
取出14前有这些容器： [12, 14]
取出14后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改vm超载的情况 v_id = 48, v_p_cost = 0.698713232377, v_rp = 1.0, v_m_cost = 0.819927993713, v_rm = 0.7
取出38前有这些容器： [5, 38]
取出38后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.7
修改hm过载  h_id = 3, h_p_cost = 1.4, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [18, 41]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.3, 0.5]
18
修改hm过载  h_id = 12, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 26, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 8]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 28, h_p_cost = 1.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [45, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 1.0]
45
修改hm过载  h_id = 31, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 33, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 25]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
25
修改hm过载  h_id = 37, h_p_cost = 2.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [0, 34, 49]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 1.0],mem尺寸[0.5, 0.5, 0.5]
0
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.5]
34
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
49
修改hm过载  h_id = 40, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 27]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 44, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 6]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.7]
6
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [23, 29]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.3]
29
进入mbbode_rank
[5, 13, 8, 9, 5] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 9, 4: 21, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 32: 47, 34: 23, 36: 49, 37: 22, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 7, v_p_cost = 0.911203569814, v_rp = 1.0, v_m_cost = 0.767851225744, v_rm = 0.7
取出21前有这些容器： [21, 47]
取出21后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.848004158303, v_rp = 0.5, v_m_cost = 0.851447126889, v_rm = 0.7
取出2前有这些容器： [2, 30, 31, 42]
取出2后有： [30, 31, 42] v_p_cost=0.744861274395, v_rp = 0.5, v_m_cost = 0.663730141954, v_rm = 0.7
取出30前有这些容器： [30, 31, 42]
取出30后有： [31, 42] v_p_cost=0.601875776273, v_rp = 0.5, v_m_cost = 0.468420585104, v_rm = 0.7
取出42前有这些容器： [31, 42]
取出42后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 23, v_p_cost = 0.627929395814, v_rp = 0.7, v_m_cost = 0.524382527105, v_rm = 0.5
取出13前有这些容器： [13, 17]
取出13后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 27, v_p_cost = 0.214198014117, v_rp = 0.7, v_m_cost = 0.315508237313, v_rm = 0.3
取出27前有这些容器： [10, 27, 49]
取出27后有： [10, 49] v_p_cost=0.199869829545, v_rp = 0.7, v_m_cost = 0.280596906446, v_rm = 0.3
修改vm超载的情况 v_id = 28, v_p_cost = 0.598950320699, v_rp = 1.0, v_m_cost = 0.603188052058, v_rm = 0.5
取出38前有这些容器： [38, 43]
取出38后有： [43] v_p_cost=0.317221221021, v_rp = 1.0, v_m_cost = 0.28319745343, v_rm = 0.5
修改vm超载的情况 v_id = 32, v_p_cost = 0.870202695527, v_rp = 1.0, v_m_cost = 0.818390844988, v_rm = 0.7
取出4前有这些容器： [4, 7, 20]
取出4后有： [7, 20] v_p_cost=0.769696003122, v_rp = 1.0, v_m_cost = 0.715793678061, v_rm = 0.7
取出7前有这些容器： [7, 20]
取出7后有： [20] v_p_cost=0.391391198077, v_rp = 1.0, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.565426618951, v_rp = 0.5, v_m_cost = 0.434029977966, v_rm = 1.0
取出45前有这些容器： [1, 29, 45]
取出45后有： [1, 29] v_p_cost=0.478246700116, v_rp = 0.5, v_m_cost = 0.412657263303, v_rm = 1.0
修改vm超载的情况 v_id = 48, v_p_cost = 0.958463575361, v_rp = 1.0, v_m_cost = 0.797505367826, v_rm = 0.7
取出23前有这些容器： [12, 23]
取出23后有： [12] v_p_cost=0.497622833867, v_rp = 1.0, v_m_cost = 0.323643319364, v_rm = 0.7
修改hm过载  h_id = 2, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 12, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 5]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 23]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 30, h_p_cost = 2.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [28, 32, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 0.7],mem尺寸[0.5, 0.7, 0.5]
41
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.7]
28
修改hm过载  h_id = 38, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [9, 22]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 1.0]
22
修改hm过载  h_id = 43, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.510145198473, v_rp = 0.5, v_m_cost = 0.382506430119, v_rm = 0.7
取出36前有这些容器： [17, 36]
取出36后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.575482071331, v_rp = 0.5, v_m_cost = 0.580006644582, v_rm = 0.7
取出29前有这些容器： [29, 47]
取出29后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.670222237344, v_rp = 0.3, v_m_cost = 0.641954490398, v_rm = 0.5
取出43前有这些容器： [8, 43]
取出43后有： [8] v_p_cost=0.353001016323, v_rp = 0.3, v_m_cost = 0.358757036968, v_rm = 0.5
取出8前有这些容器： [8]
取出8后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.746571892601, v_rp = 0.5, v_m_cost = 0.548078784037, v_rm = 0.3
取出18前有这些容器： [7, 18]
取出18后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.816593085007, v_rp = 0.5, v_m_cost = 0.659437677215, v_rm = 0.7
取出46前有这些容器： [41, 46]
取出46后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.995294822154, v_rp = 0.5, v_m_cost = 0.942433393184, v_rm = 1.0
取出30前有这些容器： [20, 24, 30]
取出30后有： [20, 24] v_p_cost=0.852309324032, v_rp = 0.5, v_m_cost = 0.747123836334, v_rm = 1.0
取出20前有这些容器： [20, 24]
取出20后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 1.0
修改vm超载的情况 v_id = 49, v_p_cost = 0.932594603107, v_rp = 1.0, v_m_cost = 0.688657790667, v_rm = 0.5
取出44前有这些容器： [11, 16, 44]
取出44后有： [11, 16] v_p_cost=0.816474461279, v_rp = 1.0, v_m_cost = 0.60503648569, v_rm = 0.5
取出11前有这些容器： [11, 16]
取出11后有： [16] v_p_cost=0.497339830683, v_rp = 1.0, v_m_cost = 0.31626214849, v_rm = 0.5
修改hm过载  h_id = 18, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [43, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 32, h_p_cost = 2.0, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 0.5]
28
修改hm过载  h_id = 36, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 46]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 44, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [21, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 1.0]
21
修改hm过载  h_id = 45, h_p_cost = 2.7, h_m_cost = 2.3
该物理机上放置的虚拟机为：  [2, 27, 35]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 1.0],mem尺寸[1.0, 0.3, 1.0]
27
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 1.0]
2
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [36, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 49, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 23]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
6
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 7, v_p_cost = 0.798197651366, v_rp = 1.0, v_m_cost = 0.770325854313, v_rm = 0.7
取出43前有这些容器： [43, 47]
取出43后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.569239048439, v_rp = 0.5, v_m_cost = 0.597269940878, v_rm = 0.7
取出29前有这些容器： [8, 29, 49]
取出29后有： [8, 49] v_p_cost=0.474733407453, v_rp = 0.5, v_m_cost = 0.50439169718, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.451608175233, v_rp = 1.0, v_m_cost = 0.565406331718, v_rm = 0.5
取出32前有这些容器： [32, 34]
取出32后有： [34] v_p_cost=0.32887410159, v_rp = 1.0, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.689479200464, v_rp = 0.5, v_m_cost = 0.725261242202, v_rm = 0.7
取出37前有这些容器： [7, 37]
取出37后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.7
修改vm超载的情况 v_id = 17, v_p_cost = 0.865662674506, v_rp = 0.7, v_m_cost = 0.803614141312, v_rm = 0.7
取出28前有这些容器： [28, 31, 38]
取出28后有： [31, 38] v_p_cost=0.678965527977, v_rp = 0.7, v_m_cost = 0.762532157587, v_rm = 0.7
取出38前有这些容器： [31, 38]
取出38后有： [31] v_p_cost=0.397236428299, v_rp = 0.7, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 1.01422449044, v_rp = 0.7, v_m_cost = 0.949760270049, v_rm = 0.5
取出27前有这些容器： [10, 23, 24, 27]
取出27后有： [10, 23, 24] v_p_cost=0.999896305865, v_rp = 0.7, v_m_cost = 0.914848939183, v_rm = 0.5
取出10前有这些容器： [10, 23, 24]
取出10后有： [23, 24] v_p_cost=0.92175886745, v_rp = 0.7, v_m_cost = 0.779886692948, v_rm = 0.5
取出23前有这些容器： [23, 24]
取出23后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.731072021382, v_rp = 0.7, v_m_cost = 0.80476638736, v_rm = 0.5
取出48前有这些容器： [20, 48]
取出48后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 0.613271477347, v_rp = 0.5, v_m_cost = 0.461271911226, v_rm = 1.0
取出39前有这些容器： [39, 41]
取出39后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 1.0
修改vm超载的情况 v_id = 49, v_p_cost = 0.763949587253, v_rp = 1.0, v_m_cost = 0.652398751456, v_rm = 0.5
取出18前有这些容器： [18, 19]
取出18后有： [19] v_p_cost=0.395682499698, v_rp = 1.0, v_m_cost = 0.379014453633, v_rm = 0.5
修改hm过载  h_id = 7, h_p_cost = 1.7, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [22, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 0.5]
22
修改hm过载  h_id = 15, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 22, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 29, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
33
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [34, 43]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.5, 0.7]
34
修改hm过载  h_id = 43, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [28, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 49, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 20]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.752234345011, v_rp = 0.5, v_m_cost = 0.586459131217, v_rm = 0.5
取出22前有这些容器： [22, 41]
取出22后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.5
修改vm超载的情况 v_id = 1, v_p_cost = 0.953263870836, v_rp = 0.7, v_m_cost = 0.733895292179, v_rm = 1.0
取出42前有这些容器： [8, 42, 46]
取出42后有： [8, 46] v_p_cost=0.748624522863, v_rp = 0.7, v_m_cost = 0.708016266034, v_rm = 1.0
取出8前有这些容器： [8, 46]
取出8后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 1.0
修改vm超载的情况 v_id = 6, v_p_cost = 1.14284230019, v_rp = 0.7, v_m_cost = 0.927456012595, v_rm = 0.7
取出34前有这些容器： [1, 21, 34]
取出34后有： [1, 21] v_p_cost=0.813968198599, v_rp = 0.7, v_m_cost = 0.600501844464, v_rm = 0.7
取出1前有这些容器： [1, 21]
取出1后有： [21] v_p_cost=0.430227139469, v_rp = 0.7, v_m_cost = 0.28072282486, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 20, v_p_cost = 0.54017337111, v_rp = 0.5, v_m_cost = 0.560256348896, v_rm = 0.7
取出3前有这些容器： [3, 30, 48]
取出3后有： [30, 48] v_p_cost=0.482666321427, v_rp = 0.5, v_m_cost = 0.558976752362, v_rm = 0.7
修改vm超载的情况 v_id = 31, v_p_cost = 0.689479200464, v_rp = 0.5, v_m_cost = 0.725261242202, v_rm = 0.5
取出37前有这些容器： [7, 37]
取出37后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.958180572177, v_rp = 0.5, v_m_cost = 0.790124196951, v_rm = 0.7
取出23前有这些容器： [16, 23]
取出23后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.5
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 47, v_p_cost = 1.05974238851, v_rp = 0.5, v_m_cost = 0.976158714606, v_rm = 1.0
取出6前有这些容器： [6, 12, 14]
取出6后有： [12, 14] v_p_cost=0.975551114026, v_rp = 0.5, v_m_cost = 0.760505773007, v_rm = 1.0
取出14前有这些容器： [12, 14]
取出14后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改hm过载  h_id = 5, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 11, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [35, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
45
修改hm过载  h_id = 12, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [12, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 1.0]
12
修改hm过载  h_id = 14, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [14, 18]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
14
修改hm过载  h_id = 33, h_p_cost = 2.2, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [0, 30, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 1.0],mem尺寸[0.5, 0.7, 0.7]
0
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
30
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.7]
38
修改hm过载  h_id = 36, h_p_cost = 2.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [24, 33, 36]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7],mem尺寸[0.5, 0.7, 0.5]
33
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
36
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
24
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [39, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 1.0]
47
修改hm过载  h_id = 44, h_p_cost = 2.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 28, 31]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 0.5],mem尺寸[1.0, 0.5, 0.5]
31
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.5]
2
修改hm过载  h_id = 48, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 49, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [1, 40]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.3],mem尺寸[1.0, 0.5]
40
进入mbbode_rank
[3, 9, 7, 9, 12] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 21], [44, 2], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [10, 29], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [39, 2], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.701370422678, v_rp = 0.5, v_m_cost = 0.711362102755, v_rm = 0.5
取出4前有这些容器： [4, 11, 38]
取出4后有： [11, 38] v_p_cost=0.600863730274, v_rp = 0.5, v_m_cost = 0.608764935828, v_rm = 0.5
取出38前有这些容器： [11, 38]
取出38后有： [11] v_p_cost=0.319134630596, v_rp = 0.5, v_m_cost = 0.2887743372, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.392632989618, v_rp = 0.7, v_m_cost = 0.30960581708, v_rm = 0.3
取出27前有这些容器： [7, 27]
取出27后有： [7] v_p_cost=0.378304805046, v_rp = 0.7, v_m_cost = 0.274694486214, v_rm = 0.3
修改hm过载  h_id = 2, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [41, 44]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 20]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.856233085204, v_rp = 0.5, v_m_cost = 0.711556939856, v_rm = 0.7
取出7前有这些容器： [7, 14]
取出7后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.452997157673, v_rp = 0.7, v_m_cost = 0.42191534328, v_rm = 0.3
取出49前有这些容器： [22, 49]
取出49后有： [22] v_p_cost=0.331264766544, v_rp = 0.7, v_m_cost = 0.276280683068, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.5
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 0.822610924894, v_rp = 0.7, v_m_cost = 0.890434556266, v_rm = 0.7
取出39前有这些容器： [11, 37, 39]
取出39后有： [11, 37] v_p_cost=0.630309026015, v_rp = 0.7, v_m_cost = 0.739341093188, v_rm = 0.7
取出37前有这些容器： [11, 37]
取出37后有： [11] v_p_cost=0.319134630596, v_rp = 0.7, v_m_cost = 0.2887743372, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.524732780454, v_rp = 0.5, v_m_cost = 0.373601068558, v_rm = 1.0
取出29前有这些容器： [21, 29]
取出29后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 1.0
修改hm过载  h_id = 3, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 6, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [14, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 7, h_p_cost = 1.7, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [17, 35]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 1.0]
17
修改hm过载  h_id = 16, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [46, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 32, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 36, h_p_cost = 1.5, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [28, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 42, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 15, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 0.5
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.726947266241, v_rp = 0.5, v_m_cost = 0.655295136701, v_rm = 1.0
取出22前有这些容器： [19, 22]
取出22后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 1.0
修改vm超载的情况 v_id = 17, v_p_cost = 0.664175411742, v_rp = 0.7, v_m_cost = 0.809323792956, v_rm = 0.7
取出37前有这些容器： [8, 37]
取出37后有： [8] v_p_cost=0.353001016323, v_rp = 0.7, v_m_cost = 0.358757036968, v_rm = 0.7
修改vm超载的情况 v_id = 20, v_p_cost = 0.681101246211, v_rp = 0.5, v_m_cost = 0.523618892898, v_rm = 0.7
取出13前有这些容器： [12, 13]
取出13后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 29, v_p_cost = 0.743355871803, v_rp = 0.5, v_m_cost = 0.671451081441, v_rm = 0.3
取出49前有这些容器： [5, 42, 49]
取出49后有： [5, 42] v_p_cost=0.621623480673, v_rp = 0.5, v_m_cost = 0.525816421229, v_rm = 0.3
取出42前有这些容器： [5, 42]
取出42后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.998524730921, v_rp = 0.5, v_m_cost = 0.699369310865, v_rm = 0.7
取出44前有这些容器： [0, 41, 44]
取出44后有： [0, 41] v_p_cost=0.882404589092, v_rp = 0.5, v_m_cost = 0.615748005888, v_rm = 0.7
取出41前有这些容器： [0, 41]
取出41后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.636355851617, v_rp = 0.3, v_m_cost = 0.57197179063, v_rm = 0.5
取出43前有这些容器： [11, 43]
取出43后有： [11] v_p_cost=0.319134630596, v_rp = 0.3, v_m_cost = 0.2887743372, v_rm = 0.5
取出11前有这些容器： [11]
取出11后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 1.33588828908, v_rp = 0.5, v_m_cost = 1.49590166, v_rm = 1.0
取出15前有这些容器： [9, 15, 17, 23]
取出15后有： [9, 17, 23] v_p_cost=1.1861264766, v_rp = 0.5, v_m_cost = 1.28259955968, v_rm = 1.0
取出9前有这些容器： [9, 17, 23]
取出9后有： [17, 23] v_p_cost=0.905291724964, v_rp = 0.5, v_m_cost = 0.798269002033, v_rm = 1.0
取出17前有这些容器： [17, 23]
取出17后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 1.0
修改hm过载  h_id = 5, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [33, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
33
修改hm过载  h_id = 7, h_p_cost = 1.2, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 1.0]
16
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 14, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 20, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [15, 28]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.5]
15
修改hm过载  h_id = 28, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [19, 37]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 0.7]
37
修改hm过载  h_id = 34, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 9]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 41, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [41, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
47
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [21, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.3, 0.5]
21
修改hm过载  h_id = 43, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 9, v_p_cost = 1.27133569123, v_rp = 1.0, v_m_cost = 1.12210650926, v_rm = 0.5
取出15前有这些容器： [0, 15, 22, 34]
取出15后有： [0, 22, 34] v_p_cost=1.12157387876, v_rp = 1.0, v_m_cost = 0.908804408938, v_rm = 0.5
取出34前有这些容器： [0, 22, 34]
取出34后有： [0, 22] v_p_cost=0.792699777169, v_rp = 1.0, v_m_cost = 0.581850240807, v_rm = 0.5
取出22前有这些容器： [0, 22]
取出22后有： [0] v_p_cost=0.461435010625, v_rp = 1.0, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.619072221813, v_rp = 0.3, v_m_cost = 0.461896808702, v_rm = 0.5
取出49前有这些容器： [16, 49]
取出49后有： [16] v_p_cost=0.497339830683, v_rp = 0.3, v_m_cost = 0.31626214849, v_rm = 0.5
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 20, v_p_cost = 0.708410823718, v_rp = 0.5, v_m_cost = 0.893108314947, v_rm = 0.7
取出37前有这些容器： [31, 37]
取出37后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 24, v_p_cost = 1.10247244128, v_rp = 1.0, v_m_cost = 1.05651914634, v_rm = 0.5
取出43前有这些容器： [5, 18, 43]
取出43后有： [5, 18] v_p_cost=0.785251220255, v_rp = 1.0, v_m_cost = 0.773321692908, v_rm = 0.5
取出18前有这些容器： [5, 18]
取出18后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.658815453901, v_rp = 0.5, v_m_cost = 0.652441532712, v_rm = 0.7
取出11前有这些容器： [11, 48]
取出11后有： [48] v_p_cost=0.339680823305, v_rp = 0.5, v_m_cost = 0.363667195512, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.958540959823, v_rp = 0.7, v_m_cost = 0.629667963851, v_rm = 0.5
取出24前有这些容器： [12, 24]
取出24后有： [12] v_p_cost=0.497622833867, v_rp = 0.7, v_m_cost = 0.323643319364, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.583693096956, v_rp = 0.7, v_m_cost = 0.592192654925, v_rm = 0.5
取出39前有这些容器： [20, 39]
取出39后有： [20] v_p_cost=0.391391198077, v_rp = 0.7, v_m_cost = 0.441099191848, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.866544484505, v_rp = 0.7, v_m_cost = 0.690410963333, v_rm = 0.5
取出45前有这些容器： [1, 45, 46]
取出45后有： [1, 46] v_p_cost=0.77936456567, v_rp = 0.7, v_m_cost = 0.66903824867, v_rm = 0.5
取出1前有这些容器： [1, 46]
取出1后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.5
修改vm超载的情况 v_id = 49, v_p_cost = 1.03628198699, v_rp = 1.0, v_m_cost = 0.883310047133, v_rm = 0.5
取出26前有这些容器： [19, 21, 26]
取出26后有： [19, 21] v_p_cost=0.825909639166, v_rp = 1.0, v_m_cost = 0.659737278493, v_rm = 0.5
取出19前有这些容器： [19, 21]
取出19后有： [21] v_p_cost=0.430227139469, v_rp = 1.0, v_m_cost = 0.28072282486, v_rm = 0.5
修改hm过载  h_id = 2, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 12]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
12
修改hm过载  h_id = 8, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 11]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 9, h_p_cost = 1.7, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [46, 49]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
46
修改hm过载  h_id = 11, h_p_cost = 1.5, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [19, 47]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[1.0, 1.0]
47
修改hm过载  h_id = 24, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 25, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 42]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 27, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [16, 37]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[1.0, 0.7]
16
修改hm过载  h_id = 31, h_p_cost = 1.3, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [15, 48]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.7]
15
修改hm过载  h_id = 36, h_p_cost = 2.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [2, 24]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.5]
2
修改hm过载  h_id = 38, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 5]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 40, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [20, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
20
修改hm过载  h_id = 42, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
33
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.353160051116, v_rp = 0.3, v_m_cost = 0.289318729336, v_rm = 1.0
取出40前有这些容器： [22, 40]
取出40后有： [22] v_p_cost=0.331264766544, v_rp = 0.3, v_m_cost = 0.276280683068, v_rm = 1.0
取出22前有这些容器： [22]
取出22后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 12, v_p_cost = 0.842443652103, v_rp = 0.5, v_m_cost = 0.935726332806, v_rm = 0.7
取出15前有这些容器： [8, 15, 48]
取出15后有： [8, 48] v_p_cost=0.692681839628, v_rp = 0.5, v_m_cost = 0.72242423248, v_rm = 0.7
取出48前有这些容器： [8, 48]
取出48后有： [8] v_p_cost=0.353001016323, v_rp = 0.5, v_m_cost = 0.358757036968, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.992156915852, v_rp = 0.3, v_m_cost = 0.952459496148, v_rm = 0.3
取出2前有这些容器： [2, 12, 20]
取出2后有： [12, 20] v_p_cost=0.889014031944, v_rp = 0.3, v_m_cost = 0.764742511212, v_rm = 0.3
取出20前有这些容器： [12, 20]
取出20后有： [12] v_p_cost=0.497622833867, v_rp = 0.3, v_m_cost = 0.323643319364, v_rm = 0.3
取出12前有这些容器： [12]
取出12后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 1.39623768931, v_rp = 0.7, v_m_cost = 1.06330305028, v_rm = 0.5
取出41前有这些容器： [14, 16, 41]
取出41后有： [14, 16] v_p_cost=0.975268110841, v_rp = 0.7, v_m_cost = 0.753124602132, v_rm = 0.5
取出14前有这些容器： [14, 16]
取出14后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.5
修改vm超载的情况 v_id = 32, v_p_cost = 0.780977487429, v_rp = 1.0, v_m_cost = 0.762320578564, v_rm = 0.7
取出1前有这些容器： [1, 31]
取出1后有： [31] v_p_cost=0.397236428299, v_rp = 1.0, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.559113868761, v_rp = 0.7, v_m_cost = 0.622090647119, v_rm = 0.5
取出10前有这些容器： [10, 47]
取出10后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 36, v_p_cost = 0.479814781026, v_rp = 0.7, v_m_cost = 0.564912170665, v_rm = 0.5
取出6前有这些容器： [6, 46]
取出6后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 0.785251220255, v_rp = 1.0, v_m_cost = 0.773321692908, v_rm = 0.7
取出18前有这些容器： [5, 18]
取出18后有： [5] v_p_cost=0.416984132699, v_rp = 1.0, v_m_cost = 0.499937395085, v_rm = 0.7
修改hm过载  h_id = 7, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 16]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 12, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [17, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.3]
17
修改hm过载  h_id = 22, h_p_cost = 2.5, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [24, 25, 35]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 1.0],mem尺寸[0.5, 0.7, 1.0]
25
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.5, 1.0]
24
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
35
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 25, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 44]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 27, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 34, h_p_cost = 1.7, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [30, 32]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.7]
30
修改hm过载  h_id = 45, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [8, 47]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
8
进入mbbode_rank
[3, 13, 12, 6, 6] 0
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[30, 15], [38, 27], [4, 21], [13, 9], [10, 38], [47, 0], [15, 38], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 21], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [3, 9], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]] 3 {1: 34, 3: 9, 4: 21, 6: 36, 7: 44, 8: 13, 10: 38, 11: 17, 12: 28, 13: 9, 14: 26, 15: 38, 16: 37, 19: 35, 22: 31, 24: 1, 25: 24, 28: 40, 29: 46, 30: 15, 32: 47, 34: 23, 36: 49, 37: 22, 38: 27, 39: 43, 40: 17, 41: 2, 43: 39, 44: 4, 45: 18, 46: 10, 47: 0, 48: 7, 49: 3} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.7
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改hm过载  h_id = 21, h_p_cost = 1.3, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[1.0, 1.0]
4
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 7, v_p_cost = 0.859281235391, v_rp = 1.0, v_m_cost = 0.761822887097, v_rm = 0.7
取出7前有这些容器： [7, 47]
取出7后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.272619563132, v_rp = 0.3, v_m_cost = 0.512204581735, v_rm = 0.3
取出36前有这些容器： [6, 32, 36]
取出36后有： [6, 32] v_p_cost=0.206925348129, v_rp = 0.3, v_m_cost = 0.454105105187, v_rm = 0.3
取出6前有这些容器： [6, 32]
取出6后有： [32] v_p_cost=0.122734073643, v_rp = 0.3, v_m_cost = 0.238452163587, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.578088344606, v_rp = 0.5, v_m_cost = 0.482181175573, v_rm = 0.3
取出28前有这些容器： [20, 28]
取出28后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.3
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 45, v_p_cost = 0.627356480526, v_rp = 0.5, v_m_cost = 0.723510163725, v_rm = 1.0
取出26前有这些容器： [5, 26]
取出26后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 1.0
修改vm超载的情况 v_id = 47, v_p_cost = 0.769907962774, v_rp = 0.5, v_m_cost = 0.644390020372, v_rm = 1.0
取出48前有这些容器： [21, 48]
取出48后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 1.0
修改hm过载  h_id = 0, h_p_cost = 2.1, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [3, 7, 13, 45]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0, 0.3, 0.5],mem尺寸[0.7, 0.7, 0.3, 1.0]
3
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3, 0.5],mem尺寸[0.7, 0.3, 1.0]
13
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
45
修改hm过载  h_id = 1, h_p_cost = 3.0, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [19, 38, 49]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 1.0],mem尺寸[1.0, 0.7, 0.5]
19
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.5]
38
修改hm过载  h_id = 19, h_p_cost = 1.3, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 24, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 40, h_p_cost = 2.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [2, 32]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[1.0, 0.7]
2
修改hm过载  h_id = 44, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 46, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [17, 41]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
17
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.759101241059, v_rp = 0.5, v_m_cost = 0.60767699299, v_rm = 0.5
取出34前有这些容器： [21, 34]
取出34后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 10, v_p_cost = 0.810659074996, v_rp = 0.5, v_m_cost = 0.723519941459, v_rm = 0.5
取出30前有这些容器： [28, 30, 47]
取出30后有： [28, 47] v_p_cost=0.667673576874, v_rp = 0.5, v_m_cost = 0.528210384609, v_rm = 0.5
取出28前有这些容器： [28, 47]
取出28后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.806190565703, v_rp = 0.5, v_m_cost = 0.739051087136, v_rm = 1.0
取出3前有这些容器： [3, 8, 19]
取出3后有： [8, 19] v_p_cost=0.748683516021, v_rp = 0.5, v_m_cost = 0.737771490601, v_rm = 1.0
取出8前有这些容器： [8, 19]
取出8后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 1.0
修改vm超载的情况 v_id = 21, v_p_cost = 0.746571892601, v_rp = 0.5, v_m_cost = 0.548078784037, v_rm = 0.3
取出18前有这些容器： [7, 18]
取出18后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.416984132699, v_rp = 0.7, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 39, v_p_cost = 0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 43, v_p_cost = 0.99940455103, v_rp = 1.0, v_m_cost = 0.849638068718, v_rm = 0.7
取出4前有这些容器： [4, 14, 41]
取出4后有： [14, 41] v_p_cost=0.898897858626, v_rp = 1.0, v_m_cost = 0.747040901791, v_rm = 0.7
取出41前有这些容器： [14, 41]
取出41后有： [14] v_p_cost=0.477928280159, v_rp = 1.0, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 47, v_p_cost = 0.922353136581, v_rp = 0.5, v_m_cost = 0.611594202226, v_rm = 1.0
取出24前有这些容器： [0, 24]
取出24后有： [0] v_p_cost=0.461435010625, v_rp = 0.5, v_m_cost = 0.305569557739, v_rm = 1.0
修改hm过载  h_id = 1, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 17]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 4, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [42, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.5, 0.7]
42
修改hm过载  h_id = 14, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 48]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 20, h_p_cost = 2.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [28, 41, 46]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 0.7],mem尺寸[0.5, 0.5, 0.7]
41
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.7]
46
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
37
修改hm过载  h_id = 27, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [7, 26]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.7]
26
修改hm过载  h_id = 30, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 5]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 35, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [21, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
21
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [11, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 40, h_p_cost = 1.7, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [1, 19]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[1.0, 1.0]
1
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.725306151191, v_rp = 0.3, v_m_cost = 0.585650769641, v_rm = 0.7
取出30前有这些容器： [28, 30, 46]
取出30后有： [28, 46] v_p_cost=0.582320653069, v_rp = 0.3, v_m_cost = 0.390341212791, v_rm = 0.7
取出28前有这些容器： [28, 46]
取出28后有： [46] v_p_cost=0.39562350654, v_rp = 0.3, v_m_cost = 0.349259229066, v_rm = 0.7
取出46前有这些容器： [46]
取出46后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 5, v_p_cost = 0.820231294694, v_rp = 0.5, v_m_cost = 0.675475990182, v_rm = 0.7
取出13前有这些容器： [13, 17, 39]
取出13后有： [17, 39] v_p_cost=0.636752882349, v_rp = 0.5, v_m_cost = 0.475500416649, v_rm = 0.7
取出39前有这些容器： [17, 39]
取出39后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 1.15803248598, v_rp = 0.5, v_m_cost = 1.18150880971, v_rm = 0.7
取出29前有这些容器： [8, 11, 20, 29]
取出29后有： [8, 11, 20] v_p_cost=1.063526845, v_rp = 0.5, v_m_cost = 1.08863056602, v_rm = 0.7
取出11前有这些容器： [8, 11, 20]
取出11后有： [8, 20] v_p_cost=0.7443922144, v_rp = 0.5, v_m_cost = 0.799856228816, v_rm = 0.7
取出8前有这些容器： [8, 20]
取出8后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.5
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 0.52806661752, v_rp = 0.5, v_m_cost = 0.487996586539, v_rm = 1.0
取出15前有这些容器： [7, 15]
取出15后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 1.0
修改vm超载的情况 v_id = 18, v_p_cost = 0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.3
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 1.31899529575, v_rp = 0.5, v_m_cost = 1.22242825191, v_rm = 0.7
取出31前有这些容器： [23, 24, 31]
取出31后有： [23, 24] v_p_cost=0.92175886745, v_rp = 0.5, v_m_cost = 0.779886692948, v_rm = 0.7
取出23前有这些容器： [23, 24]
取出23后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.3
取出33前有这些容器： [33]
取出33后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.588380407104, v_rp = 0.5, v_m_cost = 0.345658045749, v_rm = 0.7
取出42前有这些容器： [1, 42]
取出42后有： [1] v_p_cost=0.38374105913, v_rp = 0.5, v_m_cost = 0.319779019605, v_rm = 0.7
修改vm超载的情况 v_id = 38, v_p_cost = 1.00808688378, v_rp = 1.0, v_m_cost = 0.96742465987, v_rm = 0.7
取出32前有这些容器： [19, 25, 32, 43]
取出32后有： [19, 25, 43] v_p_cost=0.885352810133, v_rp = 1.0, v_m_cost = 0.728972496283, v_rm = 0.7
取出25前有这些容器： [19, 25, 43]
取出25后有： [19, 43] v_p_cost=0.712903720718, v_rp = 1.0, v_m_cost = 0.662211907062, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.7, h_m_cost = 2.2
该物理机上放置的虚拟机为：  [0, 12, 22]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5, 0.7],mem尺寸[0.5, 0.7, 1.0]
0
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 1.0]
12
该物理机上的虚拟机对应cpu尺寸[0.7],mem尺寸[1.0]
22
修改hm过载  h_id = 3, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [8, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
修改hm过载  h_id = 7, h_p_cost = 1.3, h_m_cost = 1.9
该物理机上放置的虚拟机为：  [3, 10, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5, 0.5],mem尺寸[0.7, 0.5, 0.7]
3
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [36, 42]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.5]
42
修改hm过载  h_id = 14, h_p_cost = 1.0, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [33, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 1.0]
33
修改hm过载  h_id = 21, h_p_cost = 0.8, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 34, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [25, 38]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
25
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [34, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 47, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [16, 18]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.3]
16
修改hm过载  h_id = 48, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [5, 7]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
5
修改hm过载  h_id = 49, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [20, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
20
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.08819722202, v_rp = 0.5, v_m_cost = 1.19737221219, v_rm = 0.5
取出26前有这些容器： [5, 23, 26]
取出26后有： [5, 23] v_p_cost=0.877824874193, v_rp = 0.5, v_m_cost = 0.973799443546, v_rm = 0.5
取出5前有这些容器： [5, 23]
取出5后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.533502871605, v_rp = 0.3, v_m_cost = 0.53308111993, v_rm = 0.7
取出15前有这些容器： [1, 15]
取出15后有： [1] v_p_cost=0.38374105913, v_rp = 0.3, v_m_cost = 0.319779019605, v_rm = 0.7
取出1前有这些容器： [1]
取出1后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 11, v_p_cost = 0.856600625653, v_rp = 0.7, v_m_cost = 0.685039098119, v_rm = 0.5
取出19前有这些容器： [19, 24]
取出19后有： [24] v_p_cost=0.460918125956, v_rp = 0.7, v_m_cost = 0.306024644486, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.453283841054, v_rp = 0.3, v_m_cost = 0.551091146864, v_rm = 0.5
取出25前有这些容器： [9, 25]
取出25后有： [9] v_p_cost=0.280834751639, v_rp = 0.3, v_m_cost = 0.484330557644, v_rm = 0.5
修改vm超载的情况 v_id = 16, v_p_cost = 1.06930335087, v_rp = 0.5, v_m_cost = 0.896383273182, v_rm = 1.0
取出35前有这些容器： [12, 14, 35]
取出35后有： [12, 14] v_p_cost=0.975551114026, v_rp = 0.5, v_m_cost = 0.760505773007, v_rm = 1.0
取出14前有这些容器： [12, 14]
取出14后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 1.0
修改vm超载的情况 v_id = 29, v_p_cost = 0.331549405593, v_rp = 0.5, v_m_cost = 0.318108784296, v_rm = 0.3
取出27前有这些容器： [27, 43]
取出27后有： [43] v_p_cost=0.317221221021, v_rp = 0.5, v_m_cost = 0.28319745343, v_rm = 0.3
修改vm超载的情况 v_id = 34, v_p_cost = 0.481598929223, v_rp = 0.7, v_m_cost = 0.600587505074, v_rm = 0.5
取出10前有这些容器： [10, 38, 49]
取出10后有： [38, 49] v_p_cost=0.403461490808, v_rp = 0.7, v_m_cost = 0.46562525884, v_rm = 0.5
修改vm超载的情况 v_id = 44, v_p_cost = 0.905885994095, v_rp = 0.7, v_m_cost = 0.629976511311, v_rm = 0.5
取出17前有这些容器： [0, 17]
取出17后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.5
修改vm超载的情况 v_id = 48, v_p_cost = 1.14663648338, v_rp = 1.0, v_m_cost = 1.06903781827, v_rm = 0.7
取出33前有这些容器： [18, 33, 47]
取出33后有： [18, 47] v_p_cost=0.849243517901, v_rp = 1.0, v_m_cost = 0.760512698707, v_rm = 0.7
取出18前有这些容器： [18, 47]
取出18后有： [47] v_p_cost=0.480976430345, v_rp = 1.0, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 3, h_p_cost = 2.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [32, 38]
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 0.7]
32
修改hm过载  h_id = 9, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [23, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 24, h_p_cost = 1.4, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [11, 41]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.5, 0.5]
11
修改hm过载  h_id = 33, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 3]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.5, 0.7]
3
修改hm过载  h_id = 34, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [29, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
29
修改hm过载  h_id = 39, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 33]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 41, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 10]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.5]
10
修改hm过载  h_id = 46, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [15, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
15
修改hm过载  h_id = 47, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [25, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 48, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 8]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
进入mbbode_rank
[6, 15, 9, 8, 2] 4
上代结果： 14417.0799408 1.57029460402 783480.158484 1430.0
本代结果替代后： 14407.1765115 1.17982857704 559813.724369 1560.0
执行全局精英解替换： 14407.1765115 1.17982857704 559813.724369 1560.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
in this chrom [[30, 15], [38, 27], [4, 16], [13, 9], [10, 38], [47, 0], [29, 24], [39, 43], [19, 35], [34, 23], [47, 0], [12, 28], [45, 18], [4, 16], [41, 2], [19, 35], [24, 1], [7, 44], [16, 37], [49, 3], [6, 36], [22, 31], [29, 46], [37, 22], [46, 10], [40, 17], [8, 13], [44, 4], [32, 47], [1, 34], [12, 28], [35, 21], [1, 34], [7, 44], [25, 24], [15, 38], [49, 3], [14, 26], [10, 38], [48, 7], [32, 47], [11, 17], [13, 9], [44, 4], [48, 7], [8, 13], [28, 40], [36, 49], [43, 39], [1, 34]], a vm has been hosted on different hm, totally wrong!! 
进入fix_effective
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 29, v_p_cost = 0.41545604103, v_rp = 0.5, v_m_cost = 0.491933624667, v_rm = 0.3
取出6前有这些容器： [6, 22]
取出6后有： [22] v_p_cost=0.331264766544, v_rp = 0.5, v_m_cost = 0.276280683068, v_rm = 0.3
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.32887410159, v_rp = 0.3, v_m_cost = 0.326954168131, v_rm = 0.7
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 5, v_p_cost = 1.06204759441, v_rp = 0.5, v_m_cost = 1.11170783946, v_rm = 0.7
取出2前有这些容器： [2, 14, 47]
取出2后有： [14, 47] v_p_cost=0.958904710504, v_rp = 0.5, v_m_cost = 0.923990854526, v_rm = 0.7
取出14前有这些容器： [14, 47]
取出14后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.497262795029, v_rp = 0.5, v_m_cost = 0.589122026014, v_rm = 0.5
取出10前有这些容器： [10, 33, 49]
取出10后有： [33, 49] v_p_cost=0.419125356614, v_rp = 0.5, v_m_cost = 0.454159779779, v_rm = 0.5
修改vm超载的情况 v_id = 12, v_p_cost = 0.71445764932, v_rp = 0.5, v_m_cost = 0.725739012389, v_rm = 0.7
取出43前有这些容器： [31, 43]
取出43后有： [31] v_p_cost=0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.494424946874, v_rp = 0.5, v_m_cost = 0.358315791191, v_rm = 0.3
取出44前有这些容器： [7, 44]
取出44后有： [7] v_p_cost=0.378304805046, v_rp = 0.5, v_m_cost = 0.274694486214, v_rm = 0.3
修改vm超载的情况 v_id = 33, v_p_cost = 0.716900135783, v_rp = 0.5, v_m_cost = 0.768815639044, v_rm = 0.7
取出6前有这些容器： [6, 17, 29, 35]
取出6后有： [17, 29, 35] v_p_cost=0.632708861297, v_rp = 0.5, v_m_cost = 0.553162697445, v_rm = 0.7
取出35前有这些容器： [17, 29, 35]
取出35后有： [17, 29] v_p_cost=0.538956624455, v_rp = 0.5, v_m_cost = 0.417285197269, v_rm = 0.7
取出29前有这些容器： [17, 29]
取出29后有： [17] v_p_cost=0.44445098347, v_rp = 0.5, v_m_cost = 0.324406953571, v_rm = 0.7
修改hm过载  h_id = 25, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [5, 27]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
5
修改hm过载  h_id = 29, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [9, 10]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 32, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 44]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
33
修改hm过载  h_id = 34, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [26, 39]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.3]
26
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 39, h_p_cost = 0.8, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [40, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.5, 1.0]
40
修改hm过载  h_id = 41, h_p_cost = 0.8, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [3, 25]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[0.7, 0.7]
3
修改hm过载  h_id = 47, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 48, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [15, 24]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.5]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 2, v_p_cost = 1.2174417347, v_rp = 1.0, v_m_cost = 1.19265734793, v_rm = 1.0
取出29前有这些容器： [1, 5, 15, 25, 29]
取出29后有： [1, 5, 15, 25] v_p_cost=1.12293609372, v_rp = 1.0, v_m_cost = 1.09977910423, v_rm = 1.0
取出15前有这些容器： [1, 5, 15, 25]
取出15后有： [1, 5, 25] v_p_cost=0.973174281245, v_rp = 1.0, v_m_cost = 0.886477003909, v_rm = 1.0
修改vm超载的情况 v_id = 17, v_p_cost = 0.875777521665, v_rp = 0.7, v_m_cost = 0.840474357248, v_rm = 0.7
取出44前有这些容器： [14, 38, 44]
取出44后有： [14, 38] v_p_cost=0.759657379836, v_rp = 0.7, v_m_cost = 0.756853052271, v_rm = 0.7
取出38前有这些容器： [14, 38]
取出38后有： [14] v_p_cost=0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.7
修改vm超载的情况 v_id = 27, v_p_cost = 0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.3
取出16前有这些容器： [16]
取出16后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.420969578467, v_rp = 0.3, v_m_cost = 0.310178448149, v_rm = 0.5
取出41前有这些容器： [41]
取出41后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.546210598883, v_rp = 0.7, v_m_cost = 0.624914739598, v_rm = 0.5
取出6前有这些容器： [6, 18, 35]
取出6后有： [18, 35] v_p_cost=0.462019324397, v_rp = 0.7, v_m_cost = 0.409261797998, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 0.749661786944, v_rp = 0.7, v_m_cost = 0.670017187317, v_rm = 0.7
取出49前有这些容器： [13, 17, 49]
取出49后有： [13, 17] v_p_cost=0.627929395814, v_rp = 0.7, v_m_cost = 0.524382527105, v_rm = 0.7
修改vm超载的情况 v_id = 48, v_p_cost = 1.27576218084, v_rp = 1.0, v_m_cost = 0.91286541728, v_rm = 0.7
取出43前有这些容器： [12, 24, 43]
取出43后有： [12, 24] v_p_cost=0.958540959823, v_rp = 1.0, v_m_cost = 0.629667963851, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [22, 46]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
22
修改hm过载  h_id = 36, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [12, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 37, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [26, 36]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
26
修改hm过载  h_id = 38, h_p_cost = 1.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 17]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[1.0, 0.7]
1
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
20
修改hm过载  h_id = 42, h_p_cost = 1.5, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [21, 32]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.3, 0.7]
21
修改hm过载  h_id = 44, h_p_cost = 2.7, h_m_cost = 3.0
该物理机上放置的虚拟机为：  [2, 5, 27, 45]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5, 0.7, 0.5],mem尺寸[1.0, 0.7, 0.3, 1.0]
5
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7, 0.5],mem尺寸[1.0, 0.3, 1.0]
45
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 0.3]
27
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
2
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 0.827463567768, v_rp = 0.5, v_m_cost = 0.723264383819, v_rm = 0.5
取出31前有这些容器： [21, 31]
取出31后有： [21] v_p_cost=0.430227139469, v_rp = 0.5, v_m_cost = 0.28072282486, v_rm = 0.5
修改vm超载的情况 v_id = 3, v_p_cost = 0.460918125956, v_rp = 0.3, v_m_cost = 0.306024644486, v_rm = 0.7
取出24前有这些容器： [24]
取出24后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 1.0
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 5, v_p_cost = 0.505160852953, v_rp = 0.5, v_m_cost = 0.525831389748, v_rm = 0.7
取出6前有这些容器： [6, 41]
取出6后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 15, v_p_cost = 0.391391198077, v_rp = 0.3, v_m_cost = 0.441099191848, v_rm = 0.5
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 28, v_p_cost = 0.590628834201, v_rp = 1.0, v_m_cost = 0.647711097738, v_rm = 0.5
取出49前有这些容器： [11, 15, 49]
取出49后有： [11, 15] v_p_cost=0.468896443071, v_rp = 1.0, v_m_cost = 0.502076437526, v_rm = 0.5
取出15前有这些容器： [11, 15]
取出15后有： [11] v_p_cost=0.319134630596, v_rp = 1.0, v_m_cost = 0.2887743372, v_rm = 0.5
修改vm超载的情况 v_id = 37, v_p_cost = 0.751571154577, v_rp = 0.5, v_m_cost = 0.695276307416, v_rm = 0.7
取出25前有这些容器： [25, 33, 38]
取出25后有： [33, 38] v_p_cost=0.579122065162, v_rp = 0.5, v_m_cost = 0.628515718196, v_rm = 0.7
取出38前有这些容器： [33, 38]
取出38后有： [33] v_p_cost=0.297392965484, v_rp = 0.5, v_m_cost = 0.308525119567, v_rm = 0.7
修改vm超载的情况 v_id = 39, v_p_cost = 0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.3
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.431312317271, v_rp = 0.3, v_m_cost = 0.534848725951, v_rm = 0.5
取出27前有这些容器： [5, 27]
取出27后有： [5] v_p_cost=0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 0.5
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 4, h_p_cost = 2.7, h_m_cost = 2.9
该物理机上放置的虚拟机为：  [17, 24, 37, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.5, 0.5],mem尺寸[0.7, 0.5, 0.7, 1.0]
37
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.5],mem尺寸[0.7, 0.5, 1.0]
45
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0],mem尺寸[0.7, 0.5]
17
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[0.5]
24
修改hm过载  h_id = 7, h_p_cost = 0.6, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [3, 15]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3],mem尺寸[0.7, 0.5]
3
修改hm过载  h_id = 8, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [11, 26]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
26
修改hm过载  h_id = 9, h_p_cost = 1.0, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [4, 36]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.5]
4
修改hm过载  h_id = 27, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 16]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 30, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
40
修改hm过载  h_id = 34, h_p_cost = 2.4, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [6, 38, 39]
该物理机上的虚拟机对应cpu尺寸[0.7, 1.0, 0.7],mem尺寸[0.7, 0.7, 0.3]
6
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.7, 0.3]
39
修改hm过载  h_id = 36, h_p_cost = 1.2, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [12, 30]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.7]
12
修改hm过载  h_id = 44, h_p_cost = 1.7, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 41]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[0.5, 0.5]
41
修改hm过载  h_id = 46, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 34]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.7, 0.5]
5
修改hm过载  h_id = 48, h_p_cost = 1.5, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [7, 10]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 0.5]
10
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 0, v_p_cost = 1.15534078533, v_rp = 0.5, v_m_cost = 1.0934979433, v_rm = 0.5
取出18前有这些容器： [18, 19, 20]
取出18后有： [19, 20] v_p_cost=0.787073697774, v_rp = 0.5, v_m_cost = 0.820113645481, v_rm = 0.5
取出20前有这些容器： [19, 20]
取出20后有： [19] v_p_cost=0.395682499698, v_rp = 0.5, v_m_cost = 0.379014453633, v_rm = 0.5
修改vm超载的情况 v_id = 1, v_p_cost = 1.07988928941, v_rp = 0.7, v_m_cost = 0.984296949102, v_rm = 1.0
取出22前有这些容器： [8, 22, 46]
取出22后有： [8, 46] v_p_cost=0.748624522863, v_rp = 0.7, v_m_cost = 0.708016266034, v_rm = 1.0
取出8前有这些容器： [8, 46]
取出8后有： [46] v_p_cost=0.39562350654, v_rp = 0.7, v_m_cost = 0.349259229066, v_rm = 1.0
修改vm超载的情况 v_id = 3, v_p_cost = 0.861905915706, v_rp = 0.3, v_m_cost = 1.10890999622, v_rm = 0.7
取出2前有这些容器： [2, 9, 14]
取出2后有： [9, 14] v_p_cost=0.758763031798, v_rp = 0.3, v_m_cost = 0.921193011287, v_rm = 0.7
取出9前有这些容器： [9, 14]
取出9后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.7
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=-1.11022302463e-16, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 10, v_p_cost = 0.451608175233, v_rp = 0.5, v_m_cost = 0.565406331718, v_rm = 0.5
取出32前有这些容器： [32, 34]
取出32后有： [34] v_p_cost=0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.3
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 23, v_p_cost = 0.771381114561, v_rp = 0.7, v_m_cost = 0.929073766267, v_rm = 0.5
取出30前有这些容器： [30, 37, 43]
取出30后有： [37, 43] v_p_cost=0.628395616439, v_rp = 0.7, v_m_cost = 0.733764209418, v_rm = 0.5
取出37前有这些容器： [37, 43]
取出37后有： [43] v_p_cost=0.317221221021, v_rp = 0.7, v_m_cost = 0.28319745343, v_rm = 0.5
修改vm超载的情况 v_id = 33, v_p_cost = 0.603681279228, v_rp = 0.5, v_m_cost = 0.54101937881, v_rm = 0.7
取出28前有这些容器： [5, 28]
取出28后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 40, v_p_cost = 0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.5
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 41, v_p_cost = 0.934145847833, v_rp = 0.7, v_m_cost = 0.784025536216, v_rm = 0.5
取出39前有这些容器： [17, 33, 39]
取出39后有： [17, 33] v_p_cost=0.741843948953, v_rp = 0.7, v_m_cost = 0.632932073139, v_rm = 0.5
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.5
修改vm超载的情况 v_id = 46, v_p_cost = 0.77997537209, v_rp = 0.7, v_m_cost = 0.762636385662, v_rm = 0.7
取出11前有这些容器： [11, 23]
取出11后有： [23] v_p_cost=0.460840741494, v_rp = 0.7, v_m_cost = 0.473862048462, v_rm = 0.7
修改hm过载  h_id = 1, h_p_cost = 1.8, h_m_cost = 2.7
该物理机上放置的虚拟机为：  [3, 13, 46, 47]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.3, 0.7, 0.5],mem尺寸[0.7, 0.3, 0.7, 1.0]
3
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7, 0.5],mem尺寸[0.3, 0.7, 1.0]
13
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
修改hm过载  h_id = 11, h_p_cost = 0.8, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [5, 15]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.3],mem尺寸[0.7, 0.5]
15
修改hm过载  h_id = 13, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [10, 11]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
10
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [31, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.5]
31
修改hm过载  h_id = 23, h_p_cost = 1.2, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [39, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 1.0]
45
修改hm过载  h_id = 30, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [28, 40]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.3],mem尺寸[0.5, 0.5]
40
修改hm过载  h_id = 33, h_p_cost = 1.5, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [20, 43]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 0.7]
20
修改hm过载  h_id = 38, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 33]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
33
修改hm过载  h_id = 48, h_p_cost = 1.0, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [4, 22]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 1.0]
4
进入mbbode_rank
[6, 12, 9, 5, 8] 3
上代结果： 14407.1765115 1.17982857704 559813.724369 1560.0
进入mbbode_migration
进入mbbode_mutation
进入mbbode_cost
进入check_effective
find a error: VM or hm has overhold [[44, 15], [12, 6], [5, 11], [8, 48], [5, 11], [4, 35], [36, 44], [31, 31], [8, 48], [15, 12], [45, 23], [46, 1], [16, 20], [19, 22], [3, 32], [40, 12], [23, 9], [6, 17], [47, 46], [43, 34], [7, 41], [37, 28], [46, 1], [0, 33], [11, 7], [36, 44], [25, 47], [45, 23], [33, 39], [40, 12], [19, 22], [49, 49], [45, 23], [41, 24], [10, 16], [32, 19], [6, 17], [33, 39], [34, 38], [41, 24], [36, 44], [14, 0], [19, 22], [29, 32], [32, 19], [6, 17], [42, 21], [48, 2], [38, 3], [34, 38]] 3 {0: 33, 3: 32, 4: 35, 5: 11, 6: 17, 7: 41, 8: 48, 10: 16, 11: 7, 12: 6, 14: 0, 15: 12, 16: 20, 19: 22, 23: 9, 25: 47, 29: 32, 31: 31, 32: 19, 33: 39, 34: 38, 36: 44, 37: 28, 38: 3, 40: 12, 41: 24, 42: 21, 43: 34, 44: 15, 45: 23, 46: 1, 47: 46, 48: 2, 49: 49} 

进入fix_effective
修改vm超载的情况 v_id = 3, v_p_cost = 0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.7
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.416984132699, v_rp = 0.3, v_m_cost = 0.499937395085, v_rm = 1.0
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改hm过载  h_id = 35, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 27]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 48, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [1, 8]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[1.0, 0.7]
8
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.524732780454, v_rp = 0.3, v_m_cost = 0.373601068558, v_rm = 0.7
取出29前有这些容器： [21, 29]
取出29后有： [21] v_p_cost=0.430227139469, v_rp = 0.3, v_m_cost = 0.28072282486, v_rm = 0.7
取出21前有这些容器： [21]
取出21后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.7
修改vm超载的情况 v_id = 8, v_p_cost = 0.54503201598, v_rp = 0.5, v_m_cost = 0.689514990061, v_rm = 0.7
取出6前有这些容器： [6, 23]
取出6后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 9, v_p_cost = 0.527093599691, v_rp = 1.0, v_m_cost = 0.502696258582, v_rm = 0.5
取出35前有这些容器： [35, 43, 44]
取出35后有： [43, 44] v_p_cost=0.433341362849, v_rp = 1.0, v_m_cost = 0.366818758407, v_rm = 0.5
修改vm超载的情况 v_id = 15, v_p_cost = 0.833048283027, v_rp = 0.3, v_m_cost = 0.718515641707, v_rm = 0.5
取出3前有这些容器： [3, 7, 31]
取出3后有： [7, 31] v_p_cost=0.775541233345, v_rp = 0.3, v_m_cost = 0.717236045173, v_rm = 0.5
取出7前有这些容器： [7, 31]
取出7后有： [31] v_p_cost=0.397236428299, v_rp = 0.3, v_m_cost = 0.442541558959, v_rm = 0.5
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -1.11022302463e-16, v_rm = 0.5
修改vm超载的情况 v_id = 18, v_p_cost = 0.477928280159, v_rp = 0.7, v_m_cost = 0.436862453643, v_rm = 0.3
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 0.812360776544, v_rp = 0.5, v_m_cost = 0.751277639996, v_rm = 0.7
取出20前有这些容器： [20, 41]
取出20后有： [41] v_p_cost=0.420969578467, v_rp = 0.5, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 26, v_p_cost = 0.892963337222, v_rp = 0.5, v_m_cost = 0.665521377556, v_rm = 0.7
取出46前有这些容器： [16, 46]
取出46后有： [16] v_p_cost=0.497339830683, v_rp = 0.5, v_m_cost = 0.31626214849, v_rm = 0.7
修改vm超载的情况 v_id = 41, v_p_cost = 0.721268103879, v_rp = 0.7, v_m_cost = 0.632141334791, v_rm = 0.5
取出8前有这些容器： [8, 18]
取出8后有： [18] v_p_cost=0.368267087556, v_rp = 0.7, v_m_cost = 0.273384297823, v_rm = 0.5
修改hm过载  h_id = 8, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [33, 42]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.5]
33
修改hm过载  h_id = 17, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [0, 14]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 20, h_p_cost = 1.2, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [18, 20]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.7]
20
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [16, 41]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[1.0, 0.5]
16
修改hm过载  h_id = 31, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [29, 45]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.3, 1.0]
29
修改hm过载  h_id = 41, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 25]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 45, h_p_cost = 1.3, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [3, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.7, 1.0]
3
修改hm过载  h_id = 47, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [30, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
31
修改hm过载  h_id = 49, h_p_cost = 1.3, h_m_cost = 1.0
该物理机上放置的虚拟机为：  [15, 49]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.5, 0.5]
15
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 3, v_p_cost = 0.48944263578, v_rp = 0.3, v_m_cost = 0.576969295838, v_rm = 0.7
取出15前有这些容器： [15, 48]
取出15后有： [48] v_p_cost=0.339680823305, v_rp = 0.3, v_m_cost = 0.363667195512, v_rm = 0.7
取出48前有这些容器： [48]
取出48后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 5.55111512313e-17, v_rm = 0.7
修改vm超载的情况 v_id = 4, v_p_cost = 0.391391198077, v_rp = 0.3, v_m_cost = 0.441099191848, v_rm = 1.0
取出20前有这些容器： [20]
取出20后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 12, v_p_cost = 0.748646117175, v_rp = 0.5, v_m_cost = 0.902756916017, v_rm = 0.7
取出6前有这些容器： [6, 13, 47]
取出6后有： [13, 47] v_p_cost=0.664454842689, v_rp = 0.5, v_m_cost = 0.687103974418, v_rm = 0.7
取出13前有这些容器： [13, 47]
取出13后有： [47] v_p_cost=0.480976430345, v_rp = 0.5, v_m_cost = 0.487128400884, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.647537888023, v_rp = 0.3, v_m_cost = 0.514944032187, v_rm = 0.3
取出28前有这些容器： [23, 28]
取出28后有： [23] v_p_cost=0.460840741494, v_rp = 0.3, v_m_cost = 0.473862048462, v_rm = 0.3
取出23前有这些容器： [23]
取出23后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 27, v_p_cost = 0.814436026948, v_rp = 0.7, v_m_cost = 0.664326594708, v_rm = 0.3
取出8前有这些容器： [0, 8]
取出8后有： [0] v_p_cost=0.461435010625, v_rp = 0.7, v_m_cost = 0.305569557739, v_rm = 0.3
取出0前有这些容器： [0]
取出0后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 40, v_p_cost = 0.54948885342, v_rp = 0.3, v_m_cost = 0.519808268338, v_rm = 0.5
取出40前有这些容器： [26, 40, 43]
取出40后有： [26, 43] v_p_cost=0.527593568848, v_rp = 0.3, v_m_cost = 0.50677022207, v_rm = 0.5
取出26前有这些容器： [26, 43]
取出26后有： [43] v_p_cost=0.317221221021, v_rp = 0.3, v_m_cost = 0.28319745343, v_rm = 0.5
取出43前有这些容器： [43]
取出43后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.5
修改vm超载的情况 v_id = 43, v_p_cost = 0.869873771205, v_rp = 1.0, v_m_cost = 0.820849468984, v_rm = 0.7
取出30前有这些容器： [22, 30, 46]
取出30后有： [22, 46] v_p_cost=0.726888273083, v_rp = 1.0, v_m_cost = 0.625539912134, v_rm = 0.7
修改vm超载的情况 v_id = 46, v_p_cost = 0.741843948953, v_rp = 0.7, v_m_cost = 0.632932073139, v_rm = 0.7
取出33前有这些容器： [17, 33]
取出33后有： [17] v_p_cost=0.44445098347, v_rp = 0.7, v_m_cost = 0.324406953571, v_rm = 0.7
修改hm过载  h_id = 7, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 10]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 0.5]
10
修改hm过载  h_id = 12, h_p_cost = 1.0, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [4, 27]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.7],mem尺寸[1.0, 0.3]
4
修改hm过载  h_id = 16, h_p_cost = 1.3, h_m_cost = 1.3
该物理机上放置的虚拟机为：  [13, 35]
该物理机上的虚拟机对应cpu尺寸[0.3, 1.0],mem尺寸[0.3, 1.0]
13
修改hm过载  h_id = 25, h_p_cost = 1.7, h_m_cost = 2.0
该物理机上放置的虚拟机为：  [2, 22]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.7],mem尺寸[1.0, 1.0]
22
修改hm过载  h_id = 27, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [7, 16]
该物理机上的虚拟机对应cpu尺寸[1.0, 0.5],mem尺寸[0.7, 1.0]
16
修改hm过载  h_id = 33, h_p_cost = 1.2, h_m_cost = 0.8
该物理机上放置的虚拟机为：  [18, 31]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.3, 0.5]
31
修改hm过载  h_id = 36, h_p_cost = 1.0, h_m_cost = 1.4
该物理机上放置的虚拟机为：  [8, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.7, 0.7]
8
修改hm过载  h_id = 38, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [0, 17, 40]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7, 0.3],mem尺寸[0.5, 0.7, 0.5]
40
该物理机上的虚拟机对应cpu尺寸[0.5, 0.7],mem尺寸[0.5, 0.7]
0
修改hm过载  h_id = 49, h_p_cost = 1.2, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [14, 47]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.7, 1.0]
47
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 4, v_p_cost = 0.480976430345, v_rp = 0.3, v_m_cost = 0.487128400884, v_rm = 1.0
取出47前有这些容器： [47]
取出47后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 1.0
修改vm超载的情况 v_id = 10, v_p_cost = 0.479814781026, v_rp = 0.5, v_m_cost = 0.564912170665, v_rm = 0.5
取出6前有这些容器： [6, 46]
取出6后有： [46] v_p_cost=0.39562350654, v_rp = 0.5, v_m_cost = 0.349259229066, v_rm = 0.5
修改vm超载的情况 v_id = 11, v_p_cost = 0.80890136916, v_rp = 0.7, v_m_cost = 0.972327144183, v_rm = 0.5
取出15前有这些容器： [7, 9, 15]
取出15后有： [7, 9] v_p_cost=0.659139556685, v_rp = 0.7, v_m_cost = 0.759025043858, v_rm = 0.5
取出9前有这些容器： [7, 9]
取出9后有： [7] v_p_cost=0.378304805046, v_rp = 0.7, v_m_cost = 0.274694486214, v_rm = 0.5
修改vm超载的情况 v_id = 13, v_p_cost = 0.311174395419, v_rp = 0.3, v_m_cost = 0.450566755988, v_rm = 0.3
取出37前有这些容器： [37]
取出37后有： [] v_p_cost=0.0, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 15, v_p_cost = 0.8281920426, v_rp = 0.3, v_m_cost = 0.644185973176, v_rm = 0.5
取出1前有这些容器： [1, 17]
取出1后有： [17] v_p_cost=0.44445098347, v_rp = 0.3, v_m_cost = 0.324406953571, v_rm = 0.5
取出17前有这些容器： [17]
取出17后有： [] v_p_cost=-5.55111512313e-17, v_rp = 0.3, v_m_cost = 0.0, v_rm = 0.5
修改vm超载的情况 v_id = 21, v_p_cost = 0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.3
取出5前有这些容器： [5]
取出5后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 29, v_p_cost = 0.32887410159, v_rp = 0.5, v_m_cost = 0.326954168131, v_rm = 0.3
取出34前有这些容器： [34]
取出34后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 37, v_p_cost = 0.614614186505, v_rp = 0.5, v_m_cost = 0.591722572997, v_rm = 0.7
取出33前有这些容器： [33, 43]
取出33后有： [43] v_p_cost=0.317221221021, v_rp = 0.5, v_m_cost = 0.28319745343, v_rm = 0.7
修改vm超载的情况 v_id = 42, v_p_cost = 0.817609103464, v_rp = 0.5, v_m_cost = 0.800529649155, v_rm = 0.5
取出48前有这些容器： [14, 48]
取出48后有： [14] v_p_cost=0.477928280159, v_rp = 0.5, v_m_cost = 0.436862453643, v_rm = 0.5
修改vm超载的情况 v_id = 45, v_p_cost = 0.673120297755, v_rp = 0.5, v_m_cost = 0.761089790476, v_rm = 1.0
取出38前有这些容器： [20, 38]
取出38后有： [20] v_p_cost=0.391391198077, v_rp = 0.5, v_m_cost = 0.441099191848, v_rm = 1.0
修改vm超载的情况 v_id = 46, v_p_cost = 0.958774841308, v_rp = 0.7, v_m_cost = 0.621831706229, v_rm = 0.7
取出0前有这些容器： [0, 16]
取出0后有： [16] v_p_cost=0.497339830683, v_rp = 0.7, v_m_cost = 0.31626214849, v_rm = 0.7
修改hm过载  h_id = 0, h_p_cost = 1.0, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [10, 12]
该物理机上的虚拟机对应cpu尺寸[0.5, 0.5],mem尺寸[0.5, 0.7]
10
修改hm过载  h_id = 18, h_p_cost = 0.8, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [4, 26]
该物理机上的虚拟机对应cpu尺寸[0.3, 0.5],mem尺寸[1.0, 0.7]
4
修改hm过载  h_id = 21, h_p_cost = 1.2, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [34, 37]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 0.7]
37
修改hm过载  h_id = 39, h_p_cost = 1.2, h_m_cost = 1.5
该物理机上放置的虚拟机为：  [36, 45]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.5],mem尺寸[0.5, 1.0]
45
修改hm过载  h_id = 45, h_p_cost = 1.5, h_m_cost = 1.7
该物理机上放置的虚拟机为：  [25, 35]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0],mem尺寸[0.7, 1.0]
25
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
ops, a vm has been hosted on different hm, totally wrong!! fixing
修改vm超载的情况 v_id = 5, v_p_cost = 0.561347433898, v_rp = 0.5, v_m_cost = 0.576459215388, v_rm = 0.7
取出4前有这些容器： [4, 23]
取出4后有： [23] v_p_cost=0.460840741494, v_rp = 0.5, v_m_cost = 0.473862048462, v_rm = 0.7
修改vm超载的情况 v_id = 6, v_p_cost = 0.909401981732, v_rp = 0.7, v_m_cost = 0.854164368167, v_rm = 0.7
取出10前有这些容器： [10, 11, 25, 48]
取出10后有： [11, 25, 48] v_p_cost=0.831264543316, v_rp = 0.7, v_m_cost = 0.719202121933, v_rm = 0.7
取出25前有这些容器： [11, 25, 48]
取出25后有： [11, 48] v_p_cost=0.658815453901, v_rp = 0.7, v_m_cost = 0.652441532712, v_rm = 0.7
修改vm超载的情况 v_id = 12, v_p_cost = 0.881363892997, v_rp = 0.5, v_m_cost = 0.643422338969, v_rm = 0.7
取出1前有这些容器： [1, 12]
取出1后有： [12] v_p_cost=0.497622833867, v_rp = 0.5, v_m_cost = 0.323643319364, v_rm = 0.7
修改vm超载的情况 v_id = 13, v_p_cost = 0.751805345523, v_rp = 0.3, v_m_cost = 0.49931715203, v_rm = 0.3
取出45前有这些容器： [14, 28, 45]
取出45后有： [14, 28] v_p_cost=0.664625426688, v_rp = 0.3, v_m_cost = 0.477944437368, v_rm = 0.3
取出28前有这些容器： [14, 28]
取出28后有： [14] v_p_cost=0.477928280159, v_rp = 0.3, v_m_cost = 0.436862453643, v_rm = 0.3
取出14前有这些容器： [14]
取出14后有： [] v_p_cost=5.55111512313e-17, v_rp = 0.3, v_m_cost = -5.55111512313e-17, v_rm = 0.3
修改vm超载的情况 v_id = 20, v_p_cost = 0.665557473929, v_rp = 0.5, v_m_cost = 0.331903670631, v_rm = 0.7
取出42前有这些容器： [24, 42]
取出42后有： [24] v_p_cost=0.460918125956, v_rp = 0.5, v_m_cost = 0.306024644486, v_rm = 0.7
修改vm超载的情况 v_id = 21, v_p_cost = 0.397236428299, v_rp = 0.5, v_m_cost = 0.442541558959, v_rm = 0.3
取出31前有这些容器： [31]
取出31后有： [] v_p_cost=0.0, v_rp = 0.5, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 30, v_p_cost = 0.799274383513, v_rp = 0.7, v_m_cost = 0.584872934362, v_rm = 0.7
取出7前有这些容器： [7, 41]
取出7后有： [41] v_p_cost=0.420969578467, v_rp = 0.7, v_m_cost = 0.310178448149, v_rm = 0.7
修改vm超载的情况 v_id = 33, v_p_cost = 0.731018422709, v_rp = 0.5, v_m_cost = 0.796665518374, v_rm = 0.7
取出49前有这些容器： [5, 39, 49]
取出49后有： [5, 39] v_p_cost=0.609286031579, v_rp = 0.5, v_m_cost = 0.651030858162, v_rm = 0.7
取出39前有这些容器： [5, 39]
取出39后有： [5] v_p_cost=0.416984132699, v_rp = 0.5, v_m_cost = 0.499937395085, v_rm = 0.7
修改vm超载的情况 v_id = 34, v_p_cost = 0.521546743246, v_rp = 0.7, v_m_cost = 0.674139524629, v_rm = 0.5
取出26前有这些容器： [26, 37]
取出26后有： [37] v_p_cost=0.311174395419, v_rp = 0.7, v_m_cost = 0.450566755988, v_rm = 0.5
修改vm超载的情况 v_id = 39, v_p_cost = 0.395682499698, v_rp = 0.7, v_m_cost = 0.379014453633, v_rm = 0.3
取出19前有这些容器： [19]
取出19后有： [] v_p_cost=0.0, v_rp = 0.7, v_m_cost = 0.0, v_rm = 0.3
修改vm超载的情况 v_id = 46, v_p_cost = 1.32105092035, v_rp = 0.7, v_m_cost = 1.16079458352, v_rm = 0.7
取出46前有这些容器： [17, 46, 47]
取出46后有： [17, 47] v_p_cost=0.925427413815, v_rp = 0.7, v_m_cost = 0.811535354455, v_rm = 0.7
取出17前有这些容器： [17, 47]
取出17后有： [47] v_p_cost=0.480976430345, v_rp = 0.7, v_m_cost = 0.487128400884, v_rm = 0.7
修改hm过载  h_id = 1, h_p_cost = 1.4, h_m_cost = 1.2
该物理机上放置的虚拟机为：  [6, 34]
该物理机上的虚拟机对应cpu尺寸[0.7, 0.7],mem尺寸[0.7, 0.5]
6
修改hm过载  h_id = 3, h_p_cost = 3.0, h_m_cost = 2.9
该物理机上放置的虚拟机为：  [0, 7, 19, 26]
该物理机上的虚拟机对应cpu尺寸[0.5, 1.0, 1.0, 0.5],mem尺寸[0.5, 0.7, 1.0, 0.7]
0
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0, 0.5],mem尺寸[0.7, 1.0, 0.7]
26
该物理机上的虚拟机对应cpu尺寸[1.0, 1.0],mem尺寸[0.7, 1.0]
7
该物理机上的虚拟机对应cpu尺寸[1.0],mem尺寸[1.0]
19
该物理机上的虚拟机对应cpu尺寸[],mem尺寸[]
hm代价统计有异常 3 {0: 43, 1: 35, 3: 29, 4: 13, 5: 11, 6: 4, 7: 36, 8: 24, 10: 10, 12: 6, 13: 13, 15: 28, 17: 12, 19: 3, 20: 0, 21: 28, 22: 2, 23: 15, 24: 39, 25: 41, 26: 26, 28: 15, 29: 41, 30: 25, 31: 12, 32: 19, 33: 24, 34: 1, 35: 45, 39: 46, 40: 29, 43: 16, 44: 6, 45: 39, 46: 29, 47: 44, 49: 19} {0: 3, 1: 35, 3: 29, 5: 11, 6: 1, 7: 3, 10: 10, 12: 6, 13: 13, 19: 3, 20: 0, 21: 28, 22: 2, 23: 15, 25: 41, 26: 3, 28: 15, 29: 41, 30: 25, 31: 12, 32: 19, 33: 24, 34: 1, 35: 45, 39: 46, 40: 29, 43: 16, 44: 6, 45: 39, 46: 29, 47: 44, 49: 19} {0: 3, 1: 35, 3: 29, 4: 13, 5: 11, 6: 1, 7: 3, 8: 24, 10: 10, 12: 6, 13: 13, 15: 28, 17: 12, 19: 3, 20: 0, 21: 28, 22: 2, 23: 15, 24: 39, 25: 41, 26: 3, 28: 15, 29: 41, 30: 25, 31: 12, 32: 19, 33: 24, 34: 1, 35: 45, 39: 46, 40: 29, 43: 16, 44: 6, 45: 39, 46: 29, 47: 44, 49: 19}
