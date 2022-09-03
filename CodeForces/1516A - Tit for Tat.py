#link : https://codeforces.com/problemset/problem/1516/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	s = 0
	for i in range(n):
		if k > 0:
			t = min(a[i], k)
			a[i] -= t
			k -= t
			s += t
	a[-1] += s
 
	print(*a)
