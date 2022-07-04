#link   : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
#author : Mohamed Ibrahim

from itertools import combinations
size = int(input())
lst = input().split()
length = int(input())
N = list(combinations(lst,length))
ALL_COMP = len(N)
cnt = 0
for i in N:
    if 'a' in i:
        cnt+=1
print(round(cnt/ALL_COMP,3))
