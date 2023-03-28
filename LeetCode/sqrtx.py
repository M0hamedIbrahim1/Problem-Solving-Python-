# link   : https://leetcode.com/problems/sqrtx/
# author : Mohamed Ibrahim

def mySqrt(self, x):
    lo, hi = 0, x

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * mid > x:
            hi = mid - 1
        elif mid * mid < x:
            lo = mid + 1
        else:
            return mid

