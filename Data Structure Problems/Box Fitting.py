# Link   : https://codeforces.com/problemset/problem/1498/B
# author : Mohamed Ibrahim


import bisect
for _ in range(int(input())):
    n,w =map(int,input().split())
    a = sorted(list(map(int,input().split())))[::-1]
    k = []
    c=0
    for j in a:
        i=bisect.bisect_left(k,j)
        if(i<len(k)):
            k[i]=k[i]-j
        else:
            k.append(w-j)
            c+=1
    print(c)
    
    
    # other sol : 
    
    
    t=int(input())
for _ in range(t):
	n,w=map(int,input().split())
	lista=list(map(int,input().split()))
	lista.sort(reverse=True)
	# print(l)
	d={}
	for i in lista:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
 
	h=0
	while(n>0):
		w1=w
		for i in d:
			while d[i]>0 and (i<=w1):
				w1-=i
				d[i]-=1
				n-=1
		h+=1
	print(h)
    




    
