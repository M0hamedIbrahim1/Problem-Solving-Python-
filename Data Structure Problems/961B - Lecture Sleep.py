# link   : https://codeforces.com/problemset/problem/961/B
# author : Mohamed Ibrahim



k,n = map(int,input().split())
lst = list(map(int,input().split()))
lstt = list(map(int,input().split()))
mx,ans = -1,0
for i in range(k):
  if lstt[i] == 1:
    ans+=lst[i]
    lst[i] = 0
s = sum(lst[:n])
mx = s
for i in range(k-n):
  s-=lst[i]
  s+=lst[i+n]
  mx = max(mx,s) 

print(mx+ans)






