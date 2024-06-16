class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left = 0
        right = x // 2
        while right >= left:
            mid = (left + right) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1


        
