# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:09:12 2021

@author: nolan
"""

n = int(input())
s = 0
for i in range(1, n+1):
    s += 1/i
f = "{0:.6f}"
print(f.format(s))

