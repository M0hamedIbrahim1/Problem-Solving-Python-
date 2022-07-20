#link   : https://codeforces.com/contest/1185/problem/B
#author : Mohamed Ibrahim

n=int(input())
 
for i in range(0, n):
	a=str(input())
	b=str(input())
	l=len(b)
	le=len(a)
	a = a+'0'
	c=0
	for j in range(0, l):
		if (a[c]==b[j] and c<le):
			c+=1
		elif (b[j-1] != b[j] or j==0):
			c=-1
			break
	if c==le:
		print('YES')
	else:
		print('NO')
