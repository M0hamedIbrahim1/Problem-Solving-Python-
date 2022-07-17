#link   : https://codeforces.com/problemset/problem/588/A
#author : Mohamed Ibrahim

T = int(input())
Min,ans = 101,0
for i in range(T):   
    m,p = map(int,input().split())
    Min = min(p,Min)
    ans+=Min*m
print(ans)
