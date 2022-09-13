# link : https://codeforces.com/problemset/problem/1722/C
# author : Mohamed Ibrahim

import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
	n = int(input())
	s = [set(list(input().split())) for _ in range(3)]
	t = []
	for p in s:
		a = 0
		for c in p:
			b = 0
			for q in s:
				if c in q:
					b += 1
			if b==1:
				a += 3
			elif b==2:
				a += 1
		t.append(a)
	ans.append(t)
 
for i in ans:
	print(*i)
