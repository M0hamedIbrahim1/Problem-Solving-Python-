#link   : https://codeforces.com/problemset/problem/1714/C
#author : Mohamed Ibrahim

for _ in range(int(input())):
	s = int(input())
	v = 9
	ans = ""
	while s > 0:
		ans = str(min(s,v))+ans
		s -= min(s,v)
		v -= 1
	print(ans)
