#link   : https://codeforces.com/problemset/problem/1141/B
#author : Mohamed Ibrahim

n = int(input())
k = n-1
lst = list(map(int,input().split()))
cnt1 = i = c = 0
while lst[i] != 0 :
    i+=1
while lst[k] != 0 :
    k -=1
    cnt1+=1
m = cnt1+i
for j in range(n):
    if lst[j] == 1:
        c+=1
    else:
        m = max(c,m)
        c=0
print(m)
 
