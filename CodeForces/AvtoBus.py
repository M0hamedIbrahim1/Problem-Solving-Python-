#link   : https://codeforces.com/problemset/problem/1679/A
#author : Mohamed Ibrahim

for t in range(int(input())):
    w = int(input())
    if(w%2 != 0 or w < 4):print(-1)
    else:
        print((w+4)//6,w//4)
