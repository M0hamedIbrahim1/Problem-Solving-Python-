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

	
	
	
	----------------
	if __name__ == '__main__':
	for _ in range (int(input())):
		n = int(input())
		l = list(map(int,input().split()))
		p = [0]*n
		for i in range(n):
			p[l[i]-1] = i
		a,r = n,0
		ans = ''
		for i in range (n):
			a = min(a,p[i])
			r = max(r,p[i])
			if r-a == i:
				ans+='1'
			else:
				ans+='0'
		print(ans)
	
