# link   : https://leetcode.com/contest/weekly-contest-331/problems/rearranging-fruits/
# author : Mohamed Ibrahim

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

                                                    # Example: [4, 4, 4, 4, 3] [5, 5, 5, 5, 3]

        c1, c2 = Counter(basket1), Counter(basket2) # c1, c2 = {3:1, 4:4}, {3:1, 5:4}
        c = c1 + c2                                 #      c = {3:2, 4:4, 5:4} 
                                                    #
        for n in c:                                 #   c[3] = 2//2 = 1
            c[n], r = divmod(c[n],2)                #   c[4] = 4//2 = 2
            if r: return -1                         #   c[5] = 4//2 = 2

        mn = min(c)                                 #     mn = 3
        c1-= c                                      #     c1 = {4: 2}
        c2-= c                                      #     c2 = {5: 2}

        arr = sorted(list(c1.elements())            #    arr = sorted([4,4]+[5,5]) = [4,4,5,5] 
                       + list(c2.elements()))
        print(arr)
        return sum(min(2*mn, arr[i])                # return sum(min(6,4), min(6,4)) = 8
                     for i in range(len(arr)//2))

                     # min(2*mn, arr[i]) 
                    #  Consider these two test cases:
                    # [2,2,100,100],[3,3,200,200] (answer 5)
                    # [1,100,100],[1,200,200] (answer 2)
                    # Why is the approach different for these two cases?
