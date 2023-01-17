# link   : https://codeforces.com/problemset/problem/1566/A
# author : Mohamed Ibrahim



for _ in range(int(input())):
    n, s = map(int, input().split())
    print(s // (n // 2 + 1))

    
