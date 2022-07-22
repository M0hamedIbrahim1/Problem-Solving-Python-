#Link : https://codeforces.com/problemset/problem/1436/B
#author : Mohamed Ibrahim

T = int(input())
for i in range(T):
    n = int(input())
    for j in range(n):
        lst = [0]*n
        lst[j] = 1
        lst[(j+1)%n] = 4
        print(*lst)
