# link   : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/I
# author : Mohamed Ibrahim



def resc(vowels,l,c):
  if len == l:
    return c
  if s[l].lower() in vowels:
    c+=1
  return resc(vowels,l+1,c)

vowels = ['a', 'e', 'i', 'o', 'u']
s = input()
len = len(s)
cnt = 0
print(resc(vowels,0,cnt))


