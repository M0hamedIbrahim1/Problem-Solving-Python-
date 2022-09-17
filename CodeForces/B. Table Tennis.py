# link   : https://codeforces.com/problemset/problem/879/B
# author : Mohamed Ibrahim

n, k = map(int, input().split())
v = list(map(int, input().split()))
occ = 0
pre = v[0]
for i in range(1, n):
	if pre>v[i]:
		occ+=1
	else:
		pre = v[i]
		occ = 1
	if occ==k:
		break
print(pre)
