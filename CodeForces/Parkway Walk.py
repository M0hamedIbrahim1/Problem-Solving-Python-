# link : https://codeforces.com/problemset/problem/1697/A
# author : Mohamed Ibrahim

T=int(input())
for i in range(0,T):
    n,m=map(int,input().split())
    print(max(0,sum(map(int,input().split()))-m))
