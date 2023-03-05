# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:35:23 2021

@author: nolan
"""
def covnert(x, t):
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if l.find(x) != -1:
        index = l.find(x) + t
        return l[index % 26]
    
    elif u.find(x) !=-1:
        indexo = u.find(x) + t
        return u[indexo % 26]
    
    
s = input()
t = int(input())
b = [covnert(y,t) for y in s]
print(*b, sep = '')