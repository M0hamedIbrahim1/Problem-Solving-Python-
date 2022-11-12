#   Link   : https://codeforces.com/problemset/problem/195/B
#   author : Mohamed Ibrahim

n, m = map(int, input().split())
a = []
t = 1 if m % 2 else -1
for i in range(m):
	a.append(int(m/2)+int(m%2)+t*int((i+1)/2))
	t *= -1
for i in range(n):
	print(a[int(i%m)])
  
  
