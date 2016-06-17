<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' filter '

_author_='wangjianfeng'

def is_odd(n):
    return n%2==0
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a','b',None,'c',' '])))

#filter prime number
#define a odd number sequence
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#define a filter 
def _not_divisible(n):
    return lambda x:x%n>0
#define a generator
def primes():
    yield 2
    it=_odd_iter()#初始化序列
    while True:
        n=next(it)#返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)#构造新数列
#打印1000以内的素数
for n in primes():
    if n<100:
        print(n)
    else:
        break

#过滤掉非回数
def is_palindrome(n):
    return str(n)[::-1]==str(n)
output=filter(is_palindrome,range(1,10000))
print(list(output))
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' filter '

_author_='wangjianfeng'

def is_odd(n):
    return n%2==0
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a','b',None,'c',' '])))

#filter prime number
#define a odd number sequence
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#define a filter 
def _not_divisible(n):
    return lambda x:x%n>0
#define a generator
def primes():
    yield 2
    it=_odd_iter()#初始化序列
    while True:
        n=next(it)#返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)#构造新数列
#打印1000以内的素数
for n in primes():
    if n<100:
        print(n)
    else:
        break

#过滤掉非回数
def is_palindrome(n):
    return str(n)[::-1]==str(n)
output=filter(is_palindrome,range(1,10000))
print(list(output))
>>>>>>> origin/Base
