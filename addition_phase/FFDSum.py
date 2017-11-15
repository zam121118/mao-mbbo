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