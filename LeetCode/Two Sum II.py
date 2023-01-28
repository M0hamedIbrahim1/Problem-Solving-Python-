# link   : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# author : Mohamed Ibrahim


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target : return [i+1,j+1]
            if numbers[i]+numbers[j] > target:j-=1
            else:i+=1
            

            
# Using Recursion

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.resc(numbers,0,len(numbers)-1,target)
    def resc(self,numbers,i,j,t):
        sum = numbers[i]+numbers[j]
        if sum == t: return [i+1,j+1]
        elif sum > t:
            return self.resc(numbers,i,j-1,t)
        else:
            return self.resc(numbers,i+1,j,t)            
