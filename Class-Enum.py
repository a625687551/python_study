#!usr/bin/env python3
# -*- coding: utf-8 -*-

'use enum'

_author_='wangjianfeng'

from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():#注意前后member不一样
    print(name,'=>',member,',',member.value)

@unique#Decorator unique可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun=0#sun value set 0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
day1=Weekday.Mon
print('day1=',day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday.Mon==day1)
print(day1==Weekday.Tue)
print(Weekday(1))
print(Weekday(1)==day1)

for name,member in Weekday.__members__.items():
    print(name,'=>',member)
