class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 0 :
                count += 1
                i += 1
                result += count
            i += 1
        return result