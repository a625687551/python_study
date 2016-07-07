#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' special class '

_author_='wangjianfeng'

'__iter__'#这样class可以用for循环，迭代
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#初始化
    def __iter__(self):
        return self#实例本身就是迭代对象，故返回自身
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b#计算下一个值
        if self.a>10000:
            raise StopIteration
        return self.a
    def __getitem__(self):#可以让class具有list的slice function
        pass
for n in Fib():
    print(n)
#__getatter__可以搞链式调用,这个不太理解
class Chain(object):

    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
#__call__可以调用了自身的方法，另外可以用callable判断一个对象是否可以调用
class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('my name is %s'%self.name)
s=Student('wangjianfeng')
s()