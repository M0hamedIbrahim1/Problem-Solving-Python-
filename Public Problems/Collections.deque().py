#link   : https://www.hackerrank.com/challenges/py-collections-deque/problem
#author : Mohamed Ibrahim

# deque can be used to add or remove elements from both ends
from collections import deque
d = deque()
for i in range(int(input())):
    inputt = input().split()
    if inputt[0]=="append":
        d.append(inputt[1])
    elif inputt[0]=="appendleft":
        d.appendleft(inputt[1])
    elif inputt[0]=="pop":
        d.pop()
    elif inputt[0]=="popleft":
        d.popleft()
print(*d)
