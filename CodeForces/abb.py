# link : https://codeforces.com/problemset/problem/1428/C
# author : Mohamed Ibrahim

TC = int(input())
for tc in range(TC):
	s = input()
	ans=0
	for i in s:
		if (i=='B' and ans!=0): ans-=1
		else: ans+=1
	print(ans)
  
