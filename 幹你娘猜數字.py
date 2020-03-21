# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:15:06 2020

@author: User
"""











counter=0
answer = guess()


while True:
    a = int(input('從1到20猜一個數字，你他媽給我快點'))
    if answer == a:
        print('你猜對了!')
        break
    else:
        print('傻逼，你猜錯了aua')
        counter=counter+1
        if counter >4:
            break
    
   
   
   





























