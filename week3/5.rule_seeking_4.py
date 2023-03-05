# -*- coding: utf-8 -*-
"""
#Created on Sun Sep 26 20:45:30 2021

@author: nolan

Description of the topic:

Find the rule ,output first n items of the sequence

1,1,1,2,3,4,6,9,13,19

Input format:+

a positive integer n

Output format:

a row of n positive integers

Sample input 1:

2

Sample output 1:

1 1

Appointment:

1<=n<=50
    =-==
prompt:
"""
# Nolan Li 9/26/2021 Python homework week 3

n = int(input())
if n>=1 :
    print("1", end = ' ')

if n>=2:
    print("1", end = ' ')

if n>=3:
    print("1", end = ' ')
    
a = 1
b = 1
c = 1

for i in range(4, n+1):

    y = a + c
    a = b
    b = c
    c = y
    print(y, end = ' ')

