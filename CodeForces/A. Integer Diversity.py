# link   : https://codeforces.com/problemset/problem/1616/A
# author : Mohamed Ibrahim

t=int(input())
for i in range(t):
	n=int(input())
	z=list(map(int,input().split()))
	s=set()
	for i in z:
		if(i in s):
			s.add(-i)
		else:
			s.add(i)
	print(len(s))
