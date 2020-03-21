# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 06:42:13 2020

@author: User
"""







counter=0
answer = int(input())
lowest = 1
highest = 20


while True:
    a = int(input('AQA從1到20猜一個數字OWO'))
    if answer == a:
        print('你猜對了!')
        break
    else:
        print('傻逼，你猜錯了aua')
        counter=counter+1
        if counter >4:
            break








