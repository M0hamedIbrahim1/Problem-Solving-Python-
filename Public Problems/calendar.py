#link : https://www.hackerrank.com/challenges/calendar-module/problem
#author : Mohamed Ibrahim

import calendar
n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
#for fun MY DAYYYYY : 04 13 2001 :) FRIDAY 
# Know your Day :) 
