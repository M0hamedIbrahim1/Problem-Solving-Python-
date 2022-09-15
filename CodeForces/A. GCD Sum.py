# link : https://codeforces.com/problemset/problem/1498/A
# author : Mohamed Ibrahim

import math
for _ in range(int(input())):
    n = input()
    while math.gcd(int(n),sum([int(i) for i in n]))==1:
        n = str(int(n)+1)
    print(n)
    
