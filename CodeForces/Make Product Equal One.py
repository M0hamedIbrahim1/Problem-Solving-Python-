#link   : https://codeforces.com/problemset/problem/1206/B
#author : Mohamed Ibrahim

n=int(input())
l=list(map(int,input().split()))
x=0
z=0
for i in l:
	if(i<0):
		z=z+1
	x=x+abs(abs(i)-1)
if(z%2==1):
	if(0 not in l):
		x=x+2
print(x)
