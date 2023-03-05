# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:48:22 2021

@author: nolan
"""

m = int(input())

for i in range(1,m+1):
    divisible_by_five = False
    temp = i
    while(temp > 0):
        if temp % 10 == 5:
            divisible_by_five = True
        temp = temp // 10
        
    divisible_by_three = (i % 3 == 0)
    
    if (divisible_by_five and divisible_by_three):
        print(i)
