# link : https://codeforces.com/problemset/problem/1638/B
# author : Mohamed Ibrahim


for iii in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]
	even,odd = [],[]
	for i in a:
		if i%2==0:
			even.append(i)
		else:
			odd.append(i)
	if even!=sorted(even) or odd!=sorted(odd):
		print("NO")
	else:
		print("YES")
