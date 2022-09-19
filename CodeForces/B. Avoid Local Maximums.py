# link : https://codeforces.com/problemset/problem/1635/B
# author : Mohamed Ibrahim

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    max_m = max(a)
    for i in range(1, n-1):
        if a[i-1] < a[i] > a[i+1]:
            a[i+1] = (a[i] if i+2 >= n else max(a[i], a[i+2]))
            k += 1
    print(k)
    print(*a)
    
