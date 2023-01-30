# link   : https://codeforces.com/contest/1646/problem/B
# author : Mohamed Ibrahim



for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  l.sort()
  if n%2 == 0:
    if sum(l[:n//2]) < sum(l[n//2+1:]): print("YES")
    else: print("NO")
  else:
    if sum(l[:n//2+1]) < sum(l[n//2+1:]): print("YES")
    else: print("NO")
    
    
    
