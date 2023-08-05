# link   : https://leetcode.com/contest/biweekly-contest-97/problems/maximum-number-of-integers-to-choose-from-a-range-i/
# author : Mohamed Ibrahim

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s ,cnt = 0 , 0
        banned = set(banned)
        for i in range(1 , n+1):
            if s + i <= maxSum :
                if i not in banned:
                    s+=i
                    cnt+=1
        return cnt
