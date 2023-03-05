# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:50:49 2021

@author: nolan

Description of the topic:

Find pattern and output the first n items of the sequence

1,1,2,3,5,8,...

Input format:

a positive integer n

Output format:

a row of n positive integers separated by space

Sample input 1:

2

Sample output 1:

1 1

Appointment:

1<=n<=50

"""
# Nolan Li 9/26/2021 Python homework week 3

n = int(input())
if n>=1 :
    print("1", end = ' ')

if n>=2:
    print("1", end = ' ')

a = 1
b = 1
    
for i in range(3, n+1):

    y = a + b
    a = b
    b = y
    
    print(y, end = ' ')