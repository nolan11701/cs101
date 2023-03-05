# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:54:22 2021

@author: nolan
"""
x = int(input())
a = [1]*x
for i in range(0, x):
     a[i] = [1]*(i+1)
     for j in range(0, i):
         if j != 0 and j != i:
             a[i][j] = a[i-1][j-1] + a[i-1][j] 
     print(*a[i])   
             
# for k in range(len(a)):
    # print(*a[k])  
