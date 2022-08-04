#link  : https://codeforces.com/problemset/problem/496/A
author : Mohamed Ibrahim

n=int(input())
l=list(map(int,input().split()))
x=max([l[i+1]-l[i] for i in range(n-1)])
y=min([l[i+2]-l[i] for i in range(n-2)])
print(max(x,y))
