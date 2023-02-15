# link : https://leetcode.com/problems/add-to-array-form-of-integer/description/
# author : Mohamed ibrahim


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
            num = int("".join([str(x) for x in num]))
            ans = [int(i) for i in list(str(k + num))]
            return ans
            
            
