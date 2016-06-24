#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'99 multiplication table'

_author_='wangjianfeng'

for i in range(1,10):
    for j in range(1,i+1):
        #print('%d*%d=%d\t'%(j,i,i*j),end='')
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print('')
