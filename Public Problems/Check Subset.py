#link   : https://www.hackerrank.com/challenges/py-check-subset/problem
#author : Mohamed Ibrahim

for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))
