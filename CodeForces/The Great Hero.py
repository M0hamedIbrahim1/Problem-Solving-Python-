#link   : https://codeforces.com/problemset/problem/1480/B
$author : Mohamed Ibrahim

for _ in range(int(input())):
    a,b,n=map(int,input().split())
    ea=list(map(int,input().split()))
    eh=list(map(int,input().split()))
    for x,y in sorted(zip(ea,eh)):
        b=b+(-y//a)*x
    if (b<=-x):
        print("NO")
    else:print("YES")
