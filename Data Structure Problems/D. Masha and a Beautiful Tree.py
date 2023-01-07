# link   : https://codeforces.com/problemset/problem/1741/D
# author : Mohamed Ibrahim


for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a = [a[i]-1 for i in range(n)]
	ans1 = 0
	flag = True
	while len(a) > 1:
		ans = []
		for i in range(0,len(a),2):
			if abs(a[i+1]-a[i]) > 1:
				flag = False
				break
			if a[i+1] < a[i]:
				ans1 += 1
			ans.append(a[i]//2)
		a = ans
		if not flag:
			break
		# print(a)
	if flag :
		print(ans1)
	else:
		print(-1)				


