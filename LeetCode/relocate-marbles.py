# link : https://leetcode.com/contest/biweekly-contest-108/problems/relocate-marbles/
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = list(set(nums))
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = 1
        for i in range(len(moveFrom)):
            del d[moveFrom[i]]
            d[moveTo[i]] = 1

        return sorted(d.keys())
