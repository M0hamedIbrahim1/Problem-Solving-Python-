# link   : https://leetcode.com/problems/prime-pairs-with-target-sum/description/
# author : Mohamed Ibrahim

class Solution:
    def findPrimePairs(self, Target: int) -> List[List[int]]:
        
        primes = [True]*(Target+1)
        res = []

        p = 2
        while p*p <= Target:
            if primes[p] == True:
                for i in range(p*p , Target+1 , p):
                    primes[i] = False
            p+=1


        for i in range( 2 , Target//2 +1):
            if primes[i] and primes[Target - i]:
                res.append([i , Target-i])
        return res
