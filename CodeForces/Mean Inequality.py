#link   : https://codeforces.com/problemset/problem/1526/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(n):
        print(a[i], a[n + i], end=" ")
        
