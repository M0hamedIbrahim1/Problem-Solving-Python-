#Link : https://codeforces.com/problemset/problem/768/A
#author : Mohamed Ibrahim

n = int(input())
l = list(map(int, input().split()))
print(max(n - l.count(max(l)) - l.count(min(l)), 0))
