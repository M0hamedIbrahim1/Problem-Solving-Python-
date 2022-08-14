#link : https://codeforces.com/problemset/problem/373/A
#author : Mohamed Ibrahim

k,s=int(input()),''
for i in range(4):
    s=s+input()
 
for i in range(1,10):
    if(s.count(str(i))>k*2):
        exit(print('NO'))
print('YES')
