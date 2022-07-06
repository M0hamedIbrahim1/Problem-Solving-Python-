#link   : https://codeforces.com/problemset/problem/1529/A 
#author : Mohamed Ibrahim

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=l.count(min(l))
    print(n-c)
    
