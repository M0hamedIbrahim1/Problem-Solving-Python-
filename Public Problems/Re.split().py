#link : https://www.hackerrank.com/challenges/re-split/problem
#author : Mohamed Ibrahim

Split = r"[,.]"	# Do not delete 'r'.
import re
print("\n".join(re.split(Split, input())))
