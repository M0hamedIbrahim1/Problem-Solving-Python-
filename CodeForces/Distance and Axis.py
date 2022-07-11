#Link   : https://codeforces.com/problemset/problem/1401/A
#author : Mohamed Ibrahim
for i in range(int(input())):
    a,b=map(int,input().split())
    print(b-a if b>a else (a - b) % 2)
