#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'account login'

_author_='wangjianfeng'

password_list=['****','12345']
def account_login():
    password=input('please input your password:')
    password_correct=password==password_list[-1]
    password_reset=password==password_list[0]
    if password_correct:
        print('login success')
    elif password_reset:
        new_password=input('enter a new password:')
        password_list.append(new_password)
        print('your password has changed successfully')
        account_login()
    else:
        print('wrong password or invalid input')
        account_login()
account_login()