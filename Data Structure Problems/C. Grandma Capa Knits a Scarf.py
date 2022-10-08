# link   : https://codeforces.com/problemset/problem/1582/C
# author : Mohamed Ibrahim


from string import ascii_lowercase
 
tc = int(input())
 
for t in range(tc):
	n = int(input())
	s = input()
	ans = -1
 
	for c in ascii_lowercase:
		i = 0
		j = n-1
		flag = cn = 0
 
		while i<j:
			if s[i]==s[j]:
				i += 1
				j -= 1
			elif s[i]!=c and s[j]!=c:
				flag = 1
				break
			elif s[i]==c:
				i+=1
				cn+=1
			else:
				j-=1
				cn+=1
				
		if  flag == 0:
			if ans==-1: ans = cn
			else : ans = min(ans, cn)
	print(ans)
  
  
  
  
  
  
