#link   : https://codeforces.com/problemset/problem/755/B
#author : Mohamed Ibrahim

n,m=map(int,input().split())
x=[]
for i in range(n+m):
    x.append(input())
if n>m: print('YES')
elif n<m: print('NO')
elif n==m:
    if len(set(x))%2!=0: print('YES')
    else: print('NO')


