#!usr/bin/env python3
# -*- coding: utf-8 -*-

'try except'

_author_='wangjianfeng'

import logging

try:
    print('try....')
    r=10/2
    print('result is',r)
#不同的except抓取不同的错误
except ValueError as e:
    print('ValueError',e)
except ZeroDivisionError as e:
    print('except:',e)
else:#当没有错误时候输出
    print('NO Error')
finally:
    print('Finally...')
print('——————————————————————————')

def foo(s):
    return 10/0
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('*************')