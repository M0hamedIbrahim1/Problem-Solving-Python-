#link    : https://codeforces.com/problemset/problem/631/A
#author  : Mohamed Ibrahim

n=int(input())
a=b=0
for i in input().split():
    a|=int(i)
for i in input().split():
    b|=int(i)
print(a+b)
