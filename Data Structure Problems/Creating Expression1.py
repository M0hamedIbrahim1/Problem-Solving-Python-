# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/V
# author : Mohamed ibrahim


n,c = map(int,input().split())
lst = list(map(int,input().split()))

def resc(indx,sum):
  if indx == n:
    return sum == c
  route1 = resc(indx+1,sum+lst[indx])
  route2 = resc(indx+1,sum-lst[indx])  
  return route1 or route2

if resc(1,lst[0]):
  print("YES")
else:
  print("NO")
  
  
