# link   : https://leetcode.com/problems/jump-game/
# author : Mohamed ibrahim

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = n = len(nums)-1

        for i in range(n,-1,-1):
            if nums[i]+i >= goal:
                goal = i
        return True if goal == 0 else False
        
        
