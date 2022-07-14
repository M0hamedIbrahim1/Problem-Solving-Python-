#link   : https://codeforces.com/problemset/problem/1471/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
    N,x = map(int,input().split())
    A = list(map(int,input().strip().split()))
    print((sum(A) + x - 1) // x, sum([(i + x - 1) // x for i in A]))
