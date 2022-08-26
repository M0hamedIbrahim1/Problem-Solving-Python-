#link   : https://codeforces.com/problemset/problem/1612/A
#author : Mohamed Ibrahim

for t in range(int(input())):
    x, y = map(int, input().split())
    if (x + y) % 2 == 0:
        print(x//2, y//2+x%2)
    else:
        print(-1, -1)
        
