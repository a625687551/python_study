<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' map/reduce function'

_author_='wangjianfeng'

#map function can do list's element
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce function
#reduce函数可以用传给reduce的func()(必须是一个二元操作函数)先对集合中的第1，2数据进行操作，
#得到的结果在与第三个数据用func()函数运算，最后得到一个结果
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5,6]))
#[1,3,5,7,9]become 13579
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

#endlish name normalize
def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT','WANGJIANFENG']
print(list(map(normalize,L1)))

#接收一个list并且求积

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*7*9=',prod([3,5,7,9]))
#using str2float function make string '123.456'to 123.456
#sn=s.split('.')[0]+s.split('.')[-1]
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2float(s):
    a,b=s.split('.')
    num=reduce(lambda x,y:x*10+y,map(char2num,(a+b)))
    return num/(10**len(b))
print(str2float('123.456'))
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' map/reduce function'

_author_='wangjianfeng'

#map function can do list's element
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce function
#reduce函数可以用传给reduce的func()(必须是一个二元操作函数)先对集合中的第1，2数据进行操作，
#得到的结果在与第三个数据用func()函数运算，最后得到一个结果
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5,6]))
#[1,3,5,7,9]become 13579
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

#endlish name normalize
def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT','WANGJIANFENG']
print(list(map(normalize,L1)))

#接收一个list并且求积

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*7*9=',prod([3,5,7,9]))
#using str2float function make string '123.456'to 123.456
#sn=s.split('.')[0]+s.split('.')[-1]
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2float(s):
    a,b=s.split('.')
    num=reduce(lambda x,y:x*10+y,map(char2num,(a+b)))
    return num/(10**len(b))
print(str2float('123.456'))
>>>>>>> origin/Base
