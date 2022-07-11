#link   : https://codeforces.com/problemset/problem/1324/A
#author : Mohamed Ibrahim

for i in range(int(input())):
	n = int(input())
	x = list(map(int, input().split()))
	if all(i%2 == x[0]%2 for i in x):
		print('YES')
	else:
		print('NO')
