#link   : https://codeforces.com/problemset/problem/1650/B
#author : Mohamed Ibrahim

t=int(input())
for _ in range(t):
    l,r,a=map(int,input().split())
    if r//a==l//a:
        print(r//a+r%a)
    else:
        print(max(r//a+r%a,r//a-1+a-1))
