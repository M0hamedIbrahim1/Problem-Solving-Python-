#link   : https://codeforces.com/problemset/problem/1200/A
#author : Mohamed Ibrahim

n=int(input())
s=input()

l=['0']*10
for i in s:
	if i=="L":
		a=l.index('0')
		l[a]='1'
	elif i=='R':
		a=l[::-1].index('0')
		l[-1-a]='1'
	else:
		l[int(i)]='0'
print(''.join(l))

