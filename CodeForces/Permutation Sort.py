#link   : https://codeforces.com/problemset/problem/1525/B
#author : Mohamed Ibrahim

T = int(input())
for i in range(T):
    n = int(input())
    lst = list(map(int,input().split()))
    s = sorted(lst)
    if lst == s:
        print(0)
    elif lst[0] == s[0] or lst[-1] == s[-1]:
        print(1)
    elif lst[0] == s[-1] and lst[-1] == s[0]:
        print(3)
    else:
        print(2)
