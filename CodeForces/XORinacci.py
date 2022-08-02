#link   : https://codeforces.com/problemset/problem/1208/A
#author : Mohamed Ibrahim

t=int(input())
while t:
	t=t-1	
	a,b,n = map(int,input().split())
	l = [a,b,a^b]
	print(l[n%3])
