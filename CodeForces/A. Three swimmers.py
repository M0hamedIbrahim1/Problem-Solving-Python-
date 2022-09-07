# link   : https://codeforces.com/problemset/problem/1492/A
# author : Mohamed Ibrahim

t = int(input())
for i in range(t):
  p,a,b,c = map(int,input().split())
  print(min(-p%a,-p%b,-p%c))
