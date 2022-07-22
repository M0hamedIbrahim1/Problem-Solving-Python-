#link   : https://codeforces.com/problemset/problem/1494/A
#author : Mohamed Ibrahim

n=int(input())

l=[[-1,-1,-1], [-1,-1,1], [-1,1,-1], [-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]]

for i in range(n):
    a=input()
    ans=0
    for j in l:
        cnt=0
        pos=1
        for k in a:
            cnt+=j[ord(k)-65]
            if cnt < 0: pos=0
        if pos==1 and cnt==0: ans=1
    
    print("YES" if ans==1 else "NO")
