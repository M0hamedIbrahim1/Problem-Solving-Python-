# link   : https://codeforces.com/problemset/problem/1658/B
# author : Mohamed Ibrahim

import math
for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        print((math.factorial(n//2)**2)%998244353)
    else:
        print(0)
 
