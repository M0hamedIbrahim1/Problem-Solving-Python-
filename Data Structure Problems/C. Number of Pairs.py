# link   : https://codeforces.com/problemset/problem/1538/C
# author : Mohamed Ibrahim



t = int(input())

for i in range(t):
	n,l,r = map(int, input().split())
	a = sorted(list(map(int, input().split())))

	count = 0
	i=0
	j=0
	
	while(i<n):
		n -= 1
		while(i<n and a[i]+a[n]<l):
			i += 1

		while(j<n and a[j]+a[n]<=r):
			j += 1

		count += min(j,n) - i		

	print(count)			
  
  
  
