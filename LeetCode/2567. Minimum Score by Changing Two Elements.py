# Link   : https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/
# author : Mohamed Ibrahim

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-2] - nums[1] , nums[-3]-nums[0] , nums[-1] - nums[2])
      
