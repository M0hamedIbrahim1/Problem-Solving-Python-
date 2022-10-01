# link   : https://codeforces.com/problemset/problem/1006/C
# author : Mohamed Ibrahim

n = int(input())
lst = list(map(int,input().split()))
i , j = 0 , len(lst) - 1
left , right = 0 , 0
ans = 0
while i <= j:
  if left < right:
    left+=lst[i]
    i+=1
  else:
    right+=lst[j]
    j-=1
  if left == right:
    ans = max(ans,left)
print(ans)


