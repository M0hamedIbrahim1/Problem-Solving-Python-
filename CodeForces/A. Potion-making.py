#link   : https://codeforces.com/problemset/problem/1525/A
#author : Mohamed Ibrahim

from math import gcd
for _ in range(int(input())):
    print(100//gcd(int(input()), 100))
    
