# Link   : https://codeforces.com/contest/1575/problem/A
# author : Mohamed Ibrahim


n,m=map(int,input().split())
l=[]
d={}
for i in range(n):
    l+=[input()]
    d[l[i]]=i
z=list(l)
for i in range(m-1,-1,-1):
    if i%2==0:
        l.sort(key=lambda x:x[i])
    else:
        l.sort(reverse=True,key=lambda x:x[i])
 
for i in l:
    print(d[i]+1,end=" ")
    
