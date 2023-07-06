# link   : https://leetcode.com/problems/prime-subtraction-operation/description/
# author : Mohamed ibrahim

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        n = max(nums)
        N = [True]*(n)
        p = 2
        while p*p <= n:
            if N[p] == True:
                for i in range(p*p , n , p):
                    N[i] = False
            p+=1
        for i in range(2,len(N)): 
            if N[i]:primes.append(i)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]: continue
            
            index = bisect_right(primes, nums[i] - nums[i + 1])
            if index >= len(primes) or nums[i] - primes[index] < 1: return False
            nums[i] -= primes[index]
        return True
