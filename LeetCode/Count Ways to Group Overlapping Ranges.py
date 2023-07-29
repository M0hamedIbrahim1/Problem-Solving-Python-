# link : https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/description/
# author : Mohamed Ibrahim

class Solution:
    def countWays(self, intervals: List[List[int]]) -> int:
		
        ans=2
		
        intervals.sort(key=lambda x: x[0])
		
        mer = []
		
        for interval in intervals:
            if not mer or mer[-1][1] < interval[0]:
                mer.append(interval)
            else:
                mer[-1][1] = max(mer[-1][1], interval[1])
				
        return pow(ans,len(mer),1000_000_007)
