class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        # loop through nums, check if current pointer is pointing to real num, if it is move to next
        # when locate a zero,  look for next non-zero values, and swap it with current pointer
        # break the loop when pointer == len of num
        if len(nums) == 1:
            return nums

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[pointer]
                nums[pointer] = nums[i]
                nums[i] = temp
                pointer += 1

        return nums