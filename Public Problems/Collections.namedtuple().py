#link : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#author : Mohamed Ibrahim

from collections import namedtuple

n_students = int(input())
header = input().split()
students = namedtuple('student',header)
summation = 0
for i in range(n_students):
    inp_1, inp_2, inp_3,inp_4 = input().split()
    student = students(inp_1, inp_2, inp_3,inp_4)
    summation += int(student.MARKS)
print('{:.2f}'.format(summation/n_students))



n = int(input())
summation = 0
input_1 = input().split()
for i in range(n):
    input_2 = input().split()
    summation = summation + int(input_2[1])
print(summation/n)
