#!usr/bin/env python3
# -*- coding: utf-8 -*-

' test '

_author_='wangjianfeng'

class Cocacola:
    calories=140
    sodium=45
    total_carb=39
    caffeine=34
    ingredients=[
        'high fructose corn syrup',
        'carbonated water ',
        'phosphoric acid',
        'natural flavors',
        'caramel color',
        'caffeine'
    ]
    def __init__(self,logo_name):
        self.local_logo=logo_name
    def drink(self):
        print('you got {} cal energy !'.format(self.calories))
class CaffeineFree(Cocacola):
    caffeine=0
    ingredients=[
        'high fructose corn syrup',
        'carbonated water ',
        'phosphoric acid',
        'natural flavors',
        'caramel color',
    ]
coke_a=CaffeineFree('Cocacola-free')
coke_a.drink()

