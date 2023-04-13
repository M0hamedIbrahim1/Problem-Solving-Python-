# link : https://leetcode.com/problems/longest-palindromic-substring/description/
# author : Mohamed ibrahim

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):

            # checking for ODD
            mx_length = self.check(s,i , i)
            if len(res) < len(mx_length):
                res = mx_length

            # checking for EVEN
            mx_length = self.check(s,i , i+1)
            if len(res) < len(mx_length):
                res = mx_length
        return res
    def check(self,s,i , j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            j+=1
            i-=1
        return s[i+1 : j]
        
        
