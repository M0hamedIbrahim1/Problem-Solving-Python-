#link   : https://codeforces.com/problemset/problem/776/A
#author : Mohamed Ibrahim

a,b=input().split()
n=int(input())
print(a,b)
for i in range(n):
	c,d=input().split()
	if a==c:
		a=d
	elif b==c:
		b=d
	print(a,b)
  
  
