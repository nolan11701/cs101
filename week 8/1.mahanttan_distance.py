# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:05:28 2021

@author: nolan

Manhattan distance
English 

Time limit: 0.2 memory limit: 32M

 

Description:

Little C came to Manhattan and wanted to visit the Metropolitan Museum of Art.

Since Manhattan's roads run perpendicular to each other and the XY axes, they can be seen as gridlines in the coordinate plane. The Manhattan distance is the distance between two points given that you can only travel along these perpendicular roads.

Given Little C's starting coordinates (a, b) and their destination coordinates (c, d), find the Manhattan distance between those points.

Please use function to implement this problem.

 

Input:

The four integers a, b, c, d where the coordinates are (a, b) and (c, d).

 

Output:

Output the Manhattan distance between these two points.

 

Sample input:

0 0 3 4
Sample output:

7
 

Assumptions:

0 <= a, b, c, d <=100
"""

def manhattan_distance(a,b,c,d):
    return abs(c-a) + abs(d-b)

a, b, c, d = map(int, input().split())
md = manhattan_distance(a,b,c,d)
print(md)



