# link    : https://codeforces.com/problemset/problem/522/B
# author : Mohamed Ibrahim

T = int(input())
h = []
w = []
SUM = 0
for i in range(T):
  width,height = map(int,input().split())
  SUM+= width
  w.append(width)
  h.append(height)
H_S = h.copy()
H_S.sort()
for i in range(T):
  a = SUM-w[i]
  b = H_S[T-1]
  if h[i] == H_S[T-1]:
    b = H_S[T-2]
  print(a*b,end = " ")

  
