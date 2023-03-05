"""
Created on Sun Sep 19 19:55:59 2021
@author: nolan

Logic calculation 2

Description

We define a number as "good" only if satisfies one of the two following conditions: 

1. The number is a multiple of 5.

2. The number is a multiple of 3 and the number is less than or equal to 20

Determine if a gien number is a good number, and output "YES" or "NO".
 

Input
A number n

Output 

The output format is described in the problem description.

Sample input 1

10
Sample output 1

YES
 
Sample input 2
21
Sample output 2
NO
 

Constraints
0 <= n <= 100
"""

a = int(input())

if (a%5 == 0) or (a%3 == 0 and a <= 20):
    print("YES")
else:
    print("NO")
