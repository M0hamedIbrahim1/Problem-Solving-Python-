# link : https://codeforces.com/problemset/problem/1703/D
# author : Mohamed Ibrahim

for _ in range(int(input())):
  n = int(input())
  s = [input() for i in range(n)]
  st = set(s)
  ans = ""
  for i in range(n):
    res = "0"
    for j in range(len(s[i])-1):
      a, b = s[i][:j+1], s[i][j+1:]
      if a in st and b in st:
        res = "1"
    ans += res
  print(ans)
