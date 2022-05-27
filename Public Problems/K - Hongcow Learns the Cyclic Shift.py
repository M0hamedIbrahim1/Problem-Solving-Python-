#link : https://codeforces.com/group/LKPSX7Pt2W/contest/323155/problem/K

a=input()
s=set()
for i in range(len(a)):
    a=a[-1]+a[:-1]
    s.add(a)
print(len(s))
