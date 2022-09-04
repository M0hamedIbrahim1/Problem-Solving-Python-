# link : https://codeforces.com/problemset/problem/1552/A
# author : Mohamed Ibrahim

for ii in range(int(input())):
	n=int(input())
	s=input()
	t,a=sorted(s),n
	for jj in range(n):
		if s[jj]==t[jj]:
			a-=1
	print(a)
