#link :   https://www.hackerrank.com/challenges/piling-up/problem
#author : Mohamed Ibrahim

for t in range(int(input())):
    input()
    a = list(map(int, input().split()))
    l = len(a)
    i = 0
    while i < l - 1 and a[i] >= a[i+1]:
        i += 1
    while i < l - 1 and a[i] <= a[i+1]:
        i += 1
    if i == l-1:
        print("Yes")
    else:
        print("No")
