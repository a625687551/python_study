#usr/bin/env python3
# -*- coding:utf-8 -*-

#list comprehensions
print(list(range(10)))
#1*1,2*2,3*3,4*4.....
print([x*x for x in range(1,11)])

#并且后面可以加上一些判断来筛选所需要的内容
print([x*x for x in range(1,11) if x%2==0])

#doulbe layer cycle
print([m+n for m in 'ABC' for n in 'yxt'])

#在dict中items()同时可以迭代key和value
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
print([k+'='+v for k,v in d.items()])

#大写变小写
L=['HELLO','World','IBM','Apple']
print([s.lower() for s in L])

#test
R=['Hello','World',18,'IBM','Apple',None]
print([s.lower() for s in L if isinstance(s,str)])