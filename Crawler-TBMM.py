#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'crawler taobaomm'

_author_='wangjianfeng'

import re

old_url='http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

with open('text.txt','r',encoding='utf-8') as f:
    html=f.read()
    # print(html)
#获取标题
title=re.search('<title>(.*?)</title>',html,re.S).group(1)
print(title)

#match url
# link=re.findall('href="(.*?)"',html,re.S)
# for i in link:
#     print(i)

# large first
text_filed=re.findall('<ul>(.*?)</ul>',html,re.S)[0]
the_text=re.findall('">(.*?)</a>',text_filed,re.S)
for every_text in the_text:
    print(every_text)

#sub 实现翻页
for i in range(2,total_page+1):
    new_link=re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print(new_link)