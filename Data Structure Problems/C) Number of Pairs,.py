#link   : https://codeforces.com/problemset/problem/1538/C
#author : Mohamed Ibrahim


import bisect
for _ in range(int(input())):
	n,l,r = map(int,input().split())
	a = sorted(list(map(int, input().split())))
	rslt = 0
	for i in range(n):
		x = bisect.bisect_left(a, l-a[i])
		x = max(i+1, x)
		y = bisect.bisect_right(a, r-a[i])
		if y>x:
			rslt +=(y-x)
	print(rslt)


