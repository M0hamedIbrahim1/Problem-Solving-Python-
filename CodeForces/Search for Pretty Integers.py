#link : https://codeforces.com/problemset/problem/870/A
#author : Mohamed Ibrahim


n,m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
m = 100
if a & b:
    m = min(a&b)
ma = min(a)
mb = min(b)
res1 = str(ma)+str(mb)
res2 = str(mb)+str(ma)
res = min(min(int(res1),int(res2)) , m)

print(res)
