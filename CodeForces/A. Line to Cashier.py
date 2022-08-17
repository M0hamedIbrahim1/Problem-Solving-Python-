#link   : https://codeforces.com/problemset/problem/408/A
#author : Mohamed Ibrahim

n=int(input())
ans=1000005
l=list(map(int,input().split()))
for i in range(n):
    ans=min(ans,sum(map(int,input().split()))*5+l[i]*15)
print(ans)
