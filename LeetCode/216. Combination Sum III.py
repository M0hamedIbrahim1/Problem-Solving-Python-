# link   : https://leetcode.com/problems/combination-sum-iii/description/
# author : Mohamed ibrahim


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = range(1,10)
        self.combinationSum(nums,k,n,[],res)
        return res
    def combinationSum(self,nums,k,target,path,res):
        if target == 0 and k == 0:
            res.append(path)
        for i in range(len(nums)):
            self.combinationSum(nums[i+1:],k-1,target-nums[i],path+[nums[i]],res)
            
            
