# link   : https://leetcode.com/problems/plus-one/description/
# author : Mohamed Ibrahim

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst = [str(i) for i in digits]
        LST = "".join(lst)
        n = int(LST)
        n+=1
        return [int(i) for i in str(n)]
        
