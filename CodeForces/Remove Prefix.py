#link   : https://codeforces.com/problemset/problem/1714/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=set()
    for i in range(n-1,-1,-1):
        if a[i] in b:
            break
        b.add(a[i])
    print(n-len(b))
