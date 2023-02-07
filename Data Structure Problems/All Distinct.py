# link   : https://codeforces.com/problemset/problem/1692/B
# author : Mohameed Ibrahim

for _ in range(int(input())):
  n=int(input())
  a=len(set(map(int,input().split())))
  if n%2==a%2:print(a)
  else:print(a-1)
    
    
    
