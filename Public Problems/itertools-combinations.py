#link   : https://www.hackerrank.com/challenges/itertools-combinations/problem
#author : Mohamed Ibrahim 

from itertools import combinations
s,n = input().split()
res = list(s)
res.sort()
for i in range(int(n)):
    lis_ = list(combinations(res,i+1))
    for j in lis_:
        print(''.join(j))
