#link: https://www.hackerrank.com/challenges/collections-counter/problem
#author : @Mohamed Ibrahim
from collections import Counter
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print (sum(total))
