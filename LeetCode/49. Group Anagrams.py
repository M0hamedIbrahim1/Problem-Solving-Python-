# link   : https://leetcode.com/problems/group-anagrams/
# author : Mohamed Ibrahim


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        s = ''
        for i in strs:
            s = ''.join(sorted(i))
            if s not in d :
                d[s] = []
            d[s].append(i)
        return d.values()

      
      
