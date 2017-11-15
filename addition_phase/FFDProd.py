#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-15
@Author : Amy
Goal: 定义FFD-based Herustics常见方法FFDProd即通过将多维demand、capacites向量转化为意义明确的标量(volume of the vector)，
      以标量值大小为bins、objects的排序标准，再依据资源约束，循环求解vector bin pack结果。
      FFDProd is to set volume as the product of the values， 即对所有纬度值连乘作为排序标准；
'''


import time
import random
import math
import json
import sys