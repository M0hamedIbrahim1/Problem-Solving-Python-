#link   : https://codeforces.com/problemset/problem/977/B
#author : Mohamed Ibrahim

import statistics
from statistics import mode
size = int(input())
s = input()
lst = []
for i in range(size-1):
    lst.append(s[i]+s[i+1])
print(mode(lst))

# print(max(set(lst), key = lst.count)) == mode(lst)
