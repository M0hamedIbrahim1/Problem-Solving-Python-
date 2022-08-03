#link   : https://codeforces.com/problemset/problem/1295/A
#author : Mohamed Ibrahim

T = int(input())
for i in range(T):
    n = input()
    ans = 0
    lst = list(map(int, input().split())) + [0]
    prev = 0
    for x in lst:
        if not x and prev:
            ans = ans + 1
        prev = x
    print(min(2, ans))
