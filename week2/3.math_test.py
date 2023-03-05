# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:06:44 2021

@author: nolan

Maoge encountered a problem in his math test that he thought was very difficult.
It was a piecewise function problem.

The function is defined as below:

Given an x, please calucate y. 

Maoge couldn't do anything about it, so he had to ask you for help.


[Data Format]

Enter an integer x (0<=x<=20).


Output a floating-point y, representing the function answer, retaining two decimal places.


Sample input:

3

Sample output:

 10.00
 
"""

x = float(input())

if x<2:
    y = x
elif 2 <= x and x < 6:
    y = x**2 + 1
elif 6 <= x and x < 10:
    y = (x+1)**0.5
elif 10 <= x:
    y = 1/(x+1)

print('%.2f'%y)