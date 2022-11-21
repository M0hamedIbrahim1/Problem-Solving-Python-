# link   : https://codeforces.com/problemset/problem/1566/D1
# author : Mohamed Ibrahim

for __ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(m):
        for j in range(i+1,m):
            if a[j]>a[i]:
                count+=1

    print(count)            


