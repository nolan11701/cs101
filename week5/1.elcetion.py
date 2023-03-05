# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:11:40 2021

@author: nolan

Description

In an election for the leader of the class, there are three candidates, A, B, and C.  In counting number of votes for each candidate, 1 stands for one vote for A, 2 stands for one vote for B, and 3 stands for one vote for C. The voting ends with -1. Please count the voting for the election and show the results with the following format.

A=number of votes for A 

B=number of votes for B

C=number of votes for C

Tot=number of total votes

A-yes

The last line shows the leader, who wins more than half of the ballots out of A, B, C, such as "A-yes" means A is the monitor. If no one wins more than half of the ballots out of A, B, C, output "all-NO".

 

Input

Input one line, a number of integers, and end with -1.

Output

Five lines showing the election results. Please see the format above in the problem description.

 

Sample Input

1 1 3 2 1 3 2 1 3 3 1 2 4 1 4 1 2 1 2 1 1 -1

Sample Output

A=10 

B=5 

C=4 

Tot=19 

A-yes
"""

v = list(map(int, input().split()))
a = 0
b = 0
c = 0

for i in v:
    if i == 1:
        a += 1
    elif i == 2:
        b += 1
    elif i == 3:
        c += 1
        
print("A="+str(a))
print("B="+str(b))
print("C="+str(c))
print("Tot="+str(a+b+c))

if a>(a+b+c)/2:
    print("A-yes")
elif b>(a+b+c)/2:
    print("B-yes")
elif c>(a+b+c)/2:
    print("C-yes")
else:
    print("all-NO")