# link   : https://leetcode.com/problems/fizz-buzz/description/
# author : Mohamed Ibrahim

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0]*(n+1)
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5  == 0:
                ans[i] = "FizzBuzz"
            elif i % 3 == 0:
                ans[i] = "Fizz"
            elif i % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(i)
            
        return ans[1:]
        
        
