# link   : https://leetcode.com/problems/roman-to-integer/description/
# author : Mohamed Ibrahim

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400, 'CM':900}
        SUM,i = 0,0
        while i < len(s):
            if  i < len(s)-1:
                if d.get(s[i]+s[i+1],0):
                    SUM+=d[s[i]+s[i+1]]
                    i+=1
                else:
                    SUM+=d[s[i]]
            else:
                SUM+=d[s[i]]
            i+=1
        return SUM
        
        
        
