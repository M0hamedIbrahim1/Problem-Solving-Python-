#link : https://www.hackerrank.com/challenges/itertools-product/problem
#author : @Mohamed Ibrahim

string = ""
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in a:
    for j in b:
        string += f"{(i, j)} "
print (string)
