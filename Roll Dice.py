#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'roll dice'

_author_='wangjianfeng'

import random
def roll_dice(numbers=3,points=None):
    print('<<<<<roll the dice>>>>>')
    if points is None:
        points=[]
    while numbers>0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
def roll_result(total):
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    print('<<<<<Game STARTS!>>>>>')
    choice=['Big','Small']
    your_choice=input('Small or Big:')
    if your_choice in choice:
        points=roll_dice()
        total=sum(points)
        youwin=your_choice==roll_result(total)
        if youwin:
            print('The points are',points,'You Win!')
        else:
            print('The points are',points,'You Lose!')
    else:
        print('invalid input!')
        start_game()
start_game()
    
        
