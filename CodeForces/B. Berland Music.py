#link   : https://codeforces.com/problemset/problem/1622/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
	n = int(input())
	p = [int(x) for x in input().split()]
	s = input()
	l = sorted([[s[i], p[i], i] for i in range(n)])
	q = [-1 for i in range(n)]
	for i in range(n):
		q[l[i][2]] = i + 1
	print(*q)

  
