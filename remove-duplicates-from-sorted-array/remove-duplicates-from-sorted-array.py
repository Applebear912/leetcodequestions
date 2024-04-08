class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftIndex = 1

        for rightIndex in range(1,len(nums)):
            if nums[rightIndex] != nums[rightIndex-1]:
                nums[leftIndex] = nums[rightIndex]
                leftIndex+=1

        return leftIndex
        