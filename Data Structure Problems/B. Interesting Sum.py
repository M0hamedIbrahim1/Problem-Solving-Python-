# link : https://codeforces.com/problemset/problem/1720/B
# author : Mohamed Ibrahim


for _ in range(int(input())):
	n = int(input())
	a = sorted(map(int,input().split()))
	print(a[-1]+a[-2]-a[0]-a[1])



