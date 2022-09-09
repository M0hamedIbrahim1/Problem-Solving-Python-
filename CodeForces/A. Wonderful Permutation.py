#link   : https://codeforces.com/problemset/problem/1712/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    x=sorted(l)[:k]
    print(sum([1 for i in x if(i not in l[:k])]))
