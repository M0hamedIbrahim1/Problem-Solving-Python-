# link   : https://codeforces.com/problemset/problem/1676/H2
# author : Mohamed Ibrahim



from bisect import bisect

for tcase in range(int(input())):

    n = int(input())
    a, b = [], []
    ans = 0

    for x in map(int, input().split()):

        ans += len(a) - bisect(a, x-1)
        ans += len([y for y in b if y >= x])
        b.append(x)

        if len(b) * len(b) > len(a):
            a.extend(b)
            b = []
            a.sort()

    print(ans)


# other solutation

 def invs(a):
  l = len(a)
  if l == 1:
    return 0
  x = a[:l // 2]
  y = a[l // 2:]
  tot = invs(x) + invs(y)

  x.sort()
  y.sort()
  j = 0
  for i in x:
    while j < len(y) and y[j] <= i:
      j += 1
    tot += j
  return tot

for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  print(invs(a))   

