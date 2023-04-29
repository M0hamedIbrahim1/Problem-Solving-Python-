# link   : https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
# author : Mohamed Ibrahim

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = defaultdict(int)
        res,ans = 0,[]
        for i in range(len(A)):
            d[A[i]]+=1
            d[B[i]]+=1

            if d[A[i]] == 2 :
                res+=1
            if A[i] != B[i] and d[B[i]] == 2:
                res+=1
            ans.append(res)
        return ans
        
