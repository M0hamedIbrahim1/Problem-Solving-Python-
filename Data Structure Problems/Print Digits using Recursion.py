# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/D
# author : Mohamed Ibrahim


def resc(s,l):
  if l == le-1:
    print(s[l])
    return 1
  print(s[l],'',end='')
  resc(s,l+1)
 
for _ in range(int(input())):
  s = input()
  le = int(len(s))
  resc(s,0)
  
  
  
