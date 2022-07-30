#link : https://codeforces.com/problemset/problem/1709/B
#author : Mohamed Ibrahim

n,a,ans,c=int(input()),list(map(int,input().split())),0,0
for i in range(n):a[i]=[a[i],i]
a.sort(reverse=True)
for i in a:
    ans+=i[0]*c+1
    c+=1
print(ans)
for i in a:print(i[1]+1,end=' ')
