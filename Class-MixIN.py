#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' Mixin '

_author_='wangjianfeng'

class Animal(object):
    pass
#大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('running...')
class Flyable(object):
    def fly(self):
        print('flying...')
#all kinds of animal python可以多重继承但是JAVA不可以只能单一继承
class Dog(Mammal,Runnable):
    pass
class Cat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird,Runnable):
    pass
class Bat(Bird,Flyable,Mammal):
    pass
