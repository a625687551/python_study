#!usr/bin/env python3
# -*- coding: utf-8 -*-

' datetime-test '

_author_='wangjianfeng'

import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    #使用strptime活得datetime
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    #利用正则表达式获取timezone,并且利用int和zone使其变为整数
    #tz=timezone(timedelta(hours=int(''.join(re.match(r'UTC([\+|\-])(\d{1,2})', tz_str).groups()))))
    tz=timezone(timedelta(hours=int(''.join(re.match(r'UTC([\+|\-])(\d{1,2})', tz_str).groups()))))
    dt=dt.replace(tzinfo=tz)
    return dt.timestamp()
# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
