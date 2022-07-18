## link   : https://codeforces.com/problemset/problem/1406/A
#author : Mohamed Ibrahim

T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    print("YES" if x-y > 1 else "NO")
    
