#link   : https://www.hackerrank.com/challenges/python-sort-sort/problem
#author : Mohamed Ibrahim

T,n = map(int,input().split())
lisT = [list(map(int,input().split())) for i in range(T)]
k = int(input())
lisT.sort(key = lambda x : x[k])
for j in lisT:
    print(*j)
