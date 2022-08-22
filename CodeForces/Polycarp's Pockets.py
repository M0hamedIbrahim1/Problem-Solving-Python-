#link   : https://codeforces.com/problemset/problem/1003/A
#author : Mohamed Ibrahim

n=input()
l=list(map(int,input().split()))
print(max(l.count(i) for i in l))
