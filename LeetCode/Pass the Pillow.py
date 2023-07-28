

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        

        start = 1
        direction = True
        while time > 0:
            if direction == True:
                start += 1
            else:
                start -= 1
            if start == n:
                direction = False
            if start == 1:
                direction = True
            time -= 1
        return start
        
#         n-= 1                       # the count of passes per traverse is one less than the count of the persons
#         time%= n+n                  # account for the full laps to return to the beginning
        
#         return n+1 - abs(n - time)  # determine the final position
