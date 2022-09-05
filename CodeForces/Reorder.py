# link : https://codeforces.com/problemset/problem/1436/A
# author : Mohamed Ibrahim

for i in range(int(input())):
	n, m = map(int, input().split())
	a = map(int, input().split())
	print("YES" if sum(a)==m else "NO")
  
