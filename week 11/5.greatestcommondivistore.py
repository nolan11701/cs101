# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:57:22 2021

@author: nolan
"""

a, b = map(int, input().split())

def gcd(a, b):
    if a == 1 or b ==1:
        return 1
    if a == b:
        return b
    
    x = max(a, b) - min(a, b)
    if a%x == 0 and b%x == 0:
        return x
    else:
        return gcd(max(min(a, b), x), min(min(a, b), x))

# def gcd(a, b):
#     if a%b == 0:
#         return b
#     else:
#         return gcd(b, a%b)

print(gcd(a,b))