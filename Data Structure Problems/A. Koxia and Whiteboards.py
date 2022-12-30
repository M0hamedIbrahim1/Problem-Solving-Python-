# link   : https://codeforces.com/contest/1770/problem/A
# author : Mohamed ibrahim


for _ in range(int(input())):
  n,m = map(int,input().split())
  lst_n = list(map(int,input().split()))
  lst_m = list(map(int,input().split()))
  for i in range(m):
    a = min(lst_n)
    indx = lst_n.index(a)
    lst_n[indx] = lst_m[i]
  print(sum(lst_n))

  
  
  
