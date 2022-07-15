#link:   https://codeforces.com/group/jfviGllBoY/contest/389763/problem/D
#author: Mohamed Ibrahim

n,x=map(int,input().split())
c=0
for i in range(n):
	s,d=input().split()
	d=int(d)
	if s=="+":
		x+=d
	else:
		if x-d>=0:
			x-=d
		else:
			c+=1
print(x,c)
