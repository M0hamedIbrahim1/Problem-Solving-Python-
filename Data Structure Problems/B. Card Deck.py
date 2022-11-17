# Link   : https://codeforces.com/problemset/problem/1492/B
# author : Mohamed Ibrahim


if __name__ == '__main__':
	for _ in range (int(input())):
		n = int(input())
		l = list(map(int,input().split()))
		d = dict()
		for i in range (n):
			d[l[i]] = i
		ans = []
		prev = n
		for i in range (n,0,-1):
			if d[i] <= prev:
				ans+=l[d[i]:prev]
				prev = d[i]
		print(*ans)

    
    
