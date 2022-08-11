#link   : https://codeforces.com/problemset/problem/387/A 
#author : Mohamed Ibrahim

I = lambda: map(int, input().split(':'))
 
h, m = I()
dh, dm = I()
h, m = h-dh, m-dm
h, m = (h+m//60)%24, m%60
 
print(f'{h:02}:{m:02}')
