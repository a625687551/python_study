#!usr/bin/env python3
# -*- coding: utf-8 -*-

'base64 '

_author_='wangjianfeng'

#base64是一种用64种字符来表示二进制数据的方法
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#base64中有+ /在url中不能作为参数，所以又有一种urlsafe的base64编码，其实是+ /变为了-_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
#在url、cookies中=会造成很多歧义，所以很多base64编码会把=去掉
def safe_base64_decode(s):
    return base64.b64decode(s+b'='*(len(s)%4))

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

