#link   : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
#author : Mohamed Ibrahim

n = int(input())

for i in range(n):
    s = input()
    print("+91",s[-10:-5],s[-5:])
