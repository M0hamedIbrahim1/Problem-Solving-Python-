# link   : https://codeforces.com/problemset/problem/1265/B
# author : Mohamed Ibrahim


for nt in range(int(input())):
	n=int(input())
	s="1"
	l=list(map(int,input().split()))
	d={}
	for i in range(n):
		d[str(l[i])]=i
	left = d["1"]
	right = left
	num = 2
	while num!=n+1:
		i = d[str(num)]
		if i<left:
			left = i
		elif i>right:
			right = i
		if (right-left)==num-1:
			s+="1"
		else:
			s+="0"
		num+=1
	print (s)
