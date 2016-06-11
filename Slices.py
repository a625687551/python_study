# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:52:51 2016

@author: wangjianfeng
"""
#Slices
L=['WANGJIANFENG','LIXUEYUAN','YANXIAOHE','JACK']
print(L[0:3])#0 to 3(not include 4 )
print(L[0:4:2])#0 to 4 space 2
print(L[-2:])

R=list(range(100))
print(R)
print(R[::2])#100内的偶数
print(R[:10])
print(R[::5])
print(R[:])

#also tuple and string can do it
print((1,2,3,6,5,4,9)[:3])
print('abcdef'[:3])