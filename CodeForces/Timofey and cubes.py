#link   : https://codeforces.com/problemset/problem/764/B
#author : Mohamed Ibrahim
n = int(input())

a = list(map(int,input().split()))
 
for i in range(0,n//2,2):
    a[i],a[n-i-1] = a[n-i-1],a[i]
print(*a)
