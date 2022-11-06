# Link   : https://codeforces.com/problemset/problem/1237/B
# author : Mohamed Ibrahim



n = int(input())
lst_in = list(map(int,input().split()))
lst_out = list(map(int,input().split()))
i = 0 
j = 0
s = set()
while j < n:
  if lst_in[i] in s:
    i+=1
  elif lst_in[i] != lst_out[j]:
    s.add(lst_out[j])
    j+=1
  else:
    i+=1
    j+=1
print(len(s))



