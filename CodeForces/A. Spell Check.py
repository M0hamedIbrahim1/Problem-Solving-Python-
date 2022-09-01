#link ` : https://codeforces.com/problemset/problem/1722/A
#author : Mohamed Ibrahim


for _ in range(int(input())):
    n=int(input())
    d=sorted("Timur")
    s=sorted(input())
    print("YES" if d==s else "NO")
