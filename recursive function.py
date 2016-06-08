# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:31:21 2016

@author: wangjianfeng2014
"""
#recursive function
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)
print(fact(1))
print(fact(1000))
