#link   : https://codeforces.com/problemset/problem/1624/B
#author : Mohamed Ibrahim

for i in range(int(input())):
    a,b,c=map(int,input().split()) 
    f=2*b
    if (((f-c)%a==0) and (f>c)) or ((a+c)%f==0) or (((f-a)%c==0)and(f>a)):
        print("YES")
    else:
        print("NO")
