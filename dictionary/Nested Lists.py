//link : https://www.hackerrank.com/challenges/nested-list/problem
lis = []
scores = set()
temp_lis = []
for i in range(int(input())):
    name = input()
    grade = float(input())
    lis.append([name,grade])
    scores.add(grade)

second_lowest = sorted(scores)[1]
for name, grade in lis:
    if grade == second_lowest:
        temp_lis.append(name)
for name in sorted(temp_lis):
    print(name,end='\n')
    

