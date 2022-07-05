#link   : https://codeforces.com/problemset/problem/1397/A
#author : Mohamed Ibrahim

for i in range(int(input())):
    n=int(input())
    s=""
    flag = 1
    for i in range(n):
        s+=input()
    for k in set(s):
        if s.count(k) % n != 0 :
            print("NO")
            flag = 0
            break
    if flag == 1:
        print("YES")
        
        
