class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                if mid + 1 >= len(nums):
                    return mid + 1
                if target < nums[mid + 1]:
                    return mid + 1
                left = mid + 1

            if nums[mid] > target:
                if mid - 1 < 0:
                    return mid
                if target > nums[mid - 1]:
                    return mid
                right = mid - 1