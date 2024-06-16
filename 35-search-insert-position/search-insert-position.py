class Solution(object):
    def binary(self, left, right, nums, target):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:

            # Out of bounds
            if mid + 1 >= len(nums):
                return mid + 1

            if target < nums[mid + 1]:
                return mid + 1
            return self.binary(mid + 1, right, nums, target)


        # Target is smaller than nums[mid]
        # Out of bounds
        if mid - 1 < 0:
            return mid

        if target > nums[mid - 1]:
            return mid

        return self.binary(left, mid - 1, nums, target)
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary(0, len(nums)-1, nums, target)