# link   : https://codeforces.com/problemset/problem/1490/D
# author : Mohamed Ibrahim



def resc(index,lst):
  if not lst:
    return
  m = max(lst)
  i = lst.index(m)
  d[m] = index
  resc(index+1,lst[:i])
  resc(index+1,lst[i+1:])

for _ in range(int(input())):
  indx = int(input())
  lst = list(map(int,input().split()))
  d = dict()
  resc(0,lst)
  for j in lst:
    print(d[j],end =" ")
  print()
  
  
  
