#link : https://codeforces.com/problemset/problem/893/A
#author : Mohamed Ibrahim

n=int(input())
a=[1, 2]
f="YES"
for i in range(n):
  x=int(input())
  if x in a:
    a=[x, 6-sum(a)]
  else:
    f="NO"

print(f)
