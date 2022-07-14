#link   : https://codeforces.com/problemset/problem/1471/A
#author : Mohamed Ibrahim

import math as m
for _ in range(int(input())):
    n,x = map(int,input().split())
    lst = list(map(int,input().split()))
    print(m.ceil(sum(lst)/x) , sum([m.ceil(i/x) for i in lst]) )
    
