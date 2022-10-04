# link   : https://codeforces.com/problemset/problem/961/B
# author : Mohamed Ibrahim

n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
p = 0
for i in range(n):
    if t[i] == 1:
        p += a[i]
        a[i] = 0
ans = s = sum(a[:k])
for i in range(0, n-k):
    s = s + a[i+k] - a[i]
    ans = max(ans,s)
print(ans + p)


