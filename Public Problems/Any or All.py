#link   : https://www.hackerrank.com/challenges/any-or-all/problem
#author : Mohamed Ibrahim

n = int(input())
lst = input().split(" ")
print(all(int(i)>=0 for i in lst) and any(i == i[::-1]for i in lst))
