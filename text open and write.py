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

#每次打开读写都需要open和close 太繁琐，我们使用with 
with open('C:\\Users\wangjianfeng2014\Desktop\my file.txt','r',encoding='gbk') as f:
    print(f.read())#如果文件太多可以考虑用read(size) or readlines()

#读取图片格式文件使用 rb
f=open('C:\\Users\wangjianfeng2014\Desktop\\54877586241642729.jpg','rb')
f.read()
#字符编码以及一些忽略错误
with open('C:\\Users\wangjianfeng2014\Desktop\my file.txt','r',encoding='gbk'，errors='ignore') as f:
    print(f.read())