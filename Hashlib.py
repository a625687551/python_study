#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'hashlib'

_author_='wangjianfeng'

import hashlib

#MD5算法（生成结果是固定的128bit字节，通常用一个32位的16进制的字符串表示
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
#分块调用
#md5.update('how to use md5 in '.encode('utf-8'))
#md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#SHA1算法-生成一个160bit字节，通常用一个10位的16进制的字符串表示
sha1=hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
