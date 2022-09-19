#link    : https://codeforces.com/problemset/problem/721/A
# author : Mohamed Ibrahim

n=int(input())
a=input().split('W')
c=[len (i) for i in a if len(i)>0]
print(len(c))
print(*c)
