
# link   : https://codeforces.com/problemset/problem/701/B
# author : Mohamed Ibrahim



n , m = map(int,input().split())
r = set()
c = set()
for _ in range(m):
  R,C = map(int,input().split())
  r.add(R)
  c.add(C)
  print( (n - len(r)) * (n - len(c)))
  
  
  
  
