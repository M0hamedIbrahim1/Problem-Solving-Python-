from itertools import groupby
List=input()
for i, items in groupby(List):    
    print(tuple([len(list(items)),int(i)]), end=' ')

   -------------------------------- 

# from itertools import groupby
# N = input()
# for k,g in groupby(N):
#     print(list(k))  
    
# 1222311
['1']
['2']
['3']
['1']
   --------------------------------- 
    
# from itertools import groupby
# N = input()
# for k,g in groupby(N):
#     print(list(g))

# 1222311

['1']
['2', '2', '2']
['3']
['1', '1']
-------------------------------------
