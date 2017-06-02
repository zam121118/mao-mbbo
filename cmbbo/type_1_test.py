# coding: utf-8

## 这个文件主要对比docker-hm与docker-vm-pm的实验场景，在size,generation,初始容器数量与尺寸,完全相同；
## 且docker-vm-hm中vm:hm=1:1的情况下进行测试判断，
## 测试1： 仅以power_cost为HSI的情景下
## 测试2： 以power_cost和 vm balance index为HSI的情景下
## 测试3： 考虑到migration_time的HSI比较