# link   : https://codeforces.com/problemset/problem/1598/C
# author : Mohamed Ibrahim

for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    mean_2 = (2*sum(ai))/n
    d = {}
    output = 0
    for i in ai:
        output+= d.get(i,0)
        d[mean_2 - i] = d.get(mean_2-i,0) + 1
    print(output)
    
