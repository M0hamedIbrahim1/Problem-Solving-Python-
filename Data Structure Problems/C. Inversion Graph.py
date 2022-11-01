# link : https://codeforces.com/problemset/problem/1638/C
# author : Mohamed Ibrahim



for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    ma=l[0]
    co=0
    for i in range(n):
        if l[i]>ma:
            ma=l[i]
        if ma==i+1:
            co+=1
    print(co)
    
    
    
