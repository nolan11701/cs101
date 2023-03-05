# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:00:24 2021

@author: nolan

Merge ordered arrays.
Merge the two arrays A and B sorted from small to large into an array C that is still sorted from small to large.

Sample input:
5
1 3 5 7 9
5
2 4 6 8 10


Sample output:
1 2 3 4 5 6 7 8 9 10


time limit:
1000

memory limit:
65536
"""

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = a + b
for i in range(len(c)):
    for j in range(len(c)-i-1):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
print(*c)