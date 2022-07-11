#link   : https://codeforces.com/problemset/problem/1535/B
#author : Mohamed Ibrahim

import math
t=int(input())
while t:
    t-=1
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(l[i],2*l[j])>1 or math.gcd(l[i]*2,l[j])>1:
                c+=1
    print(c)
