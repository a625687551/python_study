#!usr/bin/env python3
# -*- coding: utf-8 -*-

'collections'

_author_='wangjianfeng'

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

#namedtuple用法
Point=namedtuple('Point',['x','y'])
p=Point(1,2)

#deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')#appendleft() popleft()可以高效的头部添加和删除
print(q)

#defaultdict 引用dict时候如果key不存在的话会出现keyerrror，如果希望key不存在的话可以返回一个默认值，就可以用defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']= 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderedDict 可以让dict保持顺序
#counter简单的计数器
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)