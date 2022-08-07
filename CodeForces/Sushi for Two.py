#link   : https://codeforces.com/problemset/problem/1138/A 
#author : Mohamed Ibrahim

x=int(input())
a=list(map(int,input().split()))+[0]
m=n=p=0
for i in range(x):
	m+=1
	if a[i]!=a[i+1]:
		p=max(p,min(m,n))
		n=m
		m=0
print(2*p)
