#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'itertools'

_author_='wangjianfeng'

import itertools
'''
natuals=itertools.count(1)#创建的无限迭代器，注意停止
#for i in natuals:
#    print(i)
ts=itertools.takewhile(lambda x: x<=10,natuals)#takewhile截取数据
print(list(ts))

#cycle会把传入的序列不断迭代
cs=itertools.cycle('abc')
for c in cs:
    print(c)

#repeat 可以把一个元素无线重复下去，第二个参数可以控制重复次数
ns=itertools.repeat('a',3)
for n in ns:
    print(n)
'''    
#chain
for c in itertools.chain('BCD','344'):
    print(c)
