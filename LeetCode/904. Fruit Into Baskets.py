# link   : https://leetcode.com/problems/fruit-into-baskets/description/
# author : Mohamed Ibrahim


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        right = 1
        answer = -1
        fruit_dict = {fruits[left]: 0}
        for right, fruit in enumerate(fruits):

            fruit_dict[fruit] = right
            if len(fruit_dict) > 2:

                answer = max(answer, right - left)
                index = min(fruit_dict.values())
                del fruit_dict[fruits[index]]
                left = index + 1

        fruit_dict.clear()
        return max(answer, right - left + 1)
        
        
        
        
