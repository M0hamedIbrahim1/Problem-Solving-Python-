# link   : https://codeforces.com/problemset/problem/1763/B
# author : Mohamed Ibrahim


for _ in range(int(input())):
    n, r= map(int, input().split())
    h= list(map(int, input().split()))
    p= list(map(int, input().split()))
    z= [x for _,x in sorted(zip(p, h))]
    p.sort()
    k= r
    i= 0

    while i<n and r != 0:
        if z[i] <= k:
            i += 1
        else:
            r= max(0, r-p[i])
            k += r

    if k<max(h):
        print('NO')
    else:
        print('YES')
        
        
