# link : https://codeforces.com/problemset/problem/1676/C
# author : Mohamed Ibrahim

for _ in range (int(input())):
  n, m = map(int, input().split())
  x = []
  z = 1000000000
  for i in range(n):
    x.append(input())
  for i in range(n):
    for j in range(i + 1, n):
      w = 0
      for c in range(m):
        w += abs(ord(x[i][c]) - ord(x[j][c]))
      if w < z: z = w
  print(z)
