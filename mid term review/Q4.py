# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:38:35 2021

@author: nolan
"""

n = int(input())
s = 0
for i in range(7, n+1, 7):
    s += i
print(s)