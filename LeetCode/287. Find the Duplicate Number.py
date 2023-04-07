# link   : https://leetcode.com/problems/find-the-duplicate-number/description/
# author : Mohamed Ibrahim

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast
      
      
