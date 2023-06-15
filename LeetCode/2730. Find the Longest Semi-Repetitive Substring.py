# link : https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/
# author : Mohamed Ibrahim

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        pairs = set()
        res = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                pairs.add((i , i+1))
        if not pairs or len(pairs) == 1:return len(s)
        for left , right in pairs:
            cnt = 2 
            left-=1
            right+=1
            while left >= 0 and s[left] != s[left+1]:
                left-=1
                # cnt+=1
            while right < len(s) and s[right] != s[right-1]:
                right+=1
                # cnt+1

            res = max(res , right - left)
        return res-1


