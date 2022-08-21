#link   : https://codeforces.com/problemset/problem/1709/B
#author : Mohamed Ibrahim

n, m = map(int, input().split())
a = list(map(int, input().split()))
st = [0]
ts = [0]
for i in range(1, n):
    st += [st[-1] + max(0, a[i-1] - a[i])]
    ts += [ts[-1] + max(0, -a[n-i-1] + a[n-i])]
for i in range(m):
    s, t = map(int, input().split())
    if s<t:
        print(st[t-1] - st[s-1])
    else:
        print(ts[n-t] - ts[n-s])
        
