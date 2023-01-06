# Link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/Y
# author : Mohamed Ibrahim

def resc(num,target):
  if num>target:
    return 0
  if num == target:
    return 1
  return resc(num+1,target)+resc(num+2,target)+resc(num+3,target)


n,t = map(int,input().split())
print(resc(n,t))

