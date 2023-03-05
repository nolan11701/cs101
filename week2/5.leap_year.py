# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:18:48 2021

@author: nolan

Description
Determine whether a number is a leap year.

 

Input

An integer n. 1<=n<=2018

 

Output
If the number is leap year,ouput "yes",else,ouput "no".

 

Sample Input1
2000 
 

Sample Output1
yes
Sample Input2
1900 
 

Sample Output2
no

"""

x = int(input())

if x%4 != 0:
    print("no")
elif x%400 == 0 :
    print("yes")
elif x%100 == 0 :
    print("no")
else:
    print("yes")