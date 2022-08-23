#link   : https://codeforces.com/problemset/problem/1716/A
#author : Mohamed Ibrahim

for i in range(int(input())):
	n=int(input())
	if n==1:
		print(2)
	else:
		print((n+2)//3)
