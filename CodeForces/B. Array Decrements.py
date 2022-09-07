# link   : https://codeforces.com/problemset/problem/1690/B
# author : Mohamed Ibrahim

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m = 0;
    for i in range(n):
        m = max(m,a[i]-b[i])
    for i in range(n):
        a[i] = max(a[i]-m,0)
    print("YES" if a == b else "NO")
