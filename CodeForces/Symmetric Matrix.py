#link   : https://codeforces.com/problemset/problem/1426/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    s="NO"
    n,m=map(int,input().split())
    for i in range(n):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if(b==c and m%2==0):
            s="YES"
    print(s)
