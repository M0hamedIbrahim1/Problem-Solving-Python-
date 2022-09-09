# link   : https://codeforces.com/problemset/problem/1539/B
# author : Mohamed Ibrahim

n,q=map(int,input().split())
p=[0]
for i in input():
    p+=[p[-1]+ord(i)-96]
for _ in range(q):
    a,b=map(int,input().split())  
    print(p[b]-p[a-1])
    
