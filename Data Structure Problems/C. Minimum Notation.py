# Link   : https://codeforces.com/problemset/problem/1730/C
# author : Mohamed Ibrahim


for _ in range(int(input())):
  s = input()
  a = list(int(x) for x in s)
  a.reverse()
  m = 10
  for i in range(len(s)):
    if a[i] > m:
      a[i] = min(a[i]+1,9)
    m = min(a[i],m)
  print(''.join(str(x) for x in sorted(a)))


