#link   : https://codeforces.com/problemset/problem/1398/B
#author : Mohamed Ibrahim

 
for _ in range(int(input())):
	l=input().split("0")
	l.sort(reverse=True)
	f=0
	for i in range(0,len(l),2):
		f+=len(l[i])
	print(f)
  
