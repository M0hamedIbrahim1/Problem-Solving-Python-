#link :   https://codeforces.com/problemset/problem/1490/A
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
    cnt = 0
    s = int(input())
    lst = list(map(int,input().split()))
    for j in range(1,s):
        maX = max(lst[j],lst[j-1])
        miN = min(lst[j],lst[j-1])
        while(maX/miN) > 2:
            miN = 2*miN
            cnt+=1
    print(cnt)
