#link   : https://codeforces.com/problemset/problem/1674/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    s=input()
    
    a=ord(s[0])-96
    b=ord(s[1])-96
    if a<b:
        print(25*(a-1)+b-1)
    else:
        print(25*(a-1)+b)
