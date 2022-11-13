# link   : https://codeforces.com/problemset/problem/1730/A
# author : Mohamed Ibrahim

from collections import Counter
for _ in range(int(input())):
  n,m = map(int,input().split())
  lst = list(map(int,input().split()))
  a = Counter(lst)
  s = 0
  for i in a.values():
    s+=min(m,i)
  print(s)
  
  
  
