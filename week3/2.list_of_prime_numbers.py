# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:40:20 2021

@author: nolan

Description

A prime number is the number which can only be divided by 1 and itself. For example,2,3,5,7,11,13,17 are prime numbers. Given an integer N,please find all the prime number between 1 and N.
Input
The first line is an integer N.  1<=N<=2000

Output

One line, all the prime numbers put in order, separated with spaces.

Sample Input
20

Sample Output
2 3 5 7 11 13 17 19
 
Hint
"""

n = int(input())
for i in range(1,n+1):
    
    if i == 1:
        continue
    
    prime = True
    
    for j in range(2,i//2+1):
        if i%j == 0:
            prime = False
            break
            
    if prime:
        print(i, end = ' ')
    