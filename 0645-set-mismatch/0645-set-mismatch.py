class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()

        duplicate = -1
        missing = 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                duplicate = nums[i]

            if nums[i] == missing:
                missing += 1

        return [duplicate, missing]