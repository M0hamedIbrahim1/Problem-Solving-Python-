summ = 0
n = input()
I =list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
for i in I:
    if i in A:
        summ+=1
    elif i in B:
        summ-=1
print(summ)
