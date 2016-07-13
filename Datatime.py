#!usr/bin/env python3
# -*- coding: utf-8 -*-

'datatime'

_author_='wangjianfeng'

from datetime import datetime,timedelta
now=datetime.now()
print(now)
print(type(now))

dt=datetime(2015,4,6,12,20)
print(dt)
print(dt.timestamp())#转换为timestamp标准时间

t=1428294000.0
print(datetime.fromtimestamp(t)) #转本地时间
print(datetime.utcfromtimestamp(t))#转为UTC时间

#str 互换datetime
print(now.strftime('%a,%b %d %H:%M'))#时间转STR
cday=datetime.strptime('2016-6-1 18:15:20','%Y-%m-%d %H:%M:%S')#str to time
print(cday)
print('----------------')
#时间加减
print(now+timedelta(hours=10))
print(now+timedelta(days=1))
print(now+timedelta(days=2,hours=12))