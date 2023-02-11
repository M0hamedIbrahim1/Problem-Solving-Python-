# link   : https://codeforces.com/problemset/problem/1537/E1
# author : Mohamed Ibrahim



n,k=[int(i) for i in input().split(' ')]
s=input()
 
new=[]
 
for i in range(1,n+1):
    a=s[:i]
    while len(a)<k:
        a+=a
    new.append(a[:k])
 
new.sort()
print(new[0])

