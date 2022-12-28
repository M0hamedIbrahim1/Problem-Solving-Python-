# link   : https://codeforces.com/problemset/problem/1100/B
# author : Mohamed Ibrahim


m,n = map(int,input().split())
lst = list(map(int,input().split()))
x , y = [0]*(m+1),[0]*(n+1)
for i in lst:
  x[i] += 1
  y[x[i]] += 1 
  if y[x[i]] == m:
    print('1',end='')
  else:
    print('0',end='')
    
    
