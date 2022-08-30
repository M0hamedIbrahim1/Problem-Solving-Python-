#link   : https://codeforces.com/problemset/problem/1634/A
#author : Mohamed Ibrahim

for ii in range(int(input())):
	n,k = map(int,input().split())
	s = input()
	if k==0 or s==s[::-1]:
		print(1)
	else:
		print(2)
 
