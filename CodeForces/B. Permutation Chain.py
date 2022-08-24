#link   : https://codeforces.com/problemset/problem/1716/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
	n = int(input())
	p = [i + 1 for i in range(n)]
	print(n)
	for i in range(n):
		print(*p)
		if i < n - 1:
			p[i], p[i + 1] = p[i + 1], p[i]
            
