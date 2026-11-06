class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
        arr = []
        for i in range(len(nums)):
            if nums[i]%2 ==0:
                arr.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2 !=0:
                arr.append(nums[i])
        return arr
        
        # l = 0
        # r = len(nums) - 1
        # while l<r:
        #     if nums[l]%2 ==0:
        #         l+=1
        #     elif nums[l]%2 !=0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #     if nums[r]%2!=0:
        #         if nums[l]%2==0:
        #             l+=1
        #             nums[l], nums[r] = nums[r], nums[l]
        #             l+=1
        #     r-=1
        # return nums
            
        