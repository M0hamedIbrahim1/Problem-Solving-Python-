#link   : https://codeforces.com/problemset/problem/1279/A
#author : Mohamed Ibrahim

for t in range(int(input())):
	a = sorted(list(map(int, input().split())))
	print('Yes' if a[2] <= a[0] + a[1] + 1 else 'No')
