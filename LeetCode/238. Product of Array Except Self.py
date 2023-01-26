# link   : https://leetcode.com/problems/product-of-array-except-self/description/?languageTags=python
# author : Mohamed Ibrahim



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,n=1,len(nums)
        answer=[1]
        for i in range(1,n):
            prefix*=nums[i-1]
            answer.append(prefix)
        postfix=1
        for i in range(n-2,-1,-1):
            postfix*=nums[i+1]
            answer[i]*=postfix
        return answer
        
        
        
