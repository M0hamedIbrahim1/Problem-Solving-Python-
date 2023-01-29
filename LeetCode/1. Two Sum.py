# link   : https://leetcode.com/problems/two-sum/description/
# author : Mohamed Ibrahim



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(numbers)):
            c = target-numbers[i]
            if c in d:
              return [i,d[c]]
            d[numbers[i]] = i

            
