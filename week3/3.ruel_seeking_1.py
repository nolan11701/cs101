# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:28:54 2021

@author: nolan

Description of the topic:

Find rules and output the first n items of the sequence

2,1,4,3,6,5,...

Input format:

a positive integer n

Output format:

a row of n positive integers

Sample input 1:

2

Sample output 1:

2 1

Appointment:

1<=n<=100


"""

# Nolan Li 9/26/2021 Python homework week 3

n = int(input())

for i in range(1,n+1):
    
    if i%2 == 1:
        y = i + 1
    else:
        y = i - 1

    print(y, end = ' ')