#link   : https://codeforces.com/problemset/problem/1675/B
#author : Mohamed Ibrahim

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    last = a[-1]
    c = 0
    for i in range(n-2, -1, -1):
        if last == 0:
            return -1
        while a[i] >= last:
            a[i] = a[i]//2
            c += 1
        last = a[i]
    return c
    
T = int(input())
for i in range(T):
    print(solve())
    
