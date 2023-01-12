# link    : https://codeforces.com/contest/1260/problem/B
# author  : Mohamed Ibrahim

for i in range(int(input())):
	a,b = map(int,input().split())
	print('YES'if (a + b) % 3 == 0 and abs(a-b) <= (a+b) // 3 else 'NO')
  
  
