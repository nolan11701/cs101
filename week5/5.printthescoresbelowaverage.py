# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:30:52 2021

@author: nolan

Description
Enter n scores and print out all scores below average

 

Input

Multiple test data set, finished by entering end-of-file, a.k.a., EOF (CTRL-D on Mac, CTRL-Z on Windows). In each line, enter integer n and then n scores. Please note that you can assume 1<=n<=100.
 

Output
For each line of test data, output all the scores below the average in the input order, separated with one space.If nothing is below the average then output an empty line.

 
Sample Input
3 40 50 60

2 90 80

5 10 10 90 80 80

 
Sample Output
40

80

10 10

 

Hint

Use while (cin >> n) to loop till end of file is entered.
"""

while True:
    n = list(map(int, input().split()))

    m = n[1:len(n)]

    me = sum(m)/len(m)

    for i in m:
        if me > i:
            print(i, end = ' ')
        