# link   : https://codeforces.com/problemset/problem/975/A
# author : Mohamed Ibrahim

n = int(input())
s = input().split()
 
print(len(set(frozenset(si) for si in s)))
