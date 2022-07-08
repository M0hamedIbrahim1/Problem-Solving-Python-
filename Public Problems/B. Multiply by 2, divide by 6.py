#link   : https://codeforces.com/problemset/problem/1374/B
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    while n>1:
        if n%6 == 0:
            n = n/6
            cnt+=1
        elif n % 2 != 0:
            n = n * 2
            cnt+=1
        else:
            n = 0
            cnt= -1
    print(cnt)
    
