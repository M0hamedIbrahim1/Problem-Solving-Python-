# link   : https://codeforces.com/problemset/problem/1656/B
# author : Mohamed Ibrahim

for _ in range(int(input())):
    n,k= map(int,input().split())
    lst = set(map(int,input().split()))
    for i in lst:
        if(i+k in lst):
            print("YES")
            break
    else:
        print("NO")
