for _ in range(int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    i=0;ans=0
    while i<x and a[i]==0:i+=1
    for j in range(i,x-1):
        if a[j]:ans+=a[j]
        else:ans+=1
    print(ans)  
