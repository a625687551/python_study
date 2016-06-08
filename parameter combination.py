# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:56:51 2016

@author: wangjianfeng2014
"""
#parameter combination
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'d=',d,'kw',kw)
f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)  
f2(1,2,d=99,ext=None)
#use list or tuple
args=(1,2,3,4)
kw={'d':99,'m':'#'}
f1(*args,**kw)