#link : https://codeforces.com/problemset/problem/1440/B
#author : Mohamed Ibrahim

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    ali = list(map(int, input().split()))
    q = (n // 2) + 1
    mdn = ali[-q::-q]
    print(sum(mdn[:k]))
