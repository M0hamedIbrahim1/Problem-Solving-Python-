#link:   https://codeforces.com/problemset/problem/1350/A
#author: Mohamed Ibrahim

t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	ans=0
	for i in range(2,n+1):
		if(n%i==0):
			ans=i
			break;
	print(n+ans+(k-1)*2)
