#link:   :https://codeforces.com/problemset/problem/1330/A
#author : Mohamed Ibrahim

I = input
for i in range(int(I())):
    n, m = map(int, I().split())
    l=sorted(list(set(map(int, I().split()))))
    for i in l:
        if i<=m+1:
            m+=1
    print(m)
