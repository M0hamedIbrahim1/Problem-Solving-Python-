#link   : https://codeforces.com/problemset/problem/205/A
#author : Mohamed Ibrahim

n = int(input())
lst = list(map(int,input().split()))
m = min(lst)
if lst.count(m) > 1:
    print("Still Rozdil")
else:
    print(lst.index(m)+1)
