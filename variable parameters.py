# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:38:08 2016

@author: wangjianfeng2014
"""
#variable parameters(only a *,but refuse a list or tuple)
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
''''
r=calc([1,2,3])
print(r)
r=calc([1,2,3,5])
print(r)
'''
r=calc(1,2)
print(r)
#to slove list or tuple questions
nums=[1,2,3,5]
print(calc(*nums))