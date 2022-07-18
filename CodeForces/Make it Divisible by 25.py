#link   : https://codeforces.com/problemset/problem/1593/B
#author : Mohamed Ibrahim

T = int(input())
for i in range(T):
    s = input()
    m = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if int(s[i]+s[j]) % 25 == 0:
                m = len(s) - (i+2)
    print(m)
