#link   : https://codeforces.com/problemset/problem/1678/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if 0 not in arr and len(set(arr))==n:
        print(n+1)
    else :
        print(n-arr.count(0))
        
