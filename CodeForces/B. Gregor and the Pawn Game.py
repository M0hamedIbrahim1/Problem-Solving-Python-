# link : https://codeforces.com/problemset/problem/1549/B
# author : Mohamed Ibrahim

for _ in range(int(input())):
	n=int(input())
	e=list(map(int,input()))
	l=list(map(int,input()))
	c=0
	for i in range(n):
		if l[i]==1:
			if e[i]==0:
				c+=1
			else:
				if i>0 and e[i-1]==1:
					c+=1
					e[i-1]=0
				elif i<n-1 and e[i+1]==1:
					c+=1
					e[i+1]=0
	print(c)
