#link   : https://codeforces.com/problemset/problem/1627/A
#author : Mohamed Ibrahim

for t in range(int(input())):
    n, m, r, c = map(int, input().split())
    a = [list(input()) for i in range(n)]
    if "B" not in str(a):
        print(-1)
        continue
    print(2 - ("B" in a[r-1] + list([*zip(*a)][c-1])) - (a[r-1][c-1] == 'B'))
    
