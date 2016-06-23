#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'file open write close'

_author_='wangjianfeng'

def text_create(name,msg):
    desktop_path='C:\\Users\wangjianfeng2014\Desktop\\'
    full_path=desktop_path+name+'.txt'
    file=open(full_path,'w')
    file.write(msg)
    file.close
    print('done')
text_create('test','hello world! This is my first text open and write')