# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/F
# author : Mohamed Ibrahim


def resc(lst,n):
  if n < 0:
    return 0
  print(lst[n],' ',end = '')
  resc(lst,n-2)

n = int(input())
if n % 2 == 0:
  n-=2
else:
  n-=1
lst = list(map(int,input().split()))  
resc(lst,n)


