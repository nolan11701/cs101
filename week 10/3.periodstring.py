# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:36:32 
@author: nolan

"""

s = input()
t = len(s)

for i in range(1, t+1):
    if t%i == 0 and s[0:i] * int(t/i) == s:
            print(i)
            # IT"S BREAK TIME
            break