#link   : https://codeforces.com/problemset/problem/1543/A
#author : Mohamed Ibrahim
t = int(input())
 
for _ in range(int(input())):
	a, b = map(int, input().split())
	if a == b:
		print(0, 0)
	else:
		g = abs(a - b)
		x = a % g
		print(g, min(x, g - x))
