# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:46:16 2021

@author: nolan

Description of the topic:

Enter 5 lowercase letters, turn each letter to the letter 2 after it, e.g. a to c, c to e, z to b, and output them.

Input format:

Enter 5 lowercase letters

Output format:

The output format is described in the title.

Sample input 1:

abcde

Sample output 1:

cdefg

Sample input 2:

aacca

Sample output 2:

cceec
"""

def pl(i):
    return i+2

def al(a):
    b = list(map(ord, a))
    c = list(map(pl, b))
    d = list(map(chr, c))
    return "".join(d)

a = list(input())
t = al(a)
print(t)

