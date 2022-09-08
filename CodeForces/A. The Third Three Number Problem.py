#link : https://codeforces.com/problemset/problem/1699/A
#author : Mohamed Ibrahim

for t in range(int(input())):n = int(input()); print(*[(0,0,n//2),[-1]][n&1])
