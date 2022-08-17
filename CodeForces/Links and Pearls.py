#link : https://codeforces.com/problemset/problem/980/A
#author : Mohamed Ibrahim

s = input()
print("YES" if s.count('-')%max(s.count('o'), 1)==0 else "NO")
