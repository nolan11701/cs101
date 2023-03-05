# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:51:55 2021

@author: nolan
"""

n = int(input())


for i in range(1,n+1):
    s = 0
    for j in range(1, i//2+1):
        if i%j == 0:
            s += j
            
    if s == i:
        print(s)