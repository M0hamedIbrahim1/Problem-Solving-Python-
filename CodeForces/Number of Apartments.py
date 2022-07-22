#link   : https://codeforces.com/problemset/problem/1430/A
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
	n = int(input())
	if n in [1,2,4]:print(-1)
	elif n%3==0:print(n//3,0,0)
	elif (n-5)%3==0:print((n-5)//3,1,0)
	elif (n-7)%3==0:print((n-7)//3,0,1)
