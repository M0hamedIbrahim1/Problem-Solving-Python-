#link   : https://codeforces.com/problemset/problem/34/B
#author : Mohamed Ibrahim

inp = input().split()
m = int(inp[0])
n = int(inp[1])
lst = list(map(int,input().split()))
lst.sort()
sum = 0
for i in range(m):
    if lst[i] < 0 and n > 0:
        sum+=lst[i]
        n-=1
    elif lst[0] >=0:
        sum = 0
        break
print(abs(sum))
