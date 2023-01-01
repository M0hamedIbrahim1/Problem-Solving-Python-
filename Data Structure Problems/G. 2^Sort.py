# link   : https://codeforces.com/problemset/problem/1692/G
# author : Mohamed Ibrahim


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    ans = 0
    for i in range(n-1):
        if a[i] < 2*a[i+1]:
            c += 1
        else:
            c = 0
        if c >= k:
            ans += 1
    print(ans)



