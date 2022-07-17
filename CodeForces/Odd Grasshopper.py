#link    : https://codeforces.com/problemset/problem/1607/B
#author  : Mohamed Ibrahim
t = int(input())
for q in range(t):
	a,b = map(int,input().split())
	for i in range((b // 4) * 4 + 1, b+1):
		if a % 2 == 0:
			a -= i
		else:
			a += i
	print(a)

