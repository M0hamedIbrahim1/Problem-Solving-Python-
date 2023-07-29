# link  : https://leetcode.com/contest/biweekly-contest-99/problems/count-total-number-of-colored-cells/
# author : Mohamed Ibrahim

class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:return 1
        if n == 2 : return 5
        res = 2
        cnt = 1
        for i in range(2 , n+1):
            if i == n:res = res + cnt + 2
            else:
                cnt += 2
                res+=(cnt*2)
        return res
