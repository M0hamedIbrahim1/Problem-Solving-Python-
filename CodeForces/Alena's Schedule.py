#link : https://codeforces.com/problemset/problem/586/A
#author : Mohamed Ibrahim

n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
    if(a[i-1] and a[i+1]):
        a[i]=1
print(sum(a))
