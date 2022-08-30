#link   : https://codeforces.com/problemset/problem/1702/B
#author : Mohamed Ibrahim

for _ in range(int(input())):
    s = set()
    days = 1
    for x in input():
        s.add(x)
        if len(s) == 4:
            days += 1
            s = {x}
    print(days)
  
