#link   : https://www.hackerrank.com/challenges/zipped/problem
#author : Mohamed Ibrahim

size, t = map(int, input().split()) 
lst = []
for _ in range(t):
    lst.append(map(float, input().split())) 

for i in zip(*lst): 
    print( sum(i)/len(i) )
