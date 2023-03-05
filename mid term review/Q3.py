# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:10:43 2021

@author: nolan
"""

a = list(map(int, input().split()))
if a[1] in (1,3,5,7,8,10,12):
    print("31")
elif a[1] in (4,6,9,11): 
    print("30")
elif a[1] == 2 and a[0]%4 == 0 or a[0]%400 == 0 and a[0]%100 != 0:
    print("29")
else:
    print("28")