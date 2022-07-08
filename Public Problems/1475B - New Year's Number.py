#link : https://codeforces.com/problemset/problem/1475/B
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
    n = int(input())
    print("YES" if n//2020 >= n%2020 else "NO")
