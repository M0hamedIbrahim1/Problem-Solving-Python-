link    : https://codeforces.com/problemset/problem/115/A
#author : Mohamed Ibrahim

n=int(input())
 
l=[int(input()) for i in range(n)]
r=0
for i in range(n):
    c=0
    while(i>=0):
        i=l[i]-1
        c+=1
    r=max(c,r)
print(r) 
