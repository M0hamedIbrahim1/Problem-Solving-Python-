# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/X
# Author : Mohamed Ibrahim

def resc(i,j):
  if i == n-1 and j == m-1:
    return lst[i][j]
  if i == n or j == m:
      return -100000000

  return max(resc(i+1,j)+lst[i][j],resc(i,j+1)+lst[i][j])

n,m = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,input().split())))
print(resc(0,0))


