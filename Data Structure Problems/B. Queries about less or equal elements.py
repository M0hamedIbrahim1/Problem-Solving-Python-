# link   : https://codeforces.com/problemset/problem/600/B
# author : Mohamed Ibrahim


import bisect
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
for i in b:
  print(bisect.bisect(a,i),end=" ")
  
  
  
