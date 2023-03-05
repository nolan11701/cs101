# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:45:13 2021

@author: nolan

Description：

Xiaoming loves collecting cards. But as he collects more cards, he began to worry because he always forgets the attack power of certain cards. He finds it troublesome to look for cards each time, and wonder if the computer can do some help. He numbered every card and inform the computer the attack power of each card. In this case, when he forgets about certain cards, he can rely on the computer to tell him. Can you help him to achieve this function?

Input：  

The first line contains two integers n and m. n represents the total number of cards (numbered from 1 to n). m means number of inquiry times.

The second line contains n integers, representing the attack power of cards (numbered from 1 to n) respectively.

The third line contains m integers, t1,t2,t3,...,tm，integer ti means asking the attack power of the card numbered ti.

Output：

A single line containing m integers, representing the attack power of the cards asked for m times.

Sample input：

5 3
8 3 5 1 9
3 2 5
Sample output：

5 3 9
 

Note：

1≤m≤n≤100

The attack power of the third card is 5. The attack power of the second card is 3. The attack power of the fifth card is 9. 

"""

m, n = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in s:
    print(p[i-1], end = " ")

