# link : https://leetcode.com/problems/make-k-subarray-sums-equal/description/
# author : Mohamed ibrahim

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        visited = set()
        n = len(arr)
        res = 0
        for i in range(k):
            curlist = []
            j = i
            while j not in visited:
                visited.add(j)
                curlist.append(arr[j])
                j = (j+k)%n
            curlist.sort()
            m = len(curlist)//2
            res += sum([abs(num - curlist[m]) for num in curlist])
        return res

            
