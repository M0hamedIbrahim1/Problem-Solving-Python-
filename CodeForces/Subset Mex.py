#link   : https://codeforces.com/problemset/problem/1406/A
#author : Mohamed Ibrahim

for t in range(input()):
    n = input()
    A = B = 0
    for x in sorted(map(int,raw_input().split())):
        if x > A: break
        if x == A: A+=1
        elif x == B: B+=1
    print(A+B)
