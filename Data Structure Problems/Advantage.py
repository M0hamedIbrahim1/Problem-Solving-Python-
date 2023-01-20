# link   : https://codeforces.com/problemset/problem/1760/C
# author : Mohamed Ibrahim


for _ in range(int(input())):
  n = int(input())
  lst = list(map(int,input().split()))
  s = sorted(lst,reverse=True)
  mx,sec_mx = s[0],s[1]
  for i in lst:
    if i == mx:
      print(i-sec_mx,end=' ')
    else:
      print(i-mx,end=' ')
  print()
  
  
  
