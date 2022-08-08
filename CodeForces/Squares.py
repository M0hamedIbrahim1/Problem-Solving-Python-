# link   : https://codeforces.com/problemset/problem/263/B
# author : Mohamed Ibrahim

n,k=map(int,input().split())
r=sorted(map(int,input().split()),reverse=True)
if k>n:print(-1)
if k<=n:print(r[k-1],r[k-1])
  
