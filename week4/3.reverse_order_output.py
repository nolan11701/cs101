# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:05:06 2021

@author: nolan

Description of the topic:

Given an array of integers, please output these integers in reverse order.

Input format:

The first line is n, indicating the number of digits;

The second line is n integers.

Output format:

A row of n integers separated by space.

Sample input:
3

11 23 45

Sample output:
45 23 11

 

Range:

  N≤1000
  
"""

n = int(input())
a = map(int, input().split())
b = list(a)
b.reverse()
for x in b:
    print(x,end=" ")
    
