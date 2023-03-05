
"""
Created on Sun Sep 19 20:38:46 2021

@author: nolan

There are four coins on Maoge's desk, some facing up, some facing down. 
Now Maoge wants to ask you to help him turn these coins into the same side, but you can and only can flip three coins at a time. 
Please find out the minimum number of flips.

[Data Format]

Enter a line with four digits of 0/1 to indicate the initial state of each coin.

Output a number to indicate the answer.

Sample input:
1 0 1 1

Sample output:
1

"""

a, b, c, d = map(int, input().split())

if a == b and b == c and c == d:
    print("0")
elif a + b + c + d == 2:
    print("2")
else:
    print("1")