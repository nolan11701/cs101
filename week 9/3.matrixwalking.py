# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:08:31 2021

@author: nolan
"""

m, n = map(int, input().split())
m += 1
n += 1

a = [[1]*m for i in range(n)]

for i in range(0, n):
     for j in range(0, m):
         if j != 0 and i != 0:
             a[i][j] = a[i-1][j] + a[i][j-1] 

print(a[n-1][m-1])   