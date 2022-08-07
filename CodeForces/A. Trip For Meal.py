#link   : https://codeforces.com/problemset/problem/876/A
#author : Mohamed Ibrahim


n=int(input())
a=int(input())
b=int(input())
c=int(input())
print((n>1)*min(a,b)+max(0,n-2)*min(a,b,c))
