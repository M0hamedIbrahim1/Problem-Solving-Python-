def unique_list(l):
  x = []
  for val in l:
    if val not in x:
      x.append(val)
  return x

print(unique_list([10,30,30,40,50,60,60,10,20])) 
