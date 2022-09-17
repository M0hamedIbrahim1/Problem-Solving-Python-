# link : https://codeforces.com/problemset/problem/1300/A
#author : Mohamed Ibrahim

t=int(input())
for _ in range(t):
	n= int(input())
	a=list(map(int,input().split()))
	c=a.count(0)
	if(sum(a) + c==0):
		c+=1
	print(c)
