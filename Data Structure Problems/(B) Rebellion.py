# link   : https://codeforces.com/problemset/problem/1746/B
# author : Mohamed Ibrahim


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(l[:l.count(0)].count(1))
    
    
