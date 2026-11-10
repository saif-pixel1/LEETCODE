class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = 1;c=0
        n = len(nums)//2 
        if len(nums) <=1:
            return nums[0]

        nums.sort()
        while l<len(nums):
            if nums[l-1] == nums[l]:
                c+=1
                l+=1
                if c==n:
                    return nums[l-1]

            else:
                c=0
                l+=1
                continue
        

        