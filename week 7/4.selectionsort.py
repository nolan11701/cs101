# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:43:39 2021

@author: nolan
"""


n = int(input())
s = list(map(int, input().split()))
 
for i in range(n):
    m = i
    for j in range(i, n):
        if s[j] < s[m]:
            m = j
    s[m], s[i] = s[i], s[m]
print(*s)