# link : https://codeforces.com/problemset/problem/255/A
# author : Mohamed Ibrahim

input()
k=list(map(int,input().split()))
c={sum(k[::3]):"chest",sum(k[1::3]):"biceps",sum(k[2::3]):"back"}
print(c.get(max(c)))
