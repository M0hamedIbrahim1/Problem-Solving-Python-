# link   : https://codeforces.com/problemset/problem/1364/A
# author : Mohamed Ibrahim


t = int(input())
for k in range(t):
  n,x = map(int,input().split())
  lst = list(map(int,input().split()))
  m = -1
  sum = 0
  for i in range(n):
    sum+=lst[i]
    if(sum % x):
      m = max(m,max(len(lst)-(i+1),i+1))
  print(m)
