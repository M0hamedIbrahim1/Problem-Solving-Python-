#link   : https://codeforces.com/problemset/problem/1689/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(-1)
        continue
    x = sorted(a)
    for i in range(n - 1):
        if x[i] == a[i]:
            x[i], x[i+1] = x[i+1], x[i]
    if x[n-1] == a[n-1]:
        x[n-2], x[n-1] = x[n-1], x[n-2]
 
    print(*x)
  
