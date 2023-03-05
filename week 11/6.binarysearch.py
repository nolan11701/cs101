# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:58:31 2021

@author: nolan
"""

   
 
# def binary_search(t, a, low, high):
    
#     if (a[low] == t):
#         return low+1
    
#     if (low >= high):
#         return 0
        
#     p = 0
#     c = (high + low) // 2
    
#     if a[c] >= t :
#         # find from low
#         p = binary_search(t, a, low, c)
#     else:
#         # find from right
#         p = binary_search(t, a, c+1, t) 

#     return p

n, t = map(int, input().split())
a = list(map(int, input().split()))     

def binary_search(t, a, low, high):
    
    while (high > low):
        mid = (low + high) // 2
        
        if (a[mid] >= t): 
            high = mid
        elif (a[mid] < t):
            low = mid +1
     
    if (a[low] == t):
        return low +1
    return 0

p = binary_search(t, a, 0, len(a)-1)
print(p)