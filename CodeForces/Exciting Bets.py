#link   : https://codeforces.com/problemset/problem/1543/A
#author : Mohamed Ibrahim

for i in range(int(input())):
    n,k=map(int,input().split())
    a=abs(n-k)
    if(a==0):
        print(0,0)
    else:
        print(a,min(n%a,a-n%a))
