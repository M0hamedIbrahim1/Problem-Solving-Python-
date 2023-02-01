# link   : https://leetcode.com/problems/combination-sum-ii/description/
# author : Mohamed Ibrahim


class Solution :

    def combinationSum2(self, candidates, target):
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
        
    def combine_sum_2(self, nums, start, path, result, target):

        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])



