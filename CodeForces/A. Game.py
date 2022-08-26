#link   : https://codeforces.com/problemset/problem/984/A
#author : Mohamed Ibrahim

n=int(input())
print(sorted(list(map(int, input().split())))[(n-1)//2])

