#link   : https://www.hackerrank.com/challenges/symmetric-difference/problem
#author : Mohamed Ibrahim

n = int(input())
a = set(input().split())
m = int(input())
b = set(input().split())

x = a.difference(b)
y = b.difference(a)
u = x.union(y)
diff = sorted(u,key=int)
print("\n".join(diff))
