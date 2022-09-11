# link : https://codeforces.com/problemset/problem/1183/A
# author : Mohamed Ibrahim
  
n = int(input())
while (sum(map(int,str(n)))%4): n += 1
print(n)
