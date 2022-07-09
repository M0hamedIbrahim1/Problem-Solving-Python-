#link   : https://codeforces.com/problemset/problem/1337/B 
#author : Mohamed Ibrahim

for _ in range(int(input())):
	(x,n,m) = map(int,input().split())

	while(x>20 and n>0):
		x = x//2+10 
		n-=1
    
	if x-10*m>0:
		print("NO")
	else:
		print("YES")
