 # link   : https://codeforces.com/problemset/problem/628/B
 # author : Mohamed Ibrahim
 
 
 

lst = [int(i) for i in input()]
size = len(lst)
cnt = lst.count(0)+lst.count(4)+lst.count(8)
for i in range(1,size):
  if (lst[i-1]*10 + lst[i]) % 4 == 0:
    cnt += i
print(cnt)



