# link : 
# author : Mohamed Ibrahim

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        mn = float('inf')
        if ones:return len(nums)-ones
        for i in range(len(nums)-1):
            g = nums[i]
            for j in range(i+1 , len(nums)):
                g = gcd(g,nums[j])
                if g == 1:
                    mn = min(mn , j -i)
                    break
        return -1 if mn == float('inf') else mn+len(nums)-1
