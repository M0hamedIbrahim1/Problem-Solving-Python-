#link   : https://codeforces.com/problemset/problem/1433/C
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    Max = max(lst)
    res = -1
    for j in range(n):
        if lst[j]== Max and ((j > 0 and lst[j] > lst[j-1]) or (j < n-1 and lst[j]>lst[j+1])):
            res = j+1
    print(res)
                
