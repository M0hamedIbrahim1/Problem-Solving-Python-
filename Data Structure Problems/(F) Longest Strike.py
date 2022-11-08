# https://codeforces.com/problemset/problem/1676/F
# author : Mohamed Ibrahim

import collections
 
for _ in range(int(input())):
    _, k = map(int, input().split())
    c = collections.Counter(sorted(map(int, input().split())))
    d = collections.Counter()
    for i, x in c.items():
        if x >= k:
            d[i] = d[i - 1] + 1
    if not d:
        print(-1)
        continue
    r, u = d.most_common(1)[0]
    print(r - u + 1, r)
    
    
    
    
