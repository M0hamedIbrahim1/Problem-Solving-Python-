# link   : https://codeforces.com/problemset/problem/1647/A
# author : Mohamed Ibrahim

for x in range(int(input())):
    n=int(input())
    x=n%3
    n=n//3
    s="21"*n
    if x==1:
        s='1'+s
    elif x==2:
        s+='2'
    print(s)
    
