# link   : https://codeforces.com/problemset/problem/559/B
# author : Mohamed Ibrahim

def resc(s):
  if len(s) % 2: return s
  a = resc(s[:len(s)//2])
  b = resc(s[len(s)//2:])

  return a+b if a < b else b+a
s1 = input()
s2 = input()
print("YES" if resc(s1) == resc(s2) else "NO" )


