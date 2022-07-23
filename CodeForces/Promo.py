#Link : https://codeforces.com/problemset/problem/1697/B
#author : Mohamed Ibrahim

n,q=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
b=[0]
for i in range(n):
    b.append(l[i]+b[i])
for i in range(q):
    x,y=map(int,input().split())
    print(b[x]-b[x-y])
