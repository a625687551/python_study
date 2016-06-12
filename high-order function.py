#!usr/bin/env python3
# -*- coding:utf-8 -*-

' high-order function '

_author_='wangjianfeng'

def add(a,b,f):
    return f(a)+f(b)
a,b=-5,6
f=abs
print(add(a,b,f))