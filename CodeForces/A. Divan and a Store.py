# link : https://codeforces.com/problemset/problem/1614/A
# author : Mohamed Ibrahim

t = int(input())
for _ in range(t):
  n, l, r, k = list(map(int,input().split()))
  a = list(map(int,input().split()))
  a.sort()
  s = 0
  for i in a:
    if i>=l and i <= r and i<=k:
      s+=1
      k-=i

  print(s)
