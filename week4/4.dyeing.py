# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:46:33 2021

@author: nolan

Description of the topic:

Little A wants to dye the fence of his home. The fence is divided into n segments. At the beginning, each fence has a color of 0. Each time, Small A will dye the fence into a certain color. Ask for the color of the final fence.

Input format:

The first line is an integer n indicating the length of the road.

The second line is an integer m indicating the number of times of dyeing.

The next m lines are three integers l, r, b for each line, indicating that the interval l to r are dyed to the color b.

Output format:

A number of m rows, indicating what color each segment is.

Sample input:


3

2

1 2 1

2 3 2

Sample output:


1 2 2

 


Appointment:

  All numbers do not exceed 1000.
  
"""

n = int(input())
f = [0] * n

m = int(input())

for i in range(m):
    c = list(map(int, input().split()))
    for i in range(c[0]-1, c[1]):
        f[i] = c[2]

for k in f: print(k, end=" ")



