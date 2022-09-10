# link   : https://codeforces.com/problemset/problem/1719/A
# author : Mohamed Ibrahim


winner = ['Tonya', 'Burenka']
for _ in range(int(input())):
    print(winner[sum(map(int, input().split())) % 2])
    
