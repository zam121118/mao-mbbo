#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@Date: 2017-11-22
@Goal: python也可以支持函数句柄作为函数的形参列表
     简化函数间多种方法的调用
'''


def find_HM(bins, handle0, handle1):
    weightedHMBins = handle0(bins, handle1)
    return True

def weightHMBins1(bins, handle):
    print 'ok, we now call function 1'
    handle(bins)
    return True

def weightHMBins2(bins):
    print 'ok, we now call function 2'
    return True

if __name__ == '__main__':
    bins = [1,2,3]
    find_HM(bins, weightHMBins1, weightHMBins2)
