#link : https://codeforces.com/problemset/problem/580/A
#author : Mohamed Ibrahim

size = int(input())
Max = cnt = 1
lst = list(map(int,input().split()))
for i in range(1,size):
    if(lst[i]>=lst[i-1]):
        cnt+=1
    else:
        Max = max(cnt,Max)
        cnt = 1
print(max(cnt,Max))


