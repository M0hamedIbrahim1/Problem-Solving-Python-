#link   : https://codeforces.com/problemset/problem/1295/A
#author : Mohamed Ibrahim

for i in range(int(input())):
    n=int(input())
    f=n%2
    k=n//2
    print("7"*f + "1"*(k-f))
