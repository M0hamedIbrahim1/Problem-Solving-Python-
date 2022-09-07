# link   : https://codeforces.com/problemset/problem/34/A
# author : Mohamed Ibrahim

n=int(input())
l=list(map(int,input().split()))
f=[]
for i in range(n):
	f.append(abs(l[i]-l[i-1]))
c=f.index(min(f))
if c==0:
	print(n,1)
else:
	print(c,c+1)
