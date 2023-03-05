# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:35:53 2021

@author: nolan
"""

x = input()
e = list(x)
e.reverse()

for i in range(len(e)):
    if e[0] == '0':
        e.remove(e[0])
        
print(*e, sep = "")