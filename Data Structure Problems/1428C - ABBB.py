# link   : https://codeforces.com/problemset/problem/1428/C
# author : Mohamed Ibrahim


for i in range(int(input())):
  s = input()
  ans = 0
  for j in s:
    if j == 'B' and ans != 0:
      ans-=1
    else:
      ans+=1
  print(ans)
  
  
