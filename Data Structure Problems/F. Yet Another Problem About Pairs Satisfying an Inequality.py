# Link   : https://codeforces.com/problemset/problem/1703/F
# Author : Mohamed Ibrahim


from bisect import bisect_left
for i in range(int(input())):
  s = int(input())
  lst = list(map(int,input().split()))
  l = []
  ans = 0
  for j in range(s):
    if lst[j] < j+1:
      l.append(j+1)
  for k in range(s):
    if lst[k] < k+1:
      ans += bisect_left(l,lst[k])
  print(ans)
  
  
  
  
