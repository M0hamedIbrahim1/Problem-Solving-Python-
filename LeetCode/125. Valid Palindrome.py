# link   : https://leetcode.com/problems/valid-palindrome/description/
# author : Mohamed Ibrahim


class Solution(object):
    def isPalindrome(self, s):
        new_s = ""
        for i in s:
            if i.isalpha():
                new_s+=i.lower()
            elif i.isnumeric():
                new_s+=i
        return self.resc(0,new_s)
    def resc(self,i,s):
        if i >= len(s)/2:
            return True
        elif s[i] != s[len(s)-i-1]:
            return False
        else:
            return self.resc(i+1,s)
            
            
