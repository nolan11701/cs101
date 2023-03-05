# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:34:40 2021

@author: nolan
"""

import math as m
n = int(input())
count = 0
for i in range(1,n+1):
    a = list(map(int, str(i).strip()))
    s = m.prod(a)
    y = sum(a)
    if y>=20 and s>=162:
        count += 1
print(count)