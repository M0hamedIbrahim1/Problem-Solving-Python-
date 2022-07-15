#link:   https://codeforces.com/group/jfviGllBoY/contest/389763/problem/B
#author: Mohamed Ibrahim

l,r = map(int,input().split())
if l %2 != 0:
	l+=1
if l+2 > r:
	print(-1)
else:
	print(l,l+1,l+2)
