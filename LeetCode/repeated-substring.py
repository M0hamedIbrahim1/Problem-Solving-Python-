# link : https://leetcode.com/problems/repeated-substring-pattern/description/
# author : Mohamed Ibrahim

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        res = ""
        n = len(s)
        indx = n//2
        if n % 2 == 0 : indx += 1


        for i in range(len(s)):
            if i == indx:return False
            res+=s[i]
            if res * (n//(i+1)) == s:return True
