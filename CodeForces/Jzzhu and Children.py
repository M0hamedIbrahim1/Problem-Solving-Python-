#link   : https://codeforces.com/problemset/problem/450/A
#author : Mohamed Ibrahim

import math
n,m=map(int,input().split())
l=list(map(lambda x:math.ceil(int(x)/m),input().split()))
l.reverse()
print(n-l.index(max(l)))
