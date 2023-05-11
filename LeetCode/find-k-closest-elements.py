# link : https://leetcode.com/problems/find-k-closest-elements/
# author : Mohamed Ibrahim

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr,key = lambda i:abs(x-i))

        return sorted(arr[:k])
        
