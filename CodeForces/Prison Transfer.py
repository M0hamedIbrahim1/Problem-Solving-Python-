# link : https://codeforces.com/problemset/problem/427/B
# author : Mohamed Ibrahim

n,t,c=map(int,input().split());x=0;z=0

for i in map(int,input().split()):
    if i<=t:
        x+=1
    else:
        x=0
    if x>=c:    
        z+=1    
print(z)  
