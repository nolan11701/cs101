# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 13:55:07 2021

@author: nolan
 
Description
Input an integer n,calculate 1+(1+2)+(1+2+3)+...+(1+2+3+...+n).

 

Input

An integer.

 

Output
An integer.

 

Sample Input
4
 

Sample Output
20
 
"""


def pe(n) -> int:
    t = 1
    if n <= 1: 
        return t
    elif n != 1:
        return n + pe(n-1)
def poo(n):
    u = 1
    if n <= 1:
        return u
    elif n != 1:
        return pe(n) + poo(n-1)  

john = int(input())
print(poo(john))