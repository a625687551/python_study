# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:49:47 2016

@author: wangjianfeng2014
"""
#keyword parameter
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('wangjianfeng',26)
person('lixueyuan',25,city='xian')
extra={'city':'Beijing','job':'engineer'}
person('yanxiaohe',100,city=extra['city'],job=extra['job'])
person('yanxiaohe',100,**extra)
#named keyword parameters
def people(name,age,*,city,job):
    print(name,age,city,job)
people('jack',24,city='beijing',job='engineer')

