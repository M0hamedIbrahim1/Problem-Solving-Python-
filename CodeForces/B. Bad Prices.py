# link    : https://codeforces.com/problemset/problem/1213/B
# author  : Mohamed Ibrahim

for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))[::-1]
	c = a[0]
	count = 0
	for j in a:
		if c < j:
			count += 1
		c = min(c, j)
	print(count)

  
