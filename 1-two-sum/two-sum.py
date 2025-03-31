class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        for i in range(len(nums)):
            if target-nums[i] in obj:
                return [obj[target-nums[i]], i]
            obj[nums[i]] = i
            


