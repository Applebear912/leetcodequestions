class Solution(object):
    def mySqrt(self, x):

        """
        :type x: int
        :rtype: int
        """
        y = 0
        while y * y <= x:
            y += 1
            
        return y-1

        
