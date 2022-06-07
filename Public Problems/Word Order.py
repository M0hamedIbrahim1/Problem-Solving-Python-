#link : https://www.hackerrank.com/challenges/word-order/problem
#Aurhor : Mohamed Ibrahim

from collections import OrderedDict
dictt = OrderedDict()
size = int(input())
for i in range(size):
    word = input()
    if(dictt.get(word)):
        dictt[word] = dictt[word]+1
    else:
        dictt[word] = 1
print(len(dictt))
for y in dictt.values():
    print(y,end=' ')
