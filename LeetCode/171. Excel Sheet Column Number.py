# link   : https://leetcode.com/problems/excel-sheet-column-number/description/
# author : Mohamed Ibrahim


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for s in columnTitle:
            res = res*26 + ord(s)-ord('A')+1
        return res
        
        
