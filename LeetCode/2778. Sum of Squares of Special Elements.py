# link   : https://leetcode.com/contest/weekly-contest-354/problems/sum-of-squares-of-special-elements/
# author : Mohamed Ibrahim

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1,len(nums)+1):
            if n % i == 0:
                res+= (nums[i-1]*nums[i-1])
        return res
