# link   : https://leetcode.com/problems/permutations/description/
# author : Mohamed Ibrahim


class Solution(object):
    def permute(self, nums):
        res = []
        self.resc(nums,[],res)
        return res
    def resc(self,nums,path,res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            self.resc(nums[:i] + nums[i+1:],path+[nums[i]],res)
            
            
            
