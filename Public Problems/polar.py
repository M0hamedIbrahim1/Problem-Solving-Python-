#link   : https://www.hackerrank.com/challenges/find-angle/problem
#author : Mohamed Ibrahim
import cmath
inp = complex(input().strip())

print(cmath.polar(inp)[0])
print(cmath.polar(inp)[1])
