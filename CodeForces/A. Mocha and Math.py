#link   : https://codeforces.com/problemset/problem/1559/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	ans = l[0]
	for i in l:
		ans = ans & i
	print(ans)
