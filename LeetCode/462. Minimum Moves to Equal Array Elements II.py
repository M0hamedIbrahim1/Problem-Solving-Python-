# link   : https://leetcode.com/problems/make-k-subarray-sums-equal/description/
# author : Mohamed Ibrahim

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
      median = sorted(nums)[len(nums)//2]
      return sum(abs(num - median) for num in nums)
