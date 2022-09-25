# link   : https://codeforces.com/problemset/problem/834/B
# author : Mohamed Ibrahim

n, k = map(int, input().split())
a = input()
n = [0] * n
s = set(a)
for i in s:
    for j in range(a.find(i), a.rfind(i) + 1):
        n[j] += 1
if max(n) > k:
    print('YES')
else:
    print('NO')
    
