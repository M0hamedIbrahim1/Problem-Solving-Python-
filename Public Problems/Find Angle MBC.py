#link   : https://www.hackerrank.com/challenges/find-angle/problem
#author : Mohamed Ibrahim

import math
AB,BC=int(input()),int(input())
hy = math.hypot(AB,BC)                       
res = round(math.degrees(math.acos(BC/hy))) 
degree=chr(176)                    
print(res,degree, sep='')
