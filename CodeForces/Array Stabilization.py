#link : https://codeforces.com/problemset/problem/1095/B
#author : Mohamed Ibrahim

input()
a=sorted(map(int,input().split()))
print(min(a[-1]-a[1],a[-2]-a[0]))
