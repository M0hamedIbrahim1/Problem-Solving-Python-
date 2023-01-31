# link   : https://codeforces.com/problemset/problem/1689/A
# author : Mohamed Ibrahim

for _ in range(int(input())):
  n,m,k = map(int,input().split())
  s1 = input()
  s2 = input()
  s = ''
  s1 =''.join(sorted(s1))
  s2 =''.join(sorted(s2))
  i,j,cnt1,cnt2 = 0,0,0,0
  while i < n and j < m:
    if cnt1 == k or (s2[j]<s1[i] and cnt2 !=k):
      s+=s2[j]
      j+=1
      cnt2+=1
      cnt1 = 0
    else:
      s+=s1[i]
      i+=1
      cnt1+=1
      cnt2 = 0
  print(s)

