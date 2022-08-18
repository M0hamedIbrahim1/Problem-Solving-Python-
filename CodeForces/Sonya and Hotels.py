#link   : https://codeforces.com/problemset/problem/1004/A
#author : Mohamed Ibrahim

n,d=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n-1):
	if a[i+1]-a[i]-(2*d)>0:
		s+=2
	elif a[i+1]-a[i]-(2*d)==0:
	    s+=1
print(s+2)	
