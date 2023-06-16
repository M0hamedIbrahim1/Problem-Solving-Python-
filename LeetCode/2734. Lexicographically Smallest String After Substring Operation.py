# link   : https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description/
# author : Mohamed Ibrahim

class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s) and s[i] == 'a':
            i+=1
        if i == len(s):
            s[-1] = 'z'
        while i < len(s) and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i+=1
        return ''.join(s)
