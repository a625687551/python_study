#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class instance private'

_author_='wangjianfeng'

class Student:
    def __init__(self,name,score):
        self.__name=name#加入————确保了属性的访问限制，变为一个私有属性，只有内部可以访问
        self.__score=score
    def print_score(self):
        print('{}:{}'.format(self.__name,self.__score))
    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
    def get_name(self):#获取名字
        return self.__name
    def get_score(self):#获取分数
        return self.__score
    def set_score(self,score):#设置分数
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
bart=Student('wangjianfeng',89)

