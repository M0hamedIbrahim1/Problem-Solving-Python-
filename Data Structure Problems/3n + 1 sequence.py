# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/Q
# author : Mohamed Ibrahim 


def resc(n,c):
  if n == 1:
    return c
  elif n%2 == 0:
    c+=1
    return resc(n/2,c)
  else:
    c+=1
    return resc(3*n + 1,c)

n = int(input())
print(resc(n,1))


