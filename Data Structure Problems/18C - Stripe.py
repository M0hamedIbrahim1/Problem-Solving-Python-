
  #link  : https://codeforces.com/problemset/problem/18/C
  #auhor : Mohamed Ibrahim



n = int(input())
m = list(map(int,input().split()))
z = sum(m)
a = 0; c =0
for i in range(n-1):
   a+=m[i]
   z-=m[i]
   if(a==z):
     c+=1
     
print(c)

