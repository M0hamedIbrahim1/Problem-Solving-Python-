#link :   https://codeforces.com/problemset/problem/1506/A
#author : Mohamed Ibrahim


for i in range(int(input())):
	n,m,x=map(int,input().split())
	
	a=(x-1)//n
	b=(x-1)%n
	ans=b*m+(a+1)
	print(ans)
