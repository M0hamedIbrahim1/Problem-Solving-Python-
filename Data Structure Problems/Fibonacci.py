# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/O
# Author : Mohamed Ibrahim

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
print(fibonacci(int(input())-1))


