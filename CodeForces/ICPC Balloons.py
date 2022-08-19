#link   : https://codeforces.com/problemset/problem/1703/B
#author : Mohamed Ibrahim

t = int(input())
for i in range(t):
    cnt = 0
    input()
    s = input()
    for i in set(s):
        if s.count(i) == 1:
            cnt+=2
        else:
            cnt+=2
            cnt+=s.count(i)-1
    print(cnt)
    
