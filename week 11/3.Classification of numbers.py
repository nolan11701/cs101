# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:37:57 2021

@author: nolan
"""

mamaaaaa = int(input())
johncena = list(map(int, input().split()))
jomama = len([x for x in johncena if int(x)>0])
poo = len([x for x in johncena if int(x)==0])
pickles = len([x for x in johncena if int(x)<0])
print(jomama)
print(poo)
print(pickles)