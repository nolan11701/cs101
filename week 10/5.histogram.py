# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:01:52 2021

@author: nolan
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
q = 26*[0]

for i in range(4):
    x = input()
    for j in range(len(letters)):
        q[j] += x.count(letters[j])
        

def print_zero_one_list(alist):
    y = []
    for i in alist:
        if i == 0:
            y.append(' ')
        elif i == 1:
            y.append('*')
    print(' '.join(y))
    
def process_list(ql):
    
    # find the greatest item oftmost significance corresponding to the array of values
    maxx = max(ql)
    results = []
    # produce a loop corresponding with the range of the maximum value of the array
    for i in range(maxx):
        t = [0]*26
        for j in range(len(ql)):
            if ql[j] == maxx:
                ql[j] -= 1
                t[j] = 1
            else:






















































































































































































































































































































                t[j] = 0
        
        # remove 0s from the tail end

        while t[len(t)-1] != 1:
            t.pop(len(t)-1)

        results.append(t)
        maxx = max(ql)
    return results

    
def print_a_to_z():
    print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

dmatrix = process_list(q)
for i in dmatrix:
    print_zero_one_list(i)
print_a_to_z()
