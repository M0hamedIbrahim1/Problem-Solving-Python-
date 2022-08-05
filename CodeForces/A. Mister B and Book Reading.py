#link : https://codeforces.com/contest/820/problem/A
#author : Mohamed Ibrahim

c,v0,v1,a,l=map(int,input().split())
sum1=v0
days=1
while(sum1<c):
    sum1+=min(v0+days*a-l,v1-l)
    days+=1
print(days)
