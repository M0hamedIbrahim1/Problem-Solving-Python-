#link   : https://codeforces.com/problemset/problem/376/A
#author : Mohamed Ibrahim

s=input()
a=s.index("^")
sum=0
for i in range(len(s)):
    if s[i]!="=" and s[i]!="^":
        sum+=int(s[i])*(i-a)
if sum<0:
    print("left")
elif sum>0:
    print("right")
else:
    print("balance")
