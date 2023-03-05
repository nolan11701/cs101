# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:22:39 2021

@author: nolan
Description：
Please write down a program to output Pyramid graphics.

 

Input：
Multiple test data, each of which is entered with an integer n (1 < = n < 9).

 

Output：
Pyramid

 

Sample input：
1
3
 

Sample output：
*
  *
 ***
*****
"""

while True:
    k = int(input())

    z = ""
    for i in range(1, k+1):
        z = (k-i)*" "
        print(z + (2*i-1)*"*")