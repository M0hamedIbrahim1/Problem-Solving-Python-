# link   : https://leetcode.com/problems/palindrome-partitioning/description/
# author : Mohamed Ibrahim


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.resc(s,[],res)
        return res
    def resc(self,s,path,res):
        if s == "":
            res.append(path)
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                self.resc(s[i+1:],path+[s[:i+1]],res)
                
                
                
