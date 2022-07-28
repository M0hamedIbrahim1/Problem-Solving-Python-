#link : https://codeforces.com/problemset/problem/621/A
#author : Mohamed Ibrahim

n = int(input())
a = [int(x) for x in input().split()]
s = sum(a)
if s%2:
  s -= min(i for i in a if i%2)
print(s)
