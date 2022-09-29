# link   : https://codeforces.com/problemset/problem/1520/D
# author : Mohamed Ibrahim

t = int(input())
for j in range(t):
  n = int(input())
  lst = list(map(int,input().split()))
  d = {}
  res = 0
  for i in range(n):
    lst[i] -= i + 1
    res+= d.get(lst[i],0)
    d[lst[i]] = d.get(lst[i],0) + 1
  print(res)
