# link    : https://codeforces.com/problemset/problem/1511/C
# author  : Mohamed Ibrahim

N=input()
a=input().split()
b=input().split()
for x in b:    
    i=a.index(x)    
    print(i+1);    
    a[:i+1]=[x]+a[:i]
 
 
 
  
