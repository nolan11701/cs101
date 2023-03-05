# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:20:12 2021

@author: nolan
"""

n = int(input())
s = 0

while (n != 1):
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    s += 1
print(s)