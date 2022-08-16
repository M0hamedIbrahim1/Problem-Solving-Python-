#link : https://codeforces.com/problemset/problem/369/A
#author : Mohamed Ibrahim

n,m,k = map(int, input().split())
al = list(map(int, input().split()))
k -= al.count(2)
m -= al.count(1) + max(0, -k)
print(max(0, -m))
        
