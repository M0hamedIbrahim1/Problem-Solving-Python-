#link : https://codeforces.com/problemset/problem/11/A
#author : Mohamed Ibrahim


n,d = map(int,input().split())
cnt = x = 0
lst = list(map(int,input().split()))
for i in range(1,len(lst)):
    if lst[i]<=lst[i-1]:
        x = lst[i-1] - lst[i]
        lst[i]+= (((x//d)+1)*d)
        cnt+=(x//d)+1
print(cnt)
