# link   : https://leetcode.com/problems/first-unique-character-in-a-string/
# author : Mohamed Ibrahim


class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i in s:
            res[i] = res.get(i,0)+1
        for j in range(len(s)):
            if res[s[j]] == 1:
                return j
        return -1
        
