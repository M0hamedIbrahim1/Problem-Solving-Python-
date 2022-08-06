#link   : https://codeforces.com/problemset/problem/622/B
#author : Mohamed Ibrahim

h,m = map(int,input().split(':'))
a = int(input())

t = (h*60+m+a)%(60*24)
print("{:02d}:{:02d}".format(t//60, t%60))
