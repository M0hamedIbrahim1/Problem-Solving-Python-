# link   : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# author : Mohamed Ibrahim

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t,cnt,mx = '',0,0
        for i in s:
            if i not in t:
                t+=i
                cnt+=1
            else:
                mx = max(mx,cnt)
                indx = t.index(i)+1
                t+=i
                t = t[indx:]
                cnt -=indx 
                cnt+=1

        return (max(mx,cnt))
        
        
        
