#link   : https://codeforces.com/problemset/problem/1341/A
#author : Mohamed Ibrahim
for _ in range(int(input())):
    n,a,b,c,d = map(int,input().split())
    if n*(a+b) < c-d or n * (a-b) > c+d:
        print("No")
    else:
        print("Yes")
