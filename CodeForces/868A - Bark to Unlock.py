#link : https://codeforces.com/problemset/problem/868/A
#author : Mohamed Ibrahim

key = input()
k = int(input())

words = []

for _ in range(k):
	words.append(input())


for i in range(k):
	for j in range(k):
		if key in (words[i] + words[j]):
			print('YES')
			exit(0)
print('NO')
