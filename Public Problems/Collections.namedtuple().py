#link : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#author : Mohamed Ibrahim

n = int(input())
summation = 0
input_1 = input().split()
for i in range(n):
    input_2 = input().split()
    summation = summation + int(input_2[1])
print(summation/n)
