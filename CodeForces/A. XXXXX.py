# link   : https://codeforces.com/problemset/problem/1364/A
# author : Mohamed Ibrahim


for _ in range(int(input())):
   n,x = map(int,input().split())
   a = list(map(int,input().split()))
   ans = -1
   sum = 0
   for i in range(len(a)):
      sum += a[i]
      if sum % x:
         ans = max(ans, max(len(a) - i - 1, i + 1))
   print(ans)
   
    
