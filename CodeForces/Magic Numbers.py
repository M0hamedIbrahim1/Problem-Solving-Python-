#link   : https://codeforces.com/problemset/problem/320/A
#author : Mohamed Ibrahim

n = input()
if (n.count("1") + n.count("14") + n.count("144")) == len(n):
    print("YES")
else:
    print("NO")
