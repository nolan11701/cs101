# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:41:46 2021

@author: nolan
"""

l = int(input())
a = list(map(int, input().split()))
print(max(a) - min(a))