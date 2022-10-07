# link   : https://codeforces.com/problemset/problem/1669/E
# author : Mohamed Ibrahim


from collections import Counter as C
for _ in range(int(input())):
  n = int(input())
  l = []
  for j in range(n):
    l.append(input())
  d = C(l)
  cnt = 0
  for i in d:
    for k in d:
      if i != k and ( i[0] == k[0] or i[1] == k[1]):
        cnt += d[i]*d[k]
  print(cnt // 2)
  
  
  
