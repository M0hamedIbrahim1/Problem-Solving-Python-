# link   : https://codeforces.com/contest/1760/problem/B
# author : Mohamed Ibrahim

for i in range(int(input())):
  input()
  s = input()
  l = []
  for i in s:
    l.append(ord(i)-97 + 1)
  print(max(l))
  
  
  
