# link   : https://leetcode.com/problems/subsets/description/
# author : Mohamed Ibrahim




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        def powerSet(nums, i, subSet): 
            if i==n:
                result.append(subSet) 
                return 
            powerSet(nums, i+1, subSet) 
            powerSet(nums, i+1, subSet + [nums[i]]) 
        powerSet(nums, 0, [])
        return result 
        
        
        
        
        
        
