# link : https://codeforces.com/problemset/problem/1466/A
# author : Mohamed Ibrahim

t=int(input())
while(t):
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    x=[abs(i-j) for i in a for j in a if i!=j]
    ans=set(x)
    print(len(ans))
