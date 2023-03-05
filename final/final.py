# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:59:49 2021

@author: nolan
"""
# 1

# x = int(input())
# y = x//10
# z = y%10
# print(z)

# 2

# x, y, z = map(int, input().split())
# a = x*y*z
# b = 2*(x*y + x*z + y*z)
# print(b, a)

# 3

# m, n = map(int, input().split())
# a = [[0]*n for i in range(m)]
# b = [[0]*m for i in range(n)]

# for i in range(m):
#     c = list(map(int, input().split()))
#     a[i] = c

# for i in range(n):
#     for j in range(m):
#         b[i][j] = a[j][i]

# for i in b:
#     print(sum(i))        
        
# 4

# x = int(input())
# y = 10 - x%10
# if x%10 >= 5:
#     x+=y
#     print(x)
# elif 5 > x%10:
#     print(x-(x%10))

# 5

# a, b, c = map(str, input().split())
# d = a.replace(b, c)
# print(d)

# 6

# x = int(input())
# y = list(map(int, input().split()))
# x = len(y)
# s = []
# for i in range(x-1):
#     if y[i] == y[i+1]:
#         s.append(0)
#     s.append((max(y[i], y[i+1])) - min(y[i], y[i+1]))
# s.sort()

# if s[i-1] == s[i]-1:
#     ismagical * True
# else:
#     ismagical * False
    
 