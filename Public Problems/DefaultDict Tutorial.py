#link : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#author : @Mohamed Ibrahim

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, raw_input().split())

for i in range(1,n+1):
    d[raw_input()].append(str(i))
    
for i in range(m):
    print (' '.join(d[raw_input()]) or -1)
