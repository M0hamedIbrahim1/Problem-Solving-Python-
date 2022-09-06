#link   : https://codeforces.com/problemset/problem/519/B
#author : Mohamed Ibrahim

n,a,b,c = [sum(map(int,input().split())) for _ in ' '*4];
print(a-b,b-c)
