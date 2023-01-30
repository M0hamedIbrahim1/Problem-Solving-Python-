# link   : https://leetcode.com/problems/subsets-ii/description/
# author : Mohamed Ibrahim



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        def powerSet(nums, i, subSet): 
            if i==n:
                if subSet not in result:
                   result.append(subSet) 
                return 
            powerSet(nums, i+1, subSet) 
            powerSet(nums, i+1, subSet + [nums[i]])
        nums.sort() 
        powerSet(nums, 0, [])
        return result 
        
        
