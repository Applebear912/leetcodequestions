class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # edge case:
        if n <= 0:
            return False
        # base case:
        if n == 1:
            return True
        # immdediate false:
        if n % 4 != 0:
            return False
        # recursive case:
        return self.isPowerOfFour(n // 4)