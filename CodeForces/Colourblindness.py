#link : https://codeforces.com/problemset/problem/1722/B
#author : Mohamed Ibrahim

n = int(input())
for i in range(n):
    length = int(input())
    s1, s2 = input().replace('G', 'B'), input().replace('G', 'B')
    print('YES' if s1 == s2 else 'NO')
    
