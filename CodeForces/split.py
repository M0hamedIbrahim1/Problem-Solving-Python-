#Link : https://codeforces.com/problemset/problem/1496/A
#author : Mohamed Ibrahim

for t in range(int(input())):
	n, k = map(int, input().split())
	a = input()
    
	if (k*2)+1<=n and a[n-k:][::-1] == a[:k]:
	    print("YES")
	else:
	    print("NO")
