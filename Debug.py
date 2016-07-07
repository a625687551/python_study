#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'subject'

_author_='wangjianfeng'

import logging
import pdb
def foo(s):
    n=int(s)
    assert n!=0,'n is zeor'
    return 10/0

def main():
    foo('0')

s='0'
n=int(s)
pdb.set_trace()
logging.info('n=%d'%n)
print(10/n)