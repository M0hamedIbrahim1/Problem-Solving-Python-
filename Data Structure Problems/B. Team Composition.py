# link   : https://codeforces.com/problemset/problem/1611/B
# author : Mohamed Ibrahim


for _ in range(int(input())):
  a,b = map(int,input().split())
  print(min(min(a,b),(a+b )// 4))
  
  
