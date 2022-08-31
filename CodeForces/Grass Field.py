#link   : https://codeforces.com/problemset/problem/1701/A
#author : Mohamed Ibrahim

for x in range(int(input())) : 
  a=input()
  b=input()
  s=0
  s+=a.count('1')
  s+=b.count('1')
  if s==0 : print(0)
  elif s==4 : print(2)
  else:print(1)
    
