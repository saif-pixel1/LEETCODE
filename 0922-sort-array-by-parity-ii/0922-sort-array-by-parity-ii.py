class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        l = 0 
        r = l+1

        while l<len(nums) and r<len(nums):
            if nums[l]%2==0:
                l+=2
                continue
            if nums[r]%2!=0:
                r+=2
                continue

            if nums[l]%2!=0 and nums[r]%2 ==0:
                nums[l],nums[r] = nums[r], nums[l]
                l+=2
                r+=2
            
    
        return nums
            