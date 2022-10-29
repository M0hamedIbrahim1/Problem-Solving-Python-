# Link   : https://codeforces.com/problemset/problem/1698/C
# author : Mohamed Ibrahim



x=int(input())
for i in range (x):
    y=int(input())
    z=list(map(int,input().split()))
    z.sort()
    if z[-1] + z[-2] + z[-3] not in z:
        print("NO")
    elif z[0] + z[1] + z[2] not in z:
        print("NO")
    elif z[0] + z[1] + z[-1] not in z:
        print("NO")
    elif z[0] + z[-2] + z[-1] not in z:
        print("NO")
    else:
        print("YES")
        
        
        
        
        
        
        
        
      
        
