# link   : https://leetcode.com/problems/maximum-strength-of-a-group/description/
# author : Mohamed Ibrahim

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:return nums[0]
        nums.sort()
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        if not pos and not neg:
            return 0

        prod_pos = prod(pos)
        prod_neg = 0
        if len(neg) % 2 and len(neg) > 1:
            prod_neg = prod(neg[:-1])
        elif len(neg) > 1:
            prod_neg = prod(neg)
        if not neg:prod_neg=0
        if not pos:prod_pos=0
        return max(prod_pos , prod_pos*prod_neg , prod_neg)
      
