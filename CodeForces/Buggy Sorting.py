#link   : https://codeforces.com/problemset/problem/246/A
#author : Mohamed Ibrahim

n=int(input())
if n<3:
    print(-1)
else:
    print(*range(n,0,-1))
