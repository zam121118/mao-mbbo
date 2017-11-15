#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Date : 2017-11-15
@Author : Amy
Goal: 定义Dimension-aware herustics常见方法Dot-Product即通过多维向量间点积值作为bins、objects的排序标准，
      在本算法中为了更直观反应矢量装箱优化标准，采用以向量间夹角最小即cos值最大作为排序标准，再依据资源约束，
      循环求解vector bin pack结果
'''


import time
import random
import math
import json
import sys