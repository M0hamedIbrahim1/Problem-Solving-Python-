#link : https://codeforces.com/problemset/problem/1642/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n=int(input())
    a=set(list(map(int,input().split())))
    b=len(a)
    for i in range(1,n+1):
        print(max(i,b),end=' ')
    print()
