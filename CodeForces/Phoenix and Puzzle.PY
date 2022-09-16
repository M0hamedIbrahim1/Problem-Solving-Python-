#link   : https://codeforces.com/problemset/problem/1515/B
#author : Mohamed Ibrahim

for _ in range(t):
    n=int(input())
    if (n/2) **(1/2) % 1==0 or (n/4) **(1/2) % 1==0:
        print("YES")
    else:
        print("NO")
