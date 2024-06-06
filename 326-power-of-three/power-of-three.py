class Solution(object):
    def isPowerOfThree(self, n):
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
        # immediate false case:
        if n % 3 != 0:
            return False 
        # recursive case:
        return self.isPowerOfThree(n // 3)