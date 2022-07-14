#link   : https://www.hackerrank.com/challenges/ginorts/problem
#author : Mohamed Ibrahim

lst = input()
Small,Cap,Even,Odd = [],[],[],[]
for i in lst:
    if i.islower():
        Small.append(i)
    elif i.isupper():
        Cap.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0 :
            Even.append(i)
        else:
            Odd.append(i)
x = sorted(Small)+sorted(Cap)+sorted(Odd)+sorted(Even)   
for i in x:
    print(i,end="")
