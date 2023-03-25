# link   : https://leetcode.com/problems/missing-number/description/
# author : Mohamed Ibrahim


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        
        
