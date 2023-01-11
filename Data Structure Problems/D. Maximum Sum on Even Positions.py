# link  : https://codeforces.com/problemset/problem/1373/D
# author : Mohamed ibrahim

t=int(input())
while t:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    sum=0
    for i in range(0,n,2):
        sum+=a[i]
    m=0
    d=0
    for i in range(1,n,2):
        d+=(a[i]-a[i-1])
        if d<0:
            d=0
        m=max(m,d)
    d=0
    for i in range(2,n,2):
        d+=(a[i-1]-a[i])
        if d<0:
            d=0
        m=max(m,d)
    print(sum+m)
    
        
    
    
    
        
    
        
