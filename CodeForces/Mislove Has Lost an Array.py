#link   : https://codeforces.com/problemset/problem/1204/B
#author : Mohamed Ibrahim

[n,l,r]=list(map(int,input().split()))
print(2**l-1+n-l," ",2**r-1+(n-r)*2**(r-1))
