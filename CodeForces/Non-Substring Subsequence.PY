#LINK   : https://codeforces.com/problemset/problem/1451/B
#author : Mohamed ibrahim

for j in range(int(input())):
  n,q = map(int,input().split())
  s = input()
  for i in range(q):
    l,r = map(int,input().split())
    l-=1
    r-=1
    if(s[l] in s[:l] ) or (s[r] in s[r+1:]):
        print("YES")
    else:
        print("NO")
