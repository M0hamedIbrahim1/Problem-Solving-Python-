# link : https://codeforces.com/problemset/problem/1504/A
# author : Mohamed Ibrahim

for _ in range(int(input())):
	s=input()
	c=0
	for i in s[::-1]:
		if i=='a':
			c+=1
		else:
			break
	if len(s)-1<c:
		print('NO')
	else:
		print('YES')
		print(s[:c]+'a'+s[c:])
	
