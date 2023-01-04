# link  : https://codeforces.com/problemset/problem/383/A
#author : Mohamed Ibrahim


n = int(input())
lst = list(map(int,input().split()))
res,s = 0,0
for i in lst:
  if i == 0:
    res+=s
  else:
    s+=1
print(res)




