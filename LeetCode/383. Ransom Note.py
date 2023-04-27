# link : https://leetcode.com/problems/ransom-note/description/
# author : Mohamed Ibrahim

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1
        
