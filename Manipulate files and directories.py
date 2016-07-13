#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'system'

_author_='wangjianfeng'

import os
print(os.name)#获取计算机操作系统类型
#print(os.uname)#获取操作系统详细信息 在win上面不支持··
print(os.environ)#获取环境变量
print('----------------------------------')
print(os.path.abspath('.'))
#在某个目录下创建一个新的目录，首先先把新目录的完整路径表现出来
os.path.join('D:\\学习\GitHub\Python-Study\\','testdir')
#然后创建一个目录
os.mkdir('D:\\学习\GitHub\Python-Study\\testdir')
#然后删除目录
os.rmdir('D:\\学习\GitHub\Python-Study\\testdir')

#拆分路径
print(os.path.split('C:\\Users\wangjianfeng2014\Desktop\my file.txt'))
print(os.path.splitext('C:\\Users\wangjianfeng2014\Desktop\my file.txt'))
#重命名和删除
#os.rename('test.py','test.py')
#os.remove('test.py')

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有py file
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
