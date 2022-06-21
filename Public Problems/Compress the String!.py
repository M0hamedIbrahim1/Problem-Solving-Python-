from itertools import groupby
List=input()
for i, items in groupby(List):    
    print(tuple([len(list(items)),int(i)]), end=' ')
