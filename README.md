# MBBO by Mao Rongrong

---------------

[TOC]

Abstract:
>This project is developed on the basis of MBBO algorithm and provide a visualization for the process and status of VM migration.

Multi-objective biogeography-based optimization algorithm hybrid with differential evolution for VM Consolidation Problem (**MBBO**).

>BBO [wiki](https://en.wikipedia.org/wiki/Biogeography-based_optimization">) is an evolutionary algorithm (EA) that optimizes a function by stochastically and iteratively improving candidate solutions with regard to a given measure of quality, or fitness function. BBO belongs to the class of metaheuristics since it includes many variations, and since it does not make any assumptions about the problem and can therefore be applied to a wide class of problems.
>
>BBO is typically used to optimize multidimensional real-valued functions, but it does not use the gradient of the function, which means that it does not require the function to be differentiable as required by classic optimization methods such as gradient descent and quasi-newton methods. BBO can therefore be used on discontinuous functions.
>
>BBO optimizes a problem by maintaining a population of candidate solutions, and creating new candidate solutions by combining existing ones according to a simple formula. In this way the objective function is treated as a black box that merely provides a measure of quality given a candidate solution, and the function's gradient is not needed.
>
>Like many EAs, BBO was motivated by a natural process; in particular, BBO was motivated by biogeography, which is the study of the distribution of biological species through time and space.[1] BBO was originally introduced by Dan Simon in 2008.[2]

## Dependency

[论文1]()

[论文2]()

## Features

### MBBO 详述

***GOAL：*** To solve 3 problems —— the high energy consumption, unbalanced loading, large number of migration time of vms hosted on pms in DC.

***Model：*** We design a Multi-objective model to represent the VM Consolidation problem, referring to the biogeography-based optimization algorithm hybrid with differential evolution.

***Key steps in MBBO：*** We have 6 steps to initialize init_population and keep close to the Near-Optimal Solution。

![./viz/static/img/mbbo-steps.png](./viz/static/img/mbbo-steps.png?raw=False)

1. 采用随机分布概率模型，initialize the initialize_population
2. 余弦迁移模型进算各个chrom的迁入迁出率
3. 基于迁移率和差分进化模型，生成新的chrom
4. 基于高斯突变，生成新的chrom
5. 进行有效解判断，并计算各chrom3各HSI，使用Non-dominated-rankings排序
6. 精英解选择与替换

### the output of MBBO

after `x` pre-set generations, the final `elite_chrom` must be the best one of all this x generations chroms.
this elite_chrom应该有最小的pm占用量，即降低能耗，同时具有最低的load_index,具有最短的迁移时间，但是肯定会高于原来的迁移时间0.

### Dash Board

页面展示经过MBBO运算后的结果图，每个方框为一个pm,其中沿对角矢量方向放置vm，

1. 针对每个虚拟机的标签说明
包括，vm标号，尺寸，迁移序列。。。
![vm-label.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/vm-label.png?raw=true)

![vm-label2.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/vm-label2.png?raw=true)

2. 针对每个pm的标签说明
编号，被占用的cpu,mem，hosted的vm编号

![pm-label.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/pm-label.png?raw=true)

![empty-pm-label.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/empty-pm-label.png?raw=true)

3. MBBO算法控制面板表单输入（后期完善）

![control-panel.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/control-panel.png?raw=true)

4. MBBO算法主要参数、模型及结果展示面板

![mbbo-output.png](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/mbbo-output.png?raw=true)

### 多迭代generations结果对比

![comparison-diff-generation](https://github.com/zam121118/mao-mbbo/blob/master/viz/static/img/comparison-iterative.png?raw=true)


Generations | Computing Time| begin-end used pms | 3 begining HSIs| 3 ending HSIs|
----|----|---|---|----|
200 | 3.023 secs | 131 - 116 = 15 | (54743.2609596, 8.75537529930, 0) | (52063.0378987, 5.49267203751, 12805)
2000 | 29.628 secs | 124 - 96 = 28  | (53418.6276904, 22.6279966643, 0) | (43144.4035638, 6.55533797063, 13000)
10000 | 2.5 mins | 130 - 93 = 37 | (55652.4855526, 15.7182977405, 0) | (41804.6556596, 6.01514788466, 13000)
50000 | 0.2133 hours | 130 - 81 = 49 | (55202.1604600, 19.6813142858, 0) | (36440.5265390, 7.33657331359, 12935)
100000 | 0.4200 hours | 136 - 89 = 47 | (57004.0880516, 10.7108315600, 0) | (40029.2901459, 5.17318073288, 12870)
500000 | need 2 hours | 129 - 87 = 42 | (55217.8475305, 12.0993221000, 0) | (39136.4475108, 3.68236215952, 12935)
1000000 | 4.06 hours | 129 - 89 = 40 | (57895.8260015, 12.4676324198, 0) | (40027.6324884, 3.87020776156, 12870)


## Demo

主要全局面板展示

The visualization powered by pixi.js:

![pixi.js version](https://github.com/zam121118/mao-mbbo/blob/hh-dev/viz/static/img/demo.png?raw=true)
