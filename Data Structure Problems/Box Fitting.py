# Link   : https://codeforces.com/problemset/problem/1498/B
# author : Mohamed Ibrahim


import bisect
for _ in range(int(input())):
    n,w =map(int,input().split())
    a = sorted(list(map(int,input().split())))[::-1]
    k = []
    c=0
    for j in a:
        i=bisect.bisect_left(k,j)
        if(i<len(k)):
            k[i]=k[i]-j
        else:
            k.append(w-j)
            c+=1
    print(c)




    
