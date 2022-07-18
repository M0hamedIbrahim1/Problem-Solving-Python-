#link   : https://codeforces.com/problemset/problem/1543/B
#author : Mohamed Ibrahim

t=int(input())
while t>0:
	t-=1
	n=int(input())
	a=list(map(int,input().split()))
	s=sum(a)
	z=(s%n)*(n-s%n)
	print(z)
