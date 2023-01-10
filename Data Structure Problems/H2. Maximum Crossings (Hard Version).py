# link   : https://codeforces.com/problemset/problem/1676/H2
# author : Mohamed Ibrahim



from bisect import bisect

for tcase in range(int(input())):

    n = int(input())
    a, b = [], []
    ans = 0

    for x in map(int, input().split()):

        ans += len(a) - bisect(a, x-1)
        ans += len([y for y in b if y >= x])
        b.append(x)

        if len(b) * len(b) > len(a):
            a.extend(b)
            b = []
            a.sort()

    print(ans)


