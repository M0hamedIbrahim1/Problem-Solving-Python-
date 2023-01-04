# link : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/U
# author : Mohamed Ibrahim


def resc(w,listWeight,listValue,items):
  if w == 0 or items == 0:
    return 0
  if listWeight[items-1] > w:
    return resc(w,listWeight,listValue,items-1)
  else:
    return max(
    
    listValue[items-1]+resc(w-listWeight[items-1],listWeight,listValue,items-1),
    resc(w,listWeight,listValue,items-1),
    )


n , W = map(int,input().split())
lst_W = []
lst_V = []
for _ in range(n):
  w , v = map(int,input().split())
  lst_W.append(w)
  lst_V.append(v)
print(resc(W,lst_W,lst_V,n))


