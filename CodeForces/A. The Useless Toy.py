#link   : https://codeforces.com/problemset/problem/834/A
#author : Mohamed Ibrahim

d, s, n = '^>v<', input(), int(input())
if n % 2 == 0:
	print("undefined")
elif (d.find(s[0])+n)%4 == d.find(s[2]):
	print("cw")
else:
	print("ccw")
	
 
 
