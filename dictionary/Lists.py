//link : https://www.hackerrank.com/challenges/python-lists/problem

listt = []
cases = int(input())
for i in range(cases):
    line = input().split()
    oper = line[0]
    if oper == "print":
        print(listt)
    elif oper =="append":
         listt.append(int(line[1]))
    elif oper =="insert":
        listt.insert(int(line[1]),int(line[2]))
    elif oper == "sort":
        listt.sort()
    elif oper == "reverse":
        listt.sort(reverse = True)
    elif oper == "pop":
        listt.pop()
    elif oper == "remove":
        listt.remove(int(line[1]))


        
