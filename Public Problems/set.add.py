#Link : https://www.hackerrank.com/challenges/py-set-add/problem
#Author : Mohamed Ibrahim

size = int(input())
sett=set()
for i in range(size):
    country = input()
    sett.add(country)
print(len(sett))
