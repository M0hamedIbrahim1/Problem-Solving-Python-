#link   : https://codeforces.com/problemset/problem/1481/A
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
  x,y = map(int,input().split())
  s = input()
  if -s.count("D") <= y <= s.count("U") and -s.count("L") <= x <= s.count("R"):print("YES")
  else:print("NO")
    
