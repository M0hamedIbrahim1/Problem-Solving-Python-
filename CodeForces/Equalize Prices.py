#link   : https://codeforces.com/problemset/problem/1183/B
#author : Mohamed Ibrahim

q=int(input())
for i in range(q):
	x,y=map(int,input().split())
	a=list(map(int,input().split()))
	if(min(a)+y>=max(a)-y):
		print(min(a)+y)
	else:
		print(-1)
