# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:35:07 2021

@author: nolan
"""

x, y = map(int, input().split())
b = [0]*x
u = y
for i in range(y):
    a = list(map(int, input().split()))
    b[i] = a
    for j in range(x):
        b[i][j] = abs(b[i][j])
for i in range(y):
    print()
    for j in range(x):
        print(b[i][j], end = " ")