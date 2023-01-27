# link   : https://leetcode.com/problems/product-of-array-except-self/description/?languageTags=python
# author : Mohamed Ibrahim



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix_sum = 1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=prefix_sum
            prefix_sum*=nums[i]
        return ans
        
