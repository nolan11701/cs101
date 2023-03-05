# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:46:32 2021

@author: nolan
"""

m, n = map(int, input().split())
a = [[0]*n for i in range(m)]
b = [[0]*m for i in range(n)]

for i in range(m):
    c = list(map(int, input().split()))
    a[i] = c

for i in range(n):
    for j in range(m):
        b[i][j] = a[j][i]
    print(*b[i])