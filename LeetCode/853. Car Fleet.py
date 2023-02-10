# link    : https://leetcode.com/problems/car-fleet/description/
# author : Mohamed Ibrahim 



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[x,y] for x,y in zip(position,speed)]
        stack = []
        for x,y in sorted(pairs)[::-1]:
            stack.append((target - x) / y)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        
        
