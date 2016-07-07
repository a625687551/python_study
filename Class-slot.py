#!usr/bin/env python3
# -*- coding: utf-8 -*-

' _slot '

_author_='wangjianfeng'

class Student(object):
    _slot_=('name','age')#use tuple定义允许绑定的属性名称
s=Student()
s.name='wang'
s.age=26
s.score=99
print(s.score)