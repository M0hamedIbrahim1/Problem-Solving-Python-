# link  : https://codeforces.com/problemset/problem/1175/A
#author : Mohamed Ibrahim

for _ in range(int(input())):    
    n,k = map(int,input().split());t=0
    while n:
        t+=n%k
        n = n//k
        t+=1
    print(t-1)
