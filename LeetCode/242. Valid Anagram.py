# link    : https://leetcode.com/problems/valid-anagram/description/
# author : Mohamed Ibrahim

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for S in set(s):
            if s.count(S) != t.count(S):
                return False
        return True
        
        
