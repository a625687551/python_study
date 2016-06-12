#!usr/bin/env python3
# -*- coding: utf-8 -*-

' Iterator '

_author_='wangjianfeng'

#judgement
from collections import Iterable
print(isinstance([],Iterable)) 
print(isinstance({},Iterable)) 

#using iter() function make others become iterable 
#list dict str is iterable but not a iter
print(isinstance(iter([]),Iterable))