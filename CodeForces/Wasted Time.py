#link   : https://codeforces.com/problemset/problem/127/A
#author : Mohamed Ibrahim

n,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
t=0
for i in range(1,n):
    t+=(((l[i-1][0]-l[i][0])**2)+((l[i-1][1]-l[i][1])**2))**0.5
print(t*(k/50))
