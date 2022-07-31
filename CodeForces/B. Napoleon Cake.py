#link : https://codeforces.com/problemset/status/1501/problem/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=[0]*n
	ans=0
	for i in range(n-1,-1,-1):
		ans=max(ans-1,a[i])
		b[i]=int(ans>0)
	print(*b)
	
