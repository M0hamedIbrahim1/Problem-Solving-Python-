#link   : https://codeforces.com/problemset/problem/1462/C
#author : Mohamed Ibrahim

for _ in range(int(input())):
    s=''
    n=int(input())
    for i in range(9,0,-1):
        if n>=i:
            n-=i
            s=str(i)+s
    print(s if n==0 else -1)
