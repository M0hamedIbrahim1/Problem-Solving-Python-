# link   : https://leetcode.com/problems/add-binary/
# author : Mohamed Ibrahim

class Solution:
    def addBinary(self, a, b):
        return str(bin(int(a,2)+int(b,2)))[2:]
        
        
