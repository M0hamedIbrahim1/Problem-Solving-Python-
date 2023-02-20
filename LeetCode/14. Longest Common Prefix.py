# author : Mohamed Ibrahim
# Link   : https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        lst = zip(*strs)
        for i in lst:
            if len(set(i)) == 1:
                s+=i[0]
            else:
                break
        return s
      
