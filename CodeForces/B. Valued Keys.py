#link : https://codeforces.com/problemset/problem/801/B
#author : Mohamed Ibrahim

x, y = input(), input()
print(-1 if any(a<b for a,b in zip(x,y)) else y)
