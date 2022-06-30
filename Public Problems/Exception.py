#Link : https://www.hackerrank.com/challenges/exceptions/problem

for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
