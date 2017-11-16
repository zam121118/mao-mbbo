#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-15
@Author : Amy
Goal: 定义Dimension-aware herustics常见方法Norm-based Greedy即通过多维向量间欧几里得距离作为bins、objects的排序标准，
      再依据资源约束，循环求解vector bin pack结果。
      采用L2 norm distance metric: 
      from all unassigned VMs, it places the VM v that minimizes the quantity sum(w_i*(v_i - h_i)**2)在所有纬度上求和。
'''


import time
import random
import math
import json
import sys