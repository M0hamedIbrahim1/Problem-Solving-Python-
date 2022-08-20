#link   : https://codeforces.com/problemset/problem/1690/C
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    f=[b[0]-a[0]]
    for i in range(1,n):
        f.append(b[i]-max(b[i-1],a[i]))
    print(*f)
    
