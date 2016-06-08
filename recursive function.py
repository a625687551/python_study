# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:31:21 2016

@author: wangjianfeng2014
"""
#recursive function
'''
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)
print(fact(1))
print(fact(1000))
'''
#tail recursion(but when n=1000 it is also stack overflow,that is too bad!)
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(100))