
for _ in range(int(input())):
  a = int(input())
  k = 1
  while k*k < a:
    k += 1
  p = k*k
  if p - k + 1 <= a:
    print(k, p-a+1)
  else:
    print(k-((p-k+1)-a), k)
    
