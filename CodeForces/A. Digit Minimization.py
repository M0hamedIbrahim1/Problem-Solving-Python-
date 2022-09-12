# link   : https://codeforces.com/problemset/problem/1684/A
# author : Mohamed Ibrahim

n = int(input())
for i in range(n):
    x,y=map(int,input().split())
    print(2*max(x,y)-(x!=y))
