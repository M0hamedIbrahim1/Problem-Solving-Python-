#link   : https://codeforces.com/problemset/problem/1373/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    s=input()
    print('DA' if min(s.count('0'),s.count('1'))%2 else 'NET')
