# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:22:28 2021

@author: nolan
"""

n = int(input())
s = 0
f = "{0:.3f}"
for i in range(1, n+1):
    if i%2 == 0:
        s -= 1/i
    else:
        s += 1/i 
print(f.format(s))

