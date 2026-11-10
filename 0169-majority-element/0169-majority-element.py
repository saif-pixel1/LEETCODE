class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = 1;c=0
        n = len(nums)//2 
        if len(nums) <=1:
            return nums[0]
        nums.sort()

        return nums[n]
     