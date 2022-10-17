# link   : https://codeforces.com/problemset/problem/264/A
# author : Mohamed Ibrahim


s = input()
for i in range(len(s)):
    if s[i] == 'r':
        print(i+1)

i = len(s)-1
while i >= 0:
    if s[i] == 'l':
        print(i+1)
    i -= 1
    
    
    
