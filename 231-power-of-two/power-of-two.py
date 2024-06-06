class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Handle edge cases for negative numbers and zero
        if n <= 0:
            return False
        # Base case: 1 is a power of two (2^0)
        if n == 1:
            return True
        # Immediate False: If n is not divisible by 2, it's not a power of two
        if n % 2 != 0:
            return False
        # Recursive case: divide n by 2 and check again
        return self.isPowerOfTwo(n // 2)