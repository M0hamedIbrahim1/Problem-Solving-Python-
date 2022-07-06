#link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
#author : Mohamed Ibrahim

n , a = input(),set(map(int,input().split()))
N , b = input(),set(map(int,input().split()))
print(len(a.symmetric_difference(b)))
