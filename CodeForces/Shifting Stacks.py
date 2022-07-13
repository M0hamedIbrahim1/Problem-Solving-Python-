#link : https://codeforces.com/problemset/problem/1486/A
#author : Mohamed Ibrahim

t=int(input())
for k in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	stock=0
	f=0
	for i in range(n):
		stock+=l[i]-i
		if(stock<0):
			f=1
			break
	if(f==1):
		print("NO")
	else:
		print("YES")
 
