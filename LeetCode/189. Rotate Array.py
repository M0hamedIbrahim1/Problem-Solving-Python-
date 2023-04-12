# link   : https://leetcode.com/problems/rotate-array/
# author : Mohamed Ibrahim

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
