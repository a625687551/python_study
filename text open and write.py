#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'file open write close filter'

_author_='wangjianfeng'

def text_create(name,msg):
    desktop_path='C:\\Users\wangjianfeng2014\Desktop\\'
    full_path=desktop_path+name+'.txt'
    file=open(full_path,'w')
    file.write(msg)
    file.close
    print('done')
def text_filter(word,censored_word='lame',changed_word='awesome'):
    return word.replace(censored_word,changed_word)
def censored_text_create(name,msg):
    clean_msg=text_filter(msg)
    text_create(name,clean_msg)
censored_text_create('my file','python is lame')