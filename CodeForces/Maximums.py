#link   : https://codeforces.com/problemset/status/1326/problem/B
#author : Mohamed Ibrahim

n=int(input())
a=[int(x) for x in input().split()]
m=0
for i in a:
    print(i+m)
    m+=max(0,i)
