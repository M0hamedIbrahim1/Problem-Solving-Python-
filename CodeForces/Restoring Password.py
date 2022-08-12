#link : https://codeforces.com/problemset/problem/94/A
#author : Mohamed Ibrahim

s=input()
l=[]
for i in range(10):
	l.append(input())
for i in range(0,80,10):
	print(l.index(s[i:i+10]),end="")
