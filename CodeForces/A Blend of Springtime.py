#link : https://codeforces.com/problemset/problem/989/A
#author : Mohamed Ibrahim

s=input()
m=["ABC","ACB","BAC","BCA","CAB","CBA"]
for t in m:
 if t in s:
  print("Yes")
  exit()
print("No")
