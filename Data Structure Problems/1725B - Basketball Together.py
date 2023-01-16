# link   : https://codeforces.com/problemset/problem/1725/B
# author : Mohamed Ibrahim



n , s = map(int,input().split())
lst = list(map(int,input().split()))
i,j = 0 ,n-1
lst.sort()
cnt ,sum = 0,lst[j]
while i<=j:
  while sum <= s and i<j:
    sum+=lst[j]
    i+=1
  if sum > s :cnt+=1
  j-=1
  sum = lst[j]
print(cnt)


