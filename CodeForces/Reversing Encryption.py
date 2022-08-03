#link : https://codeforces.com/problemset/problem/999/B
#author : Mohamed Ibrahim

n, t = int(input()), input()
for i in range(1, n+1):
    if n % i == 0: t = t[i-1::-1] + t[i:]
print(t)
