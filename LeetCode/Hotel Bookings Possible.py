# link   : https://www.interviewbit.com/problems/hotel-bookings-possible/
# author : Mohamed Ibrahim

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrival = sorted(arrive)
        departure = sorted(depart)
        i, j = 0, 0
        rooms = 0
        while i < len(arrival) and j < len(departure):
            if arrival[i] <= departure[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            if rooms > K:
                return 0
        return 1
        
        
