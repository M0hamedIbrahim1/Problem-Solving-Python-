#link   : https://codeforces.com/problemset/problem/1421/A
#author : Mohamed Ibrahim

a=int(input())
for j in range (a):
    n,k=map(int,input().split())
    if (n+1)//2<k:
       print(-1)
       continue
    for i in range(n):    
       if i%2==0 and k!=0:
           print("."*i+"R"+"."*(n-i-1))
           k-=1
       else:
            print("."*n)

