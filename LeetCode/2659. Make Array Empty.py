# link   : https://leetcode.com/problems/make-array-empty/description
# author : Mohamed Ibrahim

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n, res, turn = len(nums), 1, 1
        idx = sorted(range(n), key=lambda x: nums[x])
        for i in range(1, n):
            turn += idx[i] < idx[i-1]
            res += turn
        return res
        
