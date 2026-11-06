class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        while l<r:
            if nums[l]%2 ==0:
                l+=1
            elif nums[r]%2 !=0:
                r-=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
                l+=1
        return nums
            
        