class Solution(object):

    def signFunc(self, x):
        if x == 0:
            return 0
        if x > 0:
            return 1
        if x < 0:
            return -1

    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = nums[0]
        for i in range(1, len(nums)):
            product *= nums[i]
        return self.signFunc(product)