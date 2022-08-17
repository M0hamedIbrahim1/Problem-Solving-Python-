#link   : https://codeforces.com/problemset/problem/1150/B
#author : Mohamed Ibrahim

n=int(input())
l=[]
c=c2=0
for i in range(n):
    s=input()
    c2+=s.count(".")
    l.append(list(s))
# print(l)
for i in range(1,n-1):
    for j in range(1,n-1):
        if l[i][j]==l[i+1][j]==l[i-1][j]==l[i][j-1]==l[i][j+1]==".":
        	c+=5
        	l[i][j]=l[i+1][j]=l[i-1][j]=l[i][j-1]=l[i][j+1]="1"
# print(c,c2)
if c2==c:
    print("YES")
else:
    print("NO")
