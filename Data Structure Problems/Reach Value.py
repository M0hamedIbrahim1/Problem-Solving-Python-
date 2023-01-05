# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/W
# author : Mohamed Ibrahim

def resc(target,n):
  if n == target:
    return 1
  if n > target:
    return 0
  return resc(target,n*10) or resc(target,n*20)

for _ in range(int(input())):
  T = int(input())
  if resc(T,1): print("YES")
  else:print("NO")
  
  
  
  
