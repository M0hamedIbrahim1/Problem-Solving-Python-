#link    : https://codeforces.com/problemset/problem/1559/B
#author  : Mohamed Ibrahim
for i in range(int(input())):
    n=int(input())
    a=input()
    b=""
    if a=="?"*n:
        a=a.replace("?","R",1)
        
    while "?" in a:
        a=a.replace("R?","RB")
        a=a.replace("B?","BR")
        a=a.replace("?B","RB")
        a=a.replace("?R","BR")
        
    print(a)
