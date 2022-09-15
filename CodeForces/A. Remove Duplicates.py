# link : https://codeforces.com/problemset/problem/978/A
# author : Mohamed Ibrahim

input()
x = []
for i in list(map(int,input().split()))[::-1]:
    if not i in x:
        x.append(i)
print(len(x))
print(*x[::-1])
