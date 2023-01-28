# link   : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# author : Mohamed Ibrahim


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target : return [i+1,j+1]
            if numbers[i]+numbers[j] > target:j-=1
            else:i+=1
            
            
            
