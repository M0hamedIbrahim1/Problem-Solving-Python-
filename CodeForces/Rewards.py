# link : https://codeforces.com/problemset/problem/448/A
# author : Mohamed Ibrahim

i=lambda:sum(map(int,input().split()))
print('YNEOS'[((i()+4)//5+(i()+9)//10)>i()::2])
