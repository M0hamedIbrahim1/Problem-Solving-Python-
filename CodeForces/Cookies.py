#link : https://codeforces.com/problemset/problem/129/A
#author : Mohamed Ibrahim

input()
a=[int(x)%2 for x in input().split()]
print(a.count(sum(a)%2))
