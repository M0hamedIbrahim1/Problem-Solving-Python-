#link : https://codeforces.com/problemset/problem/63/A
#author : Mohamed Ibrahim

l = []
n=int(input())
l = [input().split() for _ in range(n)]
for i in [['rat'], ['woman','child'], ['man'], ['captain']]:
    for j in l:
        if j[1] in i:print(j[0])
