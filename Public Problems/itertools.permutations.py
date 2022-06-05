#link : https://www.hackerrank.com/challenges/itertools-permutations/problem
#Author : @Mohamed Ibrahim
from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
for i in permutations:
    print("".join(i))
