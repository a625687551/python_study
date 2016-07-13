#!usr/bin/env python3
# -*- coding: utf-8 -*-

'rugular expression'

_author_='wangjianfeng'

import re

#匹配成功则返回一个match 否则NONE
print(re.match(r'^\d{3}-\d{3,8}','010-12345'))
print(re.match(r'^\d{3}-\d{3,8}','010 12345'))

#切分字符
#以空格为切分单元
print('a b   c'.split(' '))
print(re.split(r'\s+','a b   c   d'))
print(re.split(r'[\s\,]+','a,b, c  d'))
print(re.split(r'[\s\,\;]+','a,b ;;c d'))
m=re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
print(m.group(0))
print(m.group(1))
print(m.group(2))
t='19:20:55'
s=re.match(r'(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print(s.group())
#贪婪匹配
print(re.match(r'^(\d+?)(0*)$','102000').group())