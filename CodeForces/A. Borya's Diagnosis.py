#link   : https://codeforces.com/problemset/problem/879/A
#author : Mohamed Ibrahim

n=int(input())
x=0
for i in range(n):
    s,d=map(int,input().split())
    if s>x:
        x=s
    else:
        x=x-(x-s)%d+d
print(x)
