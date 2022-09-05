# link : https://codeforces.com/problemset/problem/1041/A
# author : Mohamed Ibrahim

n=int(input())
a=list(map(int,input().split()))
print(max(a)-min(a)+1-n)
