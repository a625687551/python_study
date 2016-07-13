#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'serialization'

_author_='wangjianfeng'

import pickle
import json
#获取file-like object 的对象
d=dict(name='bob',age=20,score=80)
print(pickle.dumps(d))
#json之间的转换,json的标准编码是utf-8
print(json.dumps(d))

#高级转化
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,88)
#无法直接转化，采用特殊办法
def Student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
        }
print(json.dumps(s,default=lambda obj:obj.__dict__))