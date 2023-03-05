# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:57:52 2021

@author: nolan

Description
Given an integer N, caculate 1+1/2+1/3+...+1/N.（the result keeps 6 digits after the decimal point）

Input
An integer N （1<=N<=1000）

Output
One floating-point number.（the result keeps 6 digits after the decimal point）

Sample Input
2

Sample Output
1.500000
"""
# Nolan Li 9/26/2021 Python homework week 3

x = int(input())
a = 0
for i in range(1,x+1):
    a += 1/i
print('%.6f'%a)*+