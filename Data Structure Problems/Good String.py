# link   : https://codeforces.com/problemset/problem/1385/D
# author : Mohamed Ibrahim


T = int(input())


def f(x,z):
	if len(x)==0:
		return 0
	if len(x)==1:
		return int(x!=z)
	m = len(x)//2
	L = x[:m]
	R = x[m:]
	a = (m-L.count(z))+f(R,chr(ord(z)+1))
	b = (m-R.count(z))+f(L,chr(ord(z)+1))
	return min(a,b)

while T:
	n = int(input())
	S = input()
	print(f(S,"a"))
	T = T - 1
  
  
