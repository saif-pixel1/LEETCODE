class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l = 0
        r = len(nums) - 1
        k = 0 

        while k<=r:
            if nums[k] == 2:
                nums[k], nums[r] = nums[r], nums[k]
                r-=1
            elif nums[k] == 0:
                nums[k], nums[l] = nums[l], nums[k]
                k+=1
                l+=1
            elif nums[k] == 1:
                k+=1
        return nums

        
    
                    
            