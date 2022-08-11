#link   : https://codeforces.com/problemset/problem/549/A
#author : Mohamed Ibrahim

n, m = map(int, input().split(' '))
p = [input() for i in range(n)]
r = 0
for i in range(n - 1):
    for j in range(m - 1):
        if {p[i][j], p[i+1][j], p[i][j+1], p[i+1][j+1]} == {'f','a','c','e'}:
            r = r + 1
print(r)
