# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:24:49 2021

@author: nolan

Description
Calculate S.S=1！+2！+3！+…+N！

 

Input

A natural number N.   1<=N<=10

 

Output
A natural number S.

 

Sample Input
2
 

Sample Output
3

"""

n = int(input())
s = 0

for i in range(1, n+1):
    m = 1
    for j in range(1, i+1):
        m *= j
    
    s+=m

print(s)



