//link:https://www.hackerrank.com/challenges/finding-the-percentage/problem

dictt = {}
size = int(input())
for i in range(size):
    inputt = input().split()
    name, scores = inputt[0], inputt[1:]
    scores = map(float,scores)
    dictt[name]=scores
inputt_name = input()
val = list(dictt[inputt_name])
print("{0:.2f}".format(sum(val)/(len(val))))

   

