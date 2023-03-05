# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:37:16 2021

@author: nolan

Description
Input n numbers. Compare two adjacent numbers, if the former is smaller, then swap them, so that you can bubble the largest number to the end of sequence. Repeat until all the number in sequence s is in order. Output it from small to big. 

Input
One integer N.

The second line contains N numbers.  1<=N<=1000 0<=ai<=109  


Output
N integers.

Sample Input
5
1 4 2 3 5
Sample Output
1 2 3 4 5

"""

n = int(input())
m = list(map(int, input().split()))
 
for i in range(n):
    for j in range(n-i-1):
        if m[j] > m[j+1]:
            m[j], m[j+1] = m[j+1], m[j]
 
print(*m)