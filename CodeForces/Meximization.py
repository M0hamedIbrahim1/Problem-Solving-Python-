#link   : https://codeforces.com/problemset/problem/1497/A
#author : Mohamed Ibrahim

for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    for i in s:
        l.remove(i)
    l = list(s) + l
    print(*l)
