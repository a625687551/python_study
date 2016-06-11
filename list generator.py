#!usr/bin/env python3
# -*- coding: utf-8 -*-

' list generator '

_author_='wangjianfeng'

#the difference between generator and comprehensions
print([x*x for x in range(10)])
g=(x*x for x in range(10))
for n in g:
    print(n)
#Fibonacci sequence
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b # print(b) chang to yield become a generator
        a,b=b,a+b
        n=n+1
    return 'done'
for n in fib(6):
    print(n)