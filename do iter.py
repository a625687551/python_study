#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' do iter '

_author_='wangjianfeng'

#check which can do
from collections import Iterable
print('Iterabel?\'abc\':',isinstance('abc',Iterable))# string can or not
print('Iterable?[1,2,3]',isinstance([1,2,3],Iterable))# list can or not
print('Iterable?123',isinstance(123,Iterable))# integer can or not

#类似JAVA中下标循环，采用python中内置的一个function-enumerate
for i,value in enumerate(['a','b','c']):
    print(i,value)

#two variables in the loop
for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)