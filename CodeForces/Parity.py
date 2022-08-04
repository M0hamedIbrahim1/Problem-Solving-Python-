#link : https://codeforces.com/problemset/problem/1110/A
#author : Mohamed Ibrahim

b = int(input().split()[0])
n = list(map(int, input().split()))
if b%2!=0: n=sum(n)
else : n=n[-1]
print('odd' if n % 2 else 'even')
