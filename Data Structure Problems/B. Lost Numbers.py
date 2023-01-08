
# link : https://codeforces.com/problemset/problem/1167/B
# author : Mohamed Ibrahim

arr = [4 , 8, 15, 16, 23, 42]

print("?", 1, 2)
print("?", 2, 3)
print("?", 4, 5)
print("?", 5, 6)

ans = [int(input()) for _ in range(4)]

import itertools

for combo in itertools.permutations(arr):
	a, b, c, d, e, f = combo
	if a * b == ans[0] and b * c == ans[1] and d * e == ans[2] and e * f == ans[3]:
		print("!", a, b, c, d, e, f)
		break
    
    
    
