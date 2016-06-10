# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:24:26 2016

@author: wangjianfeng2014
"""
#tower of hanoi(use recursion function)
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)
move(12,'A','B','C')