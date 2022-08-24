#link   : https://codeforces.com/problemset/problem/1438/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    n = int(input())
    arr = set(i for i in input().split())
    print("YES" if len(arr)<n else "NO")
    
