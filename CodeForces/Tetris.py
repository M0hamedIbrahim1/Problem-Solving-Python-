#link : https://codeforces.com/problemset/problem/961/A
#author : Mohamed Ibrahim


n,_=input().split();n=int(n)
c=list(map(int,input().split()))
print(min(c.count(x) for x in range(1,n+1)))
