#link   : https://codeforces.com/group/jfviGllBoY/contest/389763/problem/E
#author : Mohamed Ibrahim

s,h = map(int,input().split())
lst = list(map(int,input().split()))
Sum = 0
for i in lst:
    if i > h:
        Sum+=2
    else:
        Sum+=1
print(Sum)
