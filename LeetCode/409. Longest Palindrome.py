# link   : https://leetcode.com/problems/longest-palindrome/description/
# author : Mohamed Ibrahim


class Solution:
    def longestPalindrome(self, s):
        ans = 0 
        for i in collections.Counter(s).values():
            ans+= i//2 *2
            if ans % 2 == 0 and i % 2 == 1:
                ans+=1
        return ans
        
