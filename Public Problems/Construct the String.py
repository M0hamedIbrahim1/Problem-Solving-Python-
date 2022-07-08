#link   : https://codeforces.com/contest/1335/problem/B
#author : Mohamed Ibrahim
t = int(input())
for i in range(t):
    n,a,p = map(int,input().split())
    for j in range(n):
        print(chr(j%p + 97),end='')
    print('\n')
