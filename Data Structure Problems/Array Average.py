# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/S
# author : Mohamed Ibrahim


def resc(lst,sum):
  if len(lst) == 0:
    return sum
  sum += lst[0]
  return resc(lst[1:],sum)
 
n = int(input())
lst =list(map(int,input().split()))
print(resc(lst,0)/n) 


