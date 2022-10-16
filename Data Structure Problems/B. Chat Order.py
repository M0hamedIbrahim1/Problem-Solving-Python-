# link   : https://codeforces.com/problemset/problem/637/B
# author : Mohamed Ibrahim



s = set()
l = list()
n = int(input())
for _ in range(n):
  l.append(input())
for i in range(n-1,-1,-1):
  if l[i] not in s:
    s.add(l[i])
    print(l[i])
    
    
    
    
 
