#link : https://codeforces.com/problemset/problem/1674/A
#author : Mohamed Ibrahim

for _ in range(int(input())):
	x, y = map(int,input().split())
	if y%x != 0:
		print(0,0)
	else:
		print(1,y//x)
