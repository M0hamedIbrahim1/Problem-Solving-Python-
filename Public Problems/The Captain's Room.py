#link  : https://www.hackerrank.com/challenges/py-the-captains-room/problem
#author: Mohamed Ibrahim

n = int(input())
lst = list(map(int,input().split()))
# for i in set(lst):
#     if lst.count(i) != n:
print(min(lst,key = lst.count))
