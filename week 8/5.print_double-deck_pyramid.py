# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:21:19 2021

@author: nolan

 

Descripition：
Output double-deck Pyramid.

Iutput：
Multiple test data, each of which is entered with an integer n( 2 <= n <= 9). Multiple inputs ended by entering EOF (Ctrl+D on Mac, Ctrl-Z on Win)

Output：
One double-deck pyramid for each input

 

Sample input：
2
5
 

Sample output：
 *
***
 *
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
 

Note：
Use while (cin>>n) to keep receiving input until EOF is entered.

 
"""



def print_pyramid(k):
    z = ""
    for i in range(1, k+1):
        z = (k-i)*" "
        print(z + (2*i-1)*"*")
    for j in range(1, k):
        z = j*" "
        print(z + (2*(k-j)-1)*"*")
        
while True:
    k = int(input())
    print_pyramid(k)