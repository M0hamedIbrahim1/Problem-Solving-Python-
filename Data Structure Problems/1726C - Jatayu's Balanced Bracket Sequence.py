# link   : https://codeforces.com/problemset/problem/1726/C 
# author : Mohamed Ibrahim



tc = int(input())
for i in range(tc):
    n = int(input())
    lst = input()
    out = 0
    for i in range(2*n-1):
        if lst[i] == "(" and lst[i+1] == ")":
            out+=1
    print(n-out+1)
    
    
    
    
