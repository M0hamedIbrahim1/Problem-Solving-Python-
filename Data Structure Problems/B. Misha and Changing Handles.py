# link : https://codeforces.com/problemset/problem/501/B
# author : Mohamed Ibrahim


n = int(input())

d = dict()

for i in range(n):
	fr, to = map(str, input().split())

	if fr in d:
		d[to] = d[fr]
		del d[fr]
	else:
		d[to] = fr

print(len(d))
for p in d:
	print(d[p], p)
  
  
