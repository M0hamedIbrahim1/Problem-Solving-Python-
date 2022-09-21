# link   : https://codeforces.com/problemset/problem/1700/A
# author : Mohamed Ibrahim


for _ in ' '*int(input()):
	n,m=map(int,input().split())
	print(m*(m-1)//2+(n*(n+1)*m)//2)
  
