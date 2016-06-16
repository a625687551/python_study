#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' sorted '

_author_='wangjianfeng'

#use sorted() to sort list
print(sorted([1,5,68,8,7,96,3,6,9,8,4]))

#also sorted() is a high-order function
print(sorted([36,-9,-845,52,45,-875],key=abs))

#sorted str compare ASCII
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

#practice
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
print(sorted(L,key=lambda t:t[0]))
print(sorted(L,key=lambda t:t[1],reverse=True))
