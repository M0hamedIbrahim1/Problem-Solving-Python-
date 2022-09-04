#link   : https://codeforces.com/problemset/problem/1474/A
#author : Mohamed Ibrahim

t=int(input())
for i in range(t):
    n=int(input())
    y=input()
    s="1"
    for i in range(1,len(y)):
        if int(y[i])+1==int(y[i-1])+int(s[-1]):
            s+="0"
        else:
            s+="1"
    print(s)
    
