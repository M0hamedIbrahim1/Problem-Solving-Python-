#link : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
#Author : @Mohamed Ibrahim

from collections import OrderedDict
dictt = OrderedDict()

size = int(input())
for i in range(size):
    inputt = input().split()
    item_name = " ".join(inputt[:-1])
    price = int(inputt[-1])
    if dictt.get(item_name):
        dictt[item_name]+=price
    else:
        dictt[item_name] = price
for x,y in dictt.items():
    print(x,y)
