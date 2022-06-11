#link   : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
#author : Mohamed Ibrahim

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    inputt = input().split()
    if inputt[0] == 'pop': s.pop()
    elif inputt[0] == 'remove': s.remove(int(inputt[1]))
    elif inputt[0] == 'discard': s.discard(int(inputt[1]))
print(sum(s))
