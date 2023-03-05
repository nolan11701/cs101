'''
Hundred chicken problem
English 

Hundred chicken problem: a cock worth 5 yuan, a hen worth 3 yuan
, and 1 yuan can buy 3 chickens. buy x chickenwith x yuan ,
ask the numbers of cocks, hens, and chicken?

Sample input:
100


Sample output:
0 25 75
4 18 78
8 11 81
12 4 84


time limit:
1000

memory limit:
65536

'''

x = int(input())

list_a = list(range(x//5 + 1))
list_b = list(range(x//3 + 1))
list_c = list(range(3*x + 1))

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a*5 + b*3 + c/3 == x and a+b+c == x:
                print(a,b,c)

