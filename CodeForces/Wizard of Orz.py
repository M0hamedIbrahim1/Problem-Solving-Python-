#link   : https://codeforces.com/problemset/problem/1467/A
#author : Mohamed Ibrahim
t = int(input())
 
for x in range(t):
	n = int(input())
	st = "9" + "8901234567"*n
	print(st[:n])
