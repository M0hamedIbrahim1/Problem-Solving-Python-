#link : https://codeforces.com/problemset/problem/1657/B
#author : Mohamed Ibrahim

import math
t=int(input())
 
for _ in range(t):
  n,B,x,y=map(int,input().split())
  ans=0
  a=0
  for _ in range(n):
    if(a+x<=B):
      a=a+x
    else:
      a=a-y
    ans=ans+a
  print(ans)
 
