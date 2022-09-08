#link : https://codeforces.com/problemset/problem/1629/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    l, r, k = map(int, input().split())
    d = (r + 1) // 2 - l // 2
    print("YES" if k >= d or l == r != 1 else "NO")
