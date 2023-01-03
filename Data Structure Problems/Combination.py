# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/T
# author : Mohamed Ibrahim


def fact(n):
  if n<= 0:
    return 1
  return n*fact(n-1)
def com(x,y):
  z = fact(x-y)
  x_new = fact(x)
  y_new = fact(y)
  return x_new // (y_new * z)

n,r = map(int,input().split())
print(com(n,r))

