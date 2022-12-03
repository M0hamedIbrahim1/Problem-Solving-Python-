# link   : https://codeforces.com/problemset/problem/1265/B
# author : Mohamed Ibrahim


for _ in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    arr = [(a[i], i) for i in range(n)]
    arr.sort()
    l = r = arr[0][1]
    ans = [1]*n
    for i in range(1, n):
        l = min(l, arr[i][1])
        r = max(r, arr[i][1])
        ans[i] = int(r-l==i)
    print(*ans,sep='')

    
    
for _ in range (int(input())):
	n = int(input())
	l1 = list(map(int, input().split()))
	arr = [0] * n
	for i in range (n):
		arr[l1[i] - 1] = i
	l = n
	r = 0
	s = ""
	for i in range (n):
		l = min(l, arr[i])
		r = max(r, arr[i])
		if r - l == i:
			s += "1"
		else:
			s += "0"
	print(s)
