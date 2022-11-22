# link   : https://codeforces.com/problemset/problem/1760/C
# author : Mohamed Ibrahim


for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    s = sorted(li)
    for i in li:
        if(i!=s[n-1]):
            print(i - s[n-1],end =" ")
        else:
            print(i-s[n-2],end= " ")
            
            
            
