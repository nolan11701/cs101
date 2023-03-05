# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:37:33 2021

@author: nolan

Title Description:

 

Small C has a plane!

 

It finds two points on the plane. Please find out the Chebyshev distance between them. Chebyshev distance is defined as the bigger one of absolute value of the coordinate difference between X and Y axis.

 

 

Input format:

 

Four integers, a, b, c, D. Coordinates are (a, b) and (c, d)

 

 

Output format:

 

Output Euclidean distance of these two points.

 

 

Sample input:

 

0 0 3 4

 

Sample output:

 

4

 

 

Appointment:

 

0<=a, b, c, d<=100
"""

def chebyyshev_distance(a,b,c,d):
    return max(abs(c-a), abs(d-b))

a,b,c,d = map(int, input().split())
print(chebyyshev_distance(a, b, c, d))
