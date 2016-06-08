# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:08:05 2016

@author: wangjianfeng2014
"""

import math

def quadratic(a,b,c):
    m=b*b-4*a*c
    if a==0:
        return -c/b
    elif m<0:
        return 'no answer!'
    else:
        return (-b-math.sqrt(m))/2/a,(-b+math.sqrt(m))/2/a
x1=quadratic(2,3,1)
print(x1)

