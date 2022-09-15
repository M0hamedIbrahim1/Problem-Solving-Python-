# link : https://codeforces.com/problemset/problem/1706/A
# author : Mohamed Ibrahim

for i in range(int(input())):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	s='B'*m
	for i in range(n):
		y=l[i]
		a=m+1-y
		o=min(a-1,y-1)
		q=max(a-1,y-1)
		if s[o] != 'A':
			s=s[:o]+'A'+s[o+1:]
		else:
			s=s[:q]+'A'+s[q+1:]
	print(s)
  
