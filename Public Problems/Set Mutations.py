#link   : https://www.hackerrank.com/challenges/py-set-mutations/problem
#author : Mohamed Ibrahim

inp = int(input())
S = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd, _ = input().split()
    s = set(map(int, input().split()))
    if(cmd == "intersection_update"):
        S.intersection_update(s)
    elif(cmd == "update"):
        S.update(s)
    elif(cmd == "symmetric_difference_update"):
        S.symmetric_difference_update(s)
    elif(cmd == "difference_update"):
        S.difference_update(s)

print(sum(S))
