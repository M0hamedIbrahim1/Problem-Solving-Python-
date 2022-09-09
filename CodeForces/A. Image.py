#link   : https://codeforces.com/problemset/problem/1721/A
#author : Mohamed Ibrahim


n = int(input())
for i in range(n):
    s=input()+input()
    print(len(set(s))-1)
