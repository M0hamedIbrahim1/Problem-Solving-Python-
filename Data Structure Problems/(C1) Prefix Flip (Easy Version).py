# link   : https://codeforces.com/problemset/problem/1381/A1
# author : Mohamed Ibrahim


for _ in range(int(input())):
    num = int(input())
    a = input()
    b = input()
    ans = [-1]
    for i in range(num):
        if a[i] != b[i]:
            ans += [i + 1, 1, i + 1]
    
    ans[0] = len(ans) - 1 
    print(*ans)      
    
    
    
