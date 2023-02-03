# link : https://leetcode.com/problems/permutation-in-string/description/
# author : Mohamed Ibrahim



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i,start,end = 0,0,0
        d = dict()
        S,s = ''.join(sorted(s1)) ,''
        for i in s1:d[i] = 1
        while end < len(s2):
            if d.get(s2[end],0):
                s+=s2[end]
            else:
                s = ''
                start = end+1

            if end+1 - start == len(s1):
                if ''.join(sorted(s)) == S:
                    return True
                else:
                    s = s[1:]
                    start+=1
            end+=1

        return False
        
        
