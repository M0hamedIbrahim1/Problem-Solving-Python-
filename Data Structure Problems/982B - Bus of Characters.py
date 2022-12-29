# link : https://codeforces.com/problemset/problem/982/B
# author : Mohamed Ibrahim 



n = int(input())
lst_width = list(map(int,input().split()))
for i in range(n):
  lst_width[i] = [lst_width[i],i+1]
lst_width.sort()
ans = [0]* (2*n)
store = []
i,k = 0,0

for s in input():
  if s == '0':
    ans[k] = lst_width[i][1]
    store.append(lst_width[i][1])
    i+=1
  else:
    ans[k] = store[-1]
    store.pop()
    
  k+=1
print(*ans)

