# link : https://codeforces.com/problemset/problem/1705/A
# author : Mohamed Ibrahim

for _ in range(int(input())):
  n,x=map(int,input().split())
  lst=list(map(int,input().split()))
  lst.sort()
  for i in range(n):
    if (lst[i]+x)>lst[(n)+i]:
      print("NO")
      break
  else:
    print("YES")
