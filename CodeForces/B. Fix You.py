# link : https://codeforces.com/problemset/problem/1391/B
# author : Mohamed Ibrahim

t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    list1=[input() for i in range(m)]
    ans=sum(l[-1]=="R" for l in list1)+list1[-1].count("D")
    print(ans)
