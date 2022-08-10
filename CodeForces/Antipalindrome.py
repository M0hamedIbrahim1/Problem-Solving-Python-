# link   : https://codeforces.com/problemset/problem/981/A
# author : Mohamed Ibrahim

s = input()
print(0 if s[1:]==s[:-1] else len(s)-1 if s==s[::-1] else len(s))
