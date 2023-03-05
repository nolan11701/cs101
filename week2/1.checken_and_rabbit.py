"""
Chicken and rabbit in one cage

Chicken and rabbit in one cage: several chickens and several rabbits are kept in the same cage.

There are x heads, and y feets. How many chickens and rabbits there are ?

Sample input:
40 100

Sample output:
30
10

"""

heads, legs = map(int, input().split())
a = heads * 2
b = legs - a
y = int(b/2)
x = heads - y
print(x)
print(y)