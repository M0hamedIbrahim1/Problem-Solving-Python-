# Link   : https://codeforces.com/problemset/problem/1702/C
# author : Mohamed Ibrahim



for x in range(int(input())):
    input()
    n,k=map(int,input().split())
    ar=input().split()
    m1={}
    m2={}
    for i, j in enumerate(ar):
        if j not in m1: m1[j] = i
        m2[j] = i
    for i in range(k):
        a,b=input().split()
        if a in m1 and b in m2 and m1[a] < m2[b]:print("YES")
        else:print("NO")



