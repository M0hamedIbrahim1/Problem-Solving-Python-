#link : https://codeforces.com/problemset/problem/1517/A
#author : Mohamed Ibrahim

for i in [int(input()) for _ in range(int(input()))]:
    print(-1 if i % 2050 != 0 else sum((int(j) for j in str(i//2050))))
