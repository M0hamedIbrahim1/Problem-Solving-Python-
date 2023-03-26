# link   : https://leetcode.com/problems/reverse-bits/description/
# author : Mohamed Ibrahim

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
        
        
