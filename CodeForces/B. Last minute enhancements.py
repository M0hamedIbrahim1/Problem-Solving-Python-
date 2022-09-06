#link   : https://codeforces.com/problemset/problem/1466/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
        a=set()
        n=input()
        n=list(map(int,input().split()))
for i in n:
    if i in a:
        a.add(i+1)
    else:
        a.add(i)
print(len(a))
