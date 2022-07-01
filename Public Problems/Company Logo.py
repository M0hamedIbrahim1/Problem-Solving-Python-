#link   : https://www.hackerrank.com/challenges/most-commons/problem
#author : Mohamed Ibrahim

from collections import Counter
s = input()
c = Counter(sorted(s))
for i in c.most_common(3):
    print(*i) 
    
