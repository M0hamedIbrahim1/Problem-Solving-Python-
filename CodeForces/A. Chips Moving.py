#link   : https://codeforces.com/problemset/problem/1213/A
#author : Mohamed Ibrahim

n=int(input())
a=[0,0]
for i in input().split():
	a[int(i)%2]+=1
print(min(a))
