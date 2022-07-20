#Link : https://codeforces.com/problemset/problem/1283/B
#author : Mohamed Ibrahim

for i in range(int(input())):
    n,k =map(int,input().split())
    print(k*(n//k)+min(k//2,n%k))
