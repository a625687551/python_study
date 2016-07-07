#!usr/bin/env python3
# -*- coding: utf-8 -*-

'元类'

_author_='wangjianfeng'


'type()函数 function'
#Hello=type('Hello',(object,),dict(hello=fn))#创建HEllo Class

'metaclass'
#metaclass 是类的模板，所以必须从‘type’派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class Mylist(list,metaclass=ListMetaclass):
    pass
'test'
L=Mylist()
L.add(1)
print(L)