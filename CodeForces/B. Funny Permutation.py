# link   : https://codeforces.com/problemset/problem/1741/B  
# author : Mohamed Ibrahim


for _ in range(int(input())): 
    n=int(input().strip())
    if n==3:print(-1)
    else: 
        print(*[n,n-1]+[i for i in range(1,n-1)])
        
        
        
        
