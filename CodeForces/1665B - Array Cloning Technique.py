#link   : https://codeforces.com/problemset/problem/1665/B
#author : Mohamed Ibrahim

from collections import Counter


for _ in range(int(input())):
    n = int(input())
    w = input().split()
    s = max(Counter(w).values())

    a = n-s
    while s < n:
        a += 1
        s *= 2
    print(a)
