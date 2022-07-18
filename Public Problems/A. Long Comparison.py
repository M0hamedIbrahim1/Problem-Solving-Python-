#link   : https://codeforces.com/problemset/problem/1613/A
#author : Mohamed Ibrahim

from math import *
for _ in range(int(input())):
    x1, p1 = map(int,input().split())
    x2, p2 = map(int,input().split())
    l = log10(x1/x2) + p1 - p2
    if l == 0:
        print("=")
    else:
        print(">" if l > 0 else "<")
