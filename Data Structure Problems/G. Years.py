#  link : https://codeforces.com/problemset/problem/1424/G
#  author : Mohamed Ibrahim

l=[]
c=0
y=0
a=0
for _ in range(int(input())):
    b,d=map(int,input().split())
    l.append((b,1))
    l.append((d,-1))
l.sort()
for i in l:
    c+=i[1]
    if c>a:
        y=i[0]
        a=c
print (y,a)



