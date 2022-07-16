#link   : https://codeforces.com/problemset/problem/1420/A
#author : Mohamed Ibrahim

n=int(input())
for i in range(n):
    a,ai=input(),list(map(int,input().split()))
    b=sorted(ai,reverse=True)
    if ai!=b or len(b)>len(set(b)):print("YES")
    else:print("NO")
