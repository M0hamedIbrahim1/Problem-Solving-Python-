#link   : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
#author : Mohamed Ibrahim

from itertools import combinations_with_replacement
s,size = input().split()
for i in combinations_with_replacement(sorted(s),int(size)):
    print("".join(i))
    
    
