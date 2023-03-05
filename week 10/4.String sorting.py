# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:43:48 2021

@author: nolan
"""

y = int(input())
x = []

for i in range(y):
    x.append(input())
    
x.sort()

print(*x, sep = "\n")