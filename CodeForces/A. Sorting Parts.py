# link   : https://codeforces.com/problemset/problem/1637/A
# author : Mohamed Ibrahim

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if a != sorted(a) else "NO")   
    
